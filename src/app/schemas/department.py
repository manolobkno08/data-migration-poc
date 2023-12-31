# [Standard Library]
from typing import List
from typing import Union

# [3rd Party]
from pydantic import BaseModel


class DepartmentBase(BaseModel):
    id: int
    department: str


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(BaseModel):
    department: Union[str, None] = None


class DepartmentDelete(BaseModel):
    detail: Union[str, None] = None


class Department(DepartmentBase):

    class Config:
        orm_mode = True
