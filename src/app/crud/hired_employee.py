# [3rd Party]
from sqlalchemy.orm import Session

from ..models import models
from ..schemas import hired_employee


def get(db: Session, hired_employee_id: int):
    return db.query(models.Hired_Employee).filter(models.Hired_Employee.id == hired_employee_id).first()


def get_all(db: Session):
    return db.query(models.Hired_Employee).all()


def create(db: Session, hired_employee: hired_employee.HiredEmployeeCreate, department_id: int, job_id: int):
    db_hired_employee = models.Hired_Employee(
        **hired_employee.dict(), department_id=department_id, job_id=job_id)
    db.add(db_hired_employee)
    db.commit()
    db.refresh(db_hired_employee)
    return db_hired_employee
