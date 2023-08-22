# [Standard Library]
from typing import List

# [3rd Party]
from app.crud import department as crud_department
from app.db import get_db
from app.schemas import department as department_schema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/department/", response_model=department_schema.Department)
def create_department(department: department_schema.DepartmentCreate, db: Session = Depends(get_db)):
    db_department = crud_department.get(db, department.id)
    if db_department:
        raise HTTPException(
            status_code=400, detail="Department already registered")
    return crud_department.create(db=db, department=department)


@router.get("/department/", response_model=List[department_schema.Department])
def read_departments(db: Session = Depends(get_db)):
    db_departments = crud_department.get_all(db)
    if db_departments is None:
        raise HTTPException(status_code=404, detail="Departments not found")
    return db_departments
