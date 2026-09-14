import anyio
import httpx

from astro_bookings.app import app


def test_api_smoke_health_and_docs():
    async def smoke_request() -> tuple[httpx.Response, httpx.Response]:
        transport = httpx.ASGITransport(app=app)

        async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
            return await client.get("/health"), await client.get("/openapi.json")

    health_response, openapi_response = anyio.run(smoke_request)

    assert health_response.status_code == 200
    assert health_response.json() == {"status": "ok"}
    assert openapi_response.status_code == 200
    assert openapi_response.json()["info"]["title"] == "AstroBookings API"
