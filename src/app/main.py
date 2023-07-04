# [Standard Library]
import os
from pathlib import Path

# [3rd Party]
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

WORKING_DIRECTORY = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(WORKING_DIRECTORY, '.env')
load_dotenv(dotenv_path)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv("SERVER"), port=os.getenv("PORT"))
