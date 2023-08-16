# [Standard Library]
from typing import List
from typing import Union

# [3rd Party]
from pydantic import BaseModel

from .hired_employee_schema import HiredEmployee


class JobBase(BaseModel):
    id: int
    job: str


class JobCreate(JobBase):
    pass


class Job(JobBase):
    h_employee: List[HiredEmployee] = []

    class Config:
        orm_mode = True
