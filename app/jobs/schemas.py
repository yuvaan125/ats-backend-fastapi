from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    company: str
    salary: int
    location: str
    description: str | None = None