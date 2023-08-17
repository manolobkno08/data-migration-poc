# [3rd Party]
from fastapi import APIRouter

from .endpoints import department
from .endpoints import hired_employee
from .endpoints import job

api_router = APIRouter()
api_router.include_router(
    department.router, prefix="", tags=["department"])
# api_router.include_router(hired_employee.router,
#                           prefix="/hired_employee", tags=["hired_employee"])
api_router.include_router(job.router, prefix="", tags=["job"])
