"""FastAPI application for the AstroBookings demo."""

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

from astro_bookings import __version__
from astro_bookings.rockets import router as rockets_router


class HealthStatus(BaseModel):
    """Public health-check response."""

    model_config = ConfigDict(json_schema_extra={"example": {"status": "ok"}})

    status: str


class RootWelcome(BaseModel):
    """Public root endpoint response."""

    model_config = ConfigDict(
        json_schema_extra={"example": {"message": "Welcome to AstroBookings API"}}
    )

    message: str


app = FastAPI(
    title="AstroBookings API",
    summary="A backend API for offering bookings for rocket launches.",
    version=__version__,
)
app.include_router(rockets_router)


@app.get(
    "/",
    response_model=RootWelcome,
    summary="Welcome to the API",
    tags=["system"],
)
async def get_root() -> RootWelcome:
    """Return a minimal API welcome message."""
    return RootWelcome(message="Welcome to AstroBookings API")


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
