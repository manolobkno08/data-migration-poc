# [3rd Party]
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from ..db.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job = Column(String)

    h_employee = relationship(
        "Hired_Employee", back_populates="job_relationship")


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String)

    h_employee = relationship(
        "Hired_Employee", back_populates="department_relationship")


class Hired_Employee(Base):
    __tablename__ = "hired_employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    datetime = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))

    job_relationship = relationship("Job", back_populates="h_employee")
    department_relationship = relationship(
        "Department", back_populates="h_employee")
