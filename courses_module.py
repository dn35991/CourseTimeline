import mysql.connector
from mysql.connector import Error
import pandas as pd

# Define HOST_NAME, USERNAME, and PASSWORD in personal.py

DATABASE = "courses"
COURSE_TABLE = "course_info"
PREREQ_TABLE = "prereq_courses"
COURSE_INFO_COLUMNS = ["CourseCode", "CourseName", "Credits", "CourseType", "Completion", "Term", "Grade"]
PREREQ_INFO_COLUMNS = ["CourseCode", "PrereqCode", "EqPrereq", "MinGrade"]

def server_connection(host_name, username, password):
    connection = None
    try: 
        connection = mysql.connector.connect(
            host = host_name,
            user = username,
            passwd = password
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def database_connection(host_name, username, password, database_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = username,
            passwd = password,
            database = database_name,
            autocommit = True
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit
        print("Query Successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
