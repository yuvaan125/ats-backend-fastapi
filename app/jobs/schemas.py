from datetime import datetime
from pydantic import BaseModel


class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    salary: int
    location: str
    description: str | None
    created_at: datetime


class JobCreate(BaseModel):
    title: str
    company: str
    salary: int
    location: str
    description: str | None = None