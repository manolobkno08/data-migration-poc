#!/usr/bin/env python3
# [Standard Library]
import os
from dataclasses import dataclass
from pathlib import Path

# [3rd Party]
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv('.env')


class DataBaseConnection:
    def __init__(self, host, port, database, user, password) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = self.create_connection()

    def create_connection(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def execute_query(self, query):
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                res = cursor.fetchall()
                cursor.close()
                return res


WORKING_DIRECTORY = Path(__file__).resolve().parent.parent

if __name__ == '__main__':
    csv_to_migrate = os.path.join(WORKING_DIRECTORY, 'landing_zone')

    test_db = DataBaseConnection(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )

    query = 'SELECT NOW()'
    res = test_db.execute_query(query)
    test_db.connection.close()
    print(res)

    # for file in os.listdir(csv_to_migrate):
    #     file_path = os.path.join(csv_to_migrate, file)

    #     if file.split('.')[1] == 'csv':
    #         if file.split('.')[0] == 'departments':
    #             df = pd.read_csv(file_path, names=['id', 'department'])
    #         elif file.split('.')[0] == 'jobs':
    #             df = pd.read_csv(file_path, names=['id', 'job'])
    #         elif file.split('.')[0] == 'hired_employees':
    #             df = pd.read_csv(file_path, names=[
    #                              'id', 'name', 'datetime', 'department_id', 'job_id'])
    #     else:
    #         # Send the output into the log file
    #         print(f"The following file is not a valid csv: {file}")
    #         continue

    #     print(df.head())
