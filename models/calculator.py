from pydantic import BaseModel


class Numbers(BaseModel):
    """Request body for all calculator endpoints."""

    a: float
    b: float


class Result(BaseModel):
    """Response body for all calculator endpoints."""

    a: float
    b: float
    operation: str
    result: float
