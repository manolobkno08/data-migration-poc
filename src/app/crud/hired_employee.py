# [3rd Party]
from app.models import models
from app.schemas import hired_employee
from sqlalchemy.orm import Session


def get(db: Session, hired_employee_id: int):
    return db.query(models.Hired_Employee).filter(models.Hired_Employee.id == hired_employee_id).first()


def get_all(db: Session):
    return db.query(models.Hired_Employee).all()


def create(db: Session, hired_employee: hired_employee.HiredEmployeeCreate):
    db_hired_employee = models.Hired_Employee(
        **hired_employee.dict())
    db.add(db_hired_employee)
    db.commit()
    db.refresh(db_hired_employee)
    return db_hired_employee
