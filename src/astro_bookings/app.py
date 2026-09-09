"""FastAPI application for the AstroBookings demo."""

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict


class HealthStatus(BaseModel):
    """Public health-check response."""

    model_config = ConfigDict(json_schema_extra={"example": {"status": "ok"}})

    status: str


app = FastAPI(
    title="AstroBookings API",
    summary="A backend API for offering bookings for rocket launches.",
    version="0.1.0",
)


@app.get(
    "/health",
    response_model=HealthStatus,
    summary="Check API health",
    tags=["system"],
)
async def get_health() -> HealthStatus:
    """Return the API health status."""
    return HealthStatus(status="ok")


def main() -> int:
    """Run the API with Uvicorn."""
    uvicorn.run("astro_bookings.app:app", host="127.0.0.1", port=8000, reload=True)
    return 0
