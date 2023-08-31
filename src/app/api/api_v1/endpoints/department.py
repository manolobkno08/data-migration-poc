# [Standard Library]
from typing import List

# [3rd Party]
from app.crud import Crud
from app.db import get_db
from app.models import models
from app.schemas import department as department_schema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

router = APIRouter()
crud = Crud()


@router.get("/department/", response_model=List[department_schema.Department])
def read_departments(db: Session = Depends(get_db)):
    db_departments = crud.get_all(db=db, model=models.Department)
    if db_departments is None:
        raise HTTPException(status_code=404, detail="Departments not found")
    return db_departments


@router.post("/department/", response_model=department_schema.Department)
def create_department(department: department_schema.DepartmentCreate, db: Session = Depends(get_db)):
    db_department = crud.get(db=db, model=models.Department, id=department.id)
    if db_department:
        raise HTTPException(
            status_code=400, detail="Department already registered")
    return crud.create(db=db, model=models.Department, data=department)


@router.delete("/department{department_id}", response_model=department_schema.DepartmentDelete)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    db_department = crud.get(db=db, model=models.Department, id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return crud.delete(db=db, model=models.Department, id=department_id)


@router.put("/department/{department_id}", response_model=department_schema.Department)
def update_department(department_id: int, department: department_schema.DepartmentUpdate, db: Session = Depends(get_db)):
    db_department = crud.get(db=db, model=models.Department, id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return crud.update(db=db, model=models.Department, id=department_id, data=department)
