"""Rocket management API routes."""

from enum import StrEnum

from fastapi import APIRouter, status
from pydantic import BaseModel, ConfigDict, Field


class RocketRange(StrEnum):
    """Supported rocket mission ranges."""

    SUBORBITAL = "suborbital"
    ORBITAL = "orbital"
    MOON = "moon"
    MARS = "mars"


class Rocket(BaseModel):
    """Rocket request and response schema."""

    model_config = ConfigDict(json_schema_extra={
        "example": {"name": "Aurora", "range": "orbital", "capacity": 4}
    })

    name: str = Field(min_length=1)
    range: RocketRange
    capacity: int = Field(ge=1, le=10, strict=True)


router = APIRouter(prefix="/rockets", tags=["rockets"])


@router.post("", response_model=Rocket, status_code=status.HTTP_201_CREATED)
async def create_rocket(rocket: Rocket) -> Rocket:
    """Accept and return a rocket representation."""
    return rocket
