# [3rd Party]
from sqlalchemy.orm import Session

from app.models import models
from app.schemas import department


def get(db: Session, department_id: int):
    return db.query(models.Department).filter(models.Department.id == department_id).first()


def get_all(db: Session):
    return db.query(models.Department).all()


def create(db: Session, department: department.DepartmentCreate):
    db_department = models.Department(**department.dict())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department
