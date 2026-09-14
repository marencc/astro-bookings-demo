import anyio
import httpx

from astro_bookings.app import app


async def post_rocket(payload: dict) -> tuple[int, dict]:
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.post("/rockets", json=payload)

    return response.status_code, response.json()


async def get_json(path: str) -> tuple[int, dict]:
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.get(path)

    return response.status_code, response.json()


def test_create_rocket_returns_accepted_rocket():
    payload = {"name": "Aurora", "range": "orbital", "capacity": 4}

    status_code, body = anyio.run(post_rocket, payload)

    assert status_code == 201
    assert body == payload


def test_create_rocket_accepts_all_supported_ranges():
    for rocket_range in ("suborbital", "orbital", "moon", "mars"):
        payload = {"name": f"{rocket_range}-vehicle", "range": rocket_range, "capacity": 1}

        status_code, body = anyio.run(post_rocket, payload)

        assert status_code == 201
        assert body["range"] == rocket_range


def test_create_rocket_accepts_capacity_boundaries():
    for capacity in (1, 10):
        payload = {"name": f"Capacity {capacity}", "range": "moon", "capacity": capacity}

        status_code, body = anyio.run(post_rocket, payload)

        assert status_code == 201
        assert body["capacity"] == capacity


def test_create_rocket_rejects_invalid_range():
    status_code, body = anyio.run(
        post_rocket,
        {"name": "Voyager", "range": "interstellar", "capacity": 3},
    )

    assert status_code == 422
    assert body["detail"]


def test_create_rocket_rejects_capacity_outside_allowed_range():
    for capacity in (0, 11):
        status_code, body = anyio.run(
            post_rocket,
            {"name": "Boundary", "range": "mars", "capacity": capacity},
        )

        assert status_code == 422
        assert body["detail"]


def test_create_rocket_rejects_missing_required_fields():
    valid_payload = {"name": "Aurora", "range": "orbital", "capacity": 4}

    for field in ("name", "range", "capacity"):
        payload = valid_payload.copy()
        payload.pop(field)

        status_code, body = anyio.run(post_rocket, payload)

        assert status_code == 422
        assert body["detail"]


def test_create_rocket_rejects_empty_name():
    status_code, body = anyio.run(
        post_rocket,
        {"name": "", "range": "suborbital", "capacity": 2},
    )

    assert status_code == 422
    assert body["detail"]


def test_create_rocket_rejects_non_whole_number_capacity():
    status_code, body = anyio.run(
        post_rocket,
        {"name": "Fractional", "range": "orbital", "capacity": 2.5},
    )

    assert status_code == 422
    assert body["detail"]


def test_openapi_schema_includes_rockets_endpoint_and_constraints():
    status_code, schema = anyio.run(get_json, "/openapi.json")

    assert status_code == 200
    assert "/rockets" in schema["paths"]

    operation = schema["paths"]["/rockets"]["post"]
    assert operation["requestBody"]["content"]["application/json"]["schema"]["$ref"].endswith(
        "/Rocket"
    )
    assert operation["responses"]["201"]["content"]["application/json"]["schema"]["$ref"].endswith(
        "/Rocket"
    )

    rocket_schema = schema["components"]["schemas"]["Rocket"]
    assert rocket_schema["required"] == ["name", "range", "capacity"]
    assert rocket_schema["properties"]["capacity"]["minimum"] == 1
    assert rocket_schema["properties"]["capacity"]["maximum"] == 10

    range_ref = rocket_schema["properties"]["range"]["$ref"]
    range_schema_name = range_ref.rsplit("/", 1)[-1]
    assert schema["components"]["schemas"][range_schema_name]["enum"] == [
        "suborbital",
        "orbital",
        "moon",
        "mars",
    ]
