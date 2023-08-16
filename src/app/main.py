# [Standard Library]
import os
from pathlib import Path

# [3rd Party]
import uvicorn
from dotenv import load_dotenv
from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy.orm import Session

from .crud import department as crud_department
from .crud import hired_employee as crud_hired_employee
from .crud import job as crud_job
from .db import engine
from .db import get_db
from .models import models
from .schemas import department_schema
from .schemas import hired_employee_schema
from .schemas import job_schema

models.Base.metadata.create_all(bind=engine)


WORKING_DIRECTORY = Path(__file__).resolve().parent.parent.parent
dotenv_path = os.path.join(WORKING_DIRECTORY, '.env')
load_dotenv(dotenv_path)


app = FastAPI()


@app.post("/department/", response_model=department_schema.Department)
def create_department(department: department_schema.DepartmentCreate, db: Session = Depends(get_db)):
    db_department = crud_department.get(db, department.id)
    if db_department:
        raise HTTPException(
            status_code=400, detail="Department already registered")
    return crud_department.create(db=db, department=department)


@app.get("/department/", response_model=department_schema.Department)
def read_departments(db: Session = Depends(get_db)):
    db_departments = crud_department.get_all(db)
    if db_departments is None:
        raise HTTPException(status_code=404, detail="Departments not found")
    return db_departments


if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv("SERVER"), port=8000)
