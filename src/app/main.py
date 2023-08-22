# [Standard Library]
import os
from pathlib import Path

# [3rd Party]
from dotenv import load_dotenv
from fastapi import FastAPI

from .api.api_v1.api import api_router

WORKING_DIRECTORY = Path(__file__).resolve().parent.parent.parent
dotenv_path = os.path.join(WORKING_DIRECTORY, '.env')
load_dotenv(dotenv_path)


app = FastAPI()

app.include_router(api_router)
