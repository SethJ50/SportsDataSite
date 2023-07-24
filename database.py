import sqlalchemy
from sqlalchemy import create_engine, text
import os
import mysql.connector

""" db_connection_string = str(os.environ.get('DB_CONNECTION_STRING'))

engine = create_engine(db_connection_string)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
    return jobs """

pwd = str(os.environ.get('mySQLConnectPwd'))

connection = mysql.connector.connect(user='root', database='sportsdatadb', password=pwd, host='localhost')


def load_jobs_from_db():
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM jobs")
        jobs = []
        for row in cursor:
            jobs.append(row)
    return jobs
