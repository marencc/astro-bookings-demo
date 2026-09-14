import anyio
import httpx

from astro_bookings.app import app


async def get_json(path: str) -> tuple[int, dict]:
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.get(path)

    return response.status_code, response.json()


def test_health_status():
    status_code, payload = anyio.run(get_json, "/health")

    assert status_code == 200
    assert payload == {"status": "ok"}


def test_root_welcome():
    status_code, payload = anyio.run(get_json, "/")

    assert status_code == 200
    assert payload == {"message": "Welcome to AstroBookings API"}


def test_openapi_schema_includes_system_endpoints():
    status_code, payload = anyio.run(get_json, "/openapi.json")

    assert status_code == 200
    assert "/" in payload["paths"]
    assert "/health" in payload["paths"]
