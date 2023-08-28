# [Standard Library]
from typing import List
from typing import Union

# [3rd Party]
from pydantic import BaseModel


class JobBase(BaseModel):
    id: int
    job: str


class JobCreate(JobBase):
    pass


class JobUpdate(BaseModel):
    job: Union[str, None] = None


class JobDelete(BaseModel):
    detail: Union[str, None] = None


class Job(JobBase):
    # from .hired_employee_schema import HiredEmployee
    # h_employee: List[HiredEmployee] = []

    class Config:
        orm_mode = True
