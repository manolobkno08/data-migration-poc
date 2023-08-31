# [Standard Library]
from typing import List

# [3rd Party]
from app.crud import Crud
from app.db import get_db
from app.models import models
from app.schemas import hired_employee as hired_employee_schema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

router = APIRouter()
crud = Crud()


@router.get("/hired_employee/", response_model=List[hired_employee_schema.HiredEmployee])
def read_hired_employees(db: Session = Depends(get_db)):
    db_hired_employees = crud.get_all(db=db, model=models.Hired_Employee)
    if db_hired_employees is None:
        raise HTTPException(
            status_code=404, detail="Hired Employees not found")
    return db_hired_employees


@router.post("/hired_employee/", response_model=hired_employee_schema.HiredEmployee)
def create_hired_employee(hired_employee: hired_employee_schema.HiredEmployeeCreate, db: Session = Depends(get_db)):
    db_hired_employee = crud.get(
        db=db, model=models.Hired_Employee, id=hired_employee.id)
    if db_hired_employee:
        raise HTTPException(
            status_code=400, detail="Hired Employee already registered")
    return crud.create(db=db, model=models.Hired_Employee, data=hired_employee)


@router.delete("/hired_employee/{hired_employee_id}", response_model=hired_employee_schema.HiredEmployeeDelete)
def delete_hired_employee(hired_employee_id: int, db: Session = Depends(get_db)):
    db_hired_employee = crud.get(
        db=db, model=models.Hired_Employee, id=hired_employee_id)
    if db_hired_employee is None:
        raise HTTPException(
            status_code=404, detail="Hired Employee not found")
    return crud.delete(db=db, model=models.Hired_Employee, id=hired_employee_id)


@router.put("/hired_employee/{hired_employee_id}", response_model=hired_employee_schema.HiredEmployee)
def update_hired_employee(hired_employee_id: int, hired_employee: hired_employee_schema.HiredEmployeeUpdate, db: Session = Depends(get_db)):
    db_hired_employee = crud.get(
        db=db, model=models.Hired_Employee, id=hired_employee_id)
    if db_hired_employee is None:
        raise HTTPException(
            status_code=404, detail="Hired Employee not found")
    return crud.update(db=db, model=models.Hired_Employee, id=hired_employee_id, data=hired_employee)
