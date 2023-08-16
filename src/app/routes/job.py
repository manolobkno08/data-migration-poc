# [3rd Party]
from fastapi import APIRouter

job = APIRouter()


@job.get("/jobs")
def hello_world():
    return "Hello World"


