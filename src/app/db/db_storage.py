# [Standard Library]
from dataclasses import dataclass

# [3rd Party]
import pandas as pd
import psycopg2
import psycopg2.extras as extras


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

    def historical_data_ingestion(self, df, table):
        tuples = [tuple(x) for x in df.to_numpy()]
        cols = ','.join(list(df.columns))

        query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
        cursor = self.connection.cursor()

        try:
            extras.execute_values(cursor, query, tuples)
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.connection.rollback()
            cursor.close()
            return 1

        print(f"execute_values() for {table} ran successfully")
        cursor.close()
