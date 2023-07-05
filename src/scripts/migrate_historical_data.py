#!/usr/bin/env python3
# [Standard Library]
import os
import shutil
import sys
from pathlib import Path

# [3rd Party]
import numpy as np
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Add the parent directory to the path so we can import the app modules
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from app.db import DataBaseConnection


WORKING_DIRECTORY = Path(__file__).resolve().parent.parent

dotenv_path = os.path.join(WORKING_DIRECTORY, '.env')
load_dotenv(dotenv_path)


def load_to_db(df, table_name):
    conn_string = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('POSTGRES_DB')}"
    db = create_engine(conn_string)
    conn = db.connect()

    try:
        df.to_sql(table_name, con=conn,
                  if_exists='replace', index=False)
        print(
            f"====> data migration for '{table_name}' ran successfully\n    File moved to processed zone\n")
        conn.close()
        return 0
    except Exception as e:
        print(f"====> Error: {e}\n")
        conn.close()
        return 1


def parse_csv_files_and_save(csv_to_migrate, destiny_path):

    files = os.listdir(csv_to_migrate)

    if len(files) == 0:
        print("====> No files found for migration\n")

    # Add "hired_employees.csv" at the beginning of the list to create main table as needed
    if "hired_employees.csv" in files:
        files.remove("hired_employees.csv")
        files.insert(0, "hired_employees.csv")

    for file in files:
        file_path = os.path.join(csv_to_migrate, file)
        destiny_file_path = os.path.join(destiny_path, file)

        if file.split('.')[1] == 'csv':
            if file.split('.')[0] == 'hired_employees':
                df = pd.read_csv(file_path, names=[
                                 'id', 'name', 'datetime', 'department_id', 'job_id'])
                res = load_to_db(df, file.split('.')[0])
                if res == 0:
                    shutil.move(file_path, destiny_file_path)

            elif file.split('.')[0] == 'departments':
                df = pd.read_csv(file_path, names=['id', 'department'])
                res = load_to_db(df, file.split('.')[0])
                if res == 0:
                    shutil.move(file_path, destiny_file_path)

            elif file.split('.')[0] == 'jobs':
                df = pd.read_csv(file_path, names=['id', 'job'])
                res = load_to_db(df, file.split('.')[0])
                if res == 0:
                    shutil.move(file_path, destiny_file_path)

        else:
            # Send the output into the log file
            print(f"====> The following file is not a valid csv: {file}\n")
            continue

        # print(df.head())


if __name__ == '__main__':
    csv_to_migrate = os.path.join(WORKING_DIRECTORY, 'landing_zone')
    destiny_path = os.path.join(WORKING_DIRECTORY, 'processed')

    parse_csv_files_and_save(csv_to_migrate, destiny_path)
