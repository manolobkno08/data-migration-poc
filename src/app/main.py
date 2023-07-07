# [Standard Library]
import os
from pathlib import Path

# [3rd Party]
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import column
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

WORKING_DIRECTORY = Path(__file__).resolve().parent.parent.parent
dotenv_path = os.path.join(WORKING_DIRECTORY, '.env')
load_dotenv(dotenv_path)

app = FastAPI()


conn_string = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('POSTGRES_DB')}"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "Hello Manolo"}


@app.get("/user/{user_id}")
async def read_item(user_id: int):
    engine = create_engine(conn_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = text("SELECT * FROM jobs WHERE id = :id")
    result = session.execute(query, {"id": user_id})
    res = result.fetchone()
    session.close()

    if res is not None:
        info = dict(res._asdict())
        return info
    else:
        return {"message": "No data found"}


if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv("SERVER"), port=8000)
