# [3rd Party]
from app.models import models
from app.schemas import department
from sqlalchemy.orm import Session


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


def delete(db: Session, department_id: int):
    db_department = db.query(models.Department).filter(
        models.Department.id == department_id).first()
    if db_department:
        db.delete(db_department)
        db.commit()
        return {"detail": "Department deleted successfully"}


def update(db: Session, department_id: int, department: department.DepartmentUpdate):
    db_department = db.query(models.Department).filter(
        models.Department.id == department_id).first()
    if db_department:
        db_department.department = department.department
        db.commit()
        db.refresh(db_department)
        return db_department
