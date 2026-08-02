from datetime import datetime
from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    company: str
    salary: int
    location: str
    description: str | None = None


class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    salary: int
    location: str
    description: str | None = None
    created_at: datetime