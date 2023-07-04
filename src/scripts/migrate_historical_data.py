#!/usr/bin/env python3
# [Standard Library]
import os
import sys
from pathlib import Path

# [3rd Party]
import pandas as pd
import numpy as np
from dotenv import load_dotenv

# Add the parent directory to the path so we can import the app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.db import DataBaseConnection


WORKING_DIRECTORY = Path(__file__).resolve().parent.parent

dotenv_path = os.path.join(WORKING_DIRECTORY, '.env')
load_dotenv(dotenv_path)


def parse_csv_files_and_save(csv_to_migrate):

    conn = DataBaseConnection(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )

    for file in os.listdir(csv_to_migrate):
        file_path = os.path.join(csv_to_migrate, file)

        if file.split('.')[1] == 'csv':

            if file.split('.')[0] == 'hired_employees':
                df = pd.read_csv(file_path, names=[
                                 'id', 'name', 'datetime', 'department_id', 'job_id'])
                print(df)
                print(df.dtypes)

                print("\n")

                #df = df.astype({"department_id":'Int64', "job_id":'Int64'})
                # columns_to_convert = ['department_id', 'job_id']
                # for col in columns_to_convert:
                #     df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
                # df = df.replace(np.NAType(), float('nan'))

                for col in df.columns:
                    if df[col].dtype == np.float64:
                        df[col] = df[col].astype('int')

                print(df)
                print(df.dtypes)

                #conn.historical_data_ingestion(df, file.split('.')[0])

            # if file.split('.')[0] == 'departments':
            #     df = pd.read_csv(file_path, names=['id', 'department'])
            #     conn.historical_data_ingestion(df, file.split('.')[0])

            # elif file.split('.')[0] == 'jobs':
            #     df = pd.read_csv(file_path, names=['id', 'job'])
            #     conn.historical_data_ingestion(df, file.split('.')[0])

            # elif file.split('.')[0] == 'hired_employees':
            #     df = pd.read_csv(file_path, names=[
            #                      'id', 'name', 'datetime', 'department_id', 'job_id'])
            #     conn.historical_data_ingestion(df, file.split('.')[0])
        else:
            # Send the output into the log file
            print(f"The following file is not a valid csv: {file}")
            continue

        #print(df.head())


if __name__ == '__main__':
    csv_to_migrate = os.path.join(WORKING_DIRECTORY, 'landing_zone')
    parse_csv_files_and_save(csv_to_migrate)
