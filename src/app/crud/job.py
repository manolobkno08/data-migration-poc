# [3rd Party]
from sqlalchemy.orm import Session

from app.models import models
from app.schemas import job


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
