# [Standard Library]
from typing import List
from typing import Union

# [3rd Party]
from pydantic import BaseModel

from .department import Department
from .job import Job


class HiredEmployeeBase(BaseModel):
    id: int
    name: Union[str, None] = None
    datetime: Union[str, None] = None
    department_id: Union[int, None] = None
    job_id: Union[int, None] = None


class HiredEmployeeCreate(HiredEmployeeBase):
    pass


class HiredEmployeeUpdate(BaseModel):
    name: Union[str, None] = None
    datetime: Union[str, None] = None
    department_id: Union[int, None] = None
    job_id: Union[int, None] = None


class HiredEmployeeDelete(BaseModel):
    detail: Union[str, None] = None


class HiredEmployee(HiredEmployeeBase):
    # job: Job
    # department: Department

    class Config:
        orm_mode = True
