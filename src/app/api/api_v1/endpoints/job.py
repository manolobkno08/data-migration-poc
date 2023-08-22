# [Standard Library]
from typing import List

# [3rd Party]
from app.crud import job as crud_job
from app.db import get_db
from app.schemas import job as job_schema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/job/", response_model=job_schema.Job)
def create_job(job: job_schema.JobCreate, db: Session = Depends(get_db)):
    db_job = crud_job.get(db, job.id)
    if db_job:
        raise HTTPException(
            status_code=400, detail="Job already registered")
    return crud_job.create(db=db, job=job)


@router.get("/job/", response_model=List[job_schema.Job])
def read_jobs(db: Session = Depends(get_db)):
    db_jobs = crud_job.get_all(db)
    if db_jobs is None:
        raise HTTPException(status_code=404, detail="Jobs not found")
    return db_jobs
