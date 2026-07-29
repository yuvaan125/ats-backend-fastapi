from fastapi import FastAPI
from app.health.router import router
from app.jobs.router import router as jobs_router

app = FastAPI(
    title="ATS Backend API",
    version="1.0.0",
)

app.include_router(router)
app.include_router(jobs_router)