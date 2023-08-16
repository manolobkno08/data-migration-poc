# [Standard Library]
from typing import List
from typing import Union

# [3rd Party]
from pydantic import BaseModel

from .department_schema import Department
from .job_schema import Job


# HIRED EMPLOYEES
class HiredEmployeeBase(BaseModel):
    id: int
    name: Union[str, None] = None
    datetime: Union[str, None] = None
    department_id: Union[int, None] = None
    job_id: Union[int, None] = None


class HiredEmployeeCreate(HiredEmployeeBase):
    pass


class HiredEmployee(HiredEmployeeBase):
    job: Job
    department: Department

    class Config:
        orm_mode = True
