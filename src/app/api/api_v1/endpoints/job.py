# [Standard Library]
from typing import List

# [3rd Party]
from app.crud import Crud
from app.db import get_db
from app.models import models
from app.schemas import job as job_schema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

router = APIRouter()
crud = Crud()


@router.get("/job/", response_model=List[job_schema.Job])
def read_jobs(db: Session = Depends(get_db)):
    db_jobs = crud.get_all(db=db, model=models.Job)
    if db_jobs is None:
        raise HTTPException(status_code=404, detail="Jobs not found")
    return db_jobs


@router.post("/job/", response_model=job_schema.Job)
def create_job(job: job_schema.JobCreate, db: Session = Depends(get_db)):
    db_job = crud.get(db=db, model=models.Job, id=job.id)
    if db_job:
        raise HTTPException(
            status_code=400, detail="Job already registered")
    return crud.create(db=db, model=models.Job, data=job)


@router.delete("/job/{job_id}", response_model=job_schema.JobDelete)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = crud.get(db=db, model=models.Job, id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return crud.delete(db=db, model=models.Job, id=job_id)


@router.put("/job/{job_id}", response_model=job_schema.Job)
def update_job(job_id: int, job: job_schema.JobUpdate, db: Session = Depends(get_db)):
    db_job = crud.get(db=db, model=models.Job, id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return crud.update(db=db, model=models.Job, id=job_id, data=job)
