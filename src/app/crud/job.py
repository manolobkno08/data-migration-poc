# [3rd Party]
from app.models import models
from app.schemas import job
from sqlalchemy.orm import Session


def get(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()


def get_all(db: Session):
    return db.query(models.Job).all()


def create(db: Session, job: job.JobCreate):
    db_job = models.Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def delete(db: Session, job_id: int):
    db_job = db.query(models.Job).filter(
        models.Job.id == job_id).first()
    if db_job:
        db.delete(db_job)
        db.commit()
        return {"detail": "Job deleted successfully"}


def update(db: Session, job_id: int, job: job.JobUpdate):
    db_job = db.query(models.Job).filter(
        models.Job.id == job_id).first()
    if db_job:
        db_job.job = job.job
        db.commit()
        db.refresh(db_job)
        return db_job
