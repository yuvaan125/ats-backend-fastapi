from fastapi import APIRouter

from app.jobs.repository import get_all_jobs
from app.jobs.schemas import JobCreate, JobResponse

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.get("/", response_model=list[JobResponse])
def get_jobs():
    return get_all_jobs()


@router.post("/")
def create_job(job: JobCreate):
    return {
        "message": "Job created successfully",
        "data": job
    }


@router.get("/{job_id}")
def get_job(job_id: int):
    return {
        "message": "Get job by ID - Not implemented",
        "job_id": job_id
    }


@router.put("/{job_id}")
def update_job(job_id: int):
    return {
        "message": "Replace entire job - Not implemented",
        "job_id": job_id
    }


@router.patch("/{job_id}")
def partial_update_job(job_id: int):
    return {
        "message": "Partially update job - Not implemented",
        "job_id": job_id
    }


@router.delete("/{job_id}")
def delete_job(job_id: int):
    return {
        "message": "Delete job - Not implemented",
        "job_id": job_id
    }