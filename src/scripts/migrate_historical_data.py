#!/usr/bin/env python3

# [Standard Library]
import os
from pathlib import Path

# [3rd Party]
import pandas as pd

WORKING_DIRECTORY = Path(__file__).resolve().parent.parent

if __name__ == '__main__':
    csv_to_migrate = os.path.join(WORKING_DIRECTORY, 'landing_zone')

    for file in os.listdir(csv_to_migrate):
        file_path = os.path.join(csv_to_migrate, file)

        if file.split('.')[1] == 'csv':
            if file.split('.')[0] == 'departments':
                df = pd.read_csv(file_path, names=['id', 'department'])
            elif file.split('.')[0] == 'jobs':
                df = pd.read_csv(file_path, names=['id', 'job'])
            elif file.split('.')[0] == 'hired_employees':
                df = pd.read_csv(file_path, names=[
                                 'id', 'name', 'datetime', 'department_id', 'job_id'])
        else:
            # Send the output into the log file
            print(f"The following file is not a valid csv: {file}")
            continue

        print(df.head())
