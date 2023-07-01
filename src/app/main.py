# [Standard Library]
import os

# [3rd Party]
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv('.env')

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv("SERVER"), port=os.getenv("PORT"))
