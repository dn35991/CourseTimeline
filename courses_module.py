import mysql.connector
from mysql.connector import Error
import pandas as pd

# This is the module used in all of the programs for this project. The global constants "DATABSE", "COURSE_TABLE", 
#   and "PREREQ_TABLE" can be changed, but is not recommended. Before begining to run any programs, make sure
#   to edit the file "personal.py" where you must enter the values for "HOST_NAME", "USERNAME", and "PASSWORD"

DATABASE = "courses"
COURSE_TABLE = "course_info"
PREREQ_TABLE = "prerequisite_courses"
COURSE_INFO_COLUMNS = ["CourseCode", "CourseName", "Credits", "CourseType", "Completion", "Term", "Grade"]
PREREQ_INFO_COLUMNS = ["CourseCode", "PrereqCode", "MinGrade"]

course_info_table_query = """
SELECT *
FROM 
    {}
ORDER BY 
    (CASE WHEN Term = NULL THEN 1
          ELSE 2
    END) DESC,
    (CASE WHEN Completion = "Completed" THEN 1
          WHEN Completion = "Current" THEN 2
          WHEN Completion = "Planned" THEN 3
          WHEN Completion = "Available" THEN 4
          WHEN Completion = "Prereq" THEN 5
          ELSE 6
    END) ASC,
	Term ASC,
    Credits ASC,
    (CASE WHEN CourseType = "Non-Math" THEN 1
		  WHEN CourseType = "PD" THEN 2
          WHEN CourseType = "Math" THEN 3
          ELSE 4
	END) ASC;),
    Credits ASC,
    CourseType ASC;
""".format(COURSE_TABLE)

prereq_info_table_query = """
SELECT *
FROM 
    {}
ORDER BY
    CourseCode ASC;
""".format(PREREQ_TABLE)

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

def create_dataframe(connection, info_query, column_names, table):
    results = read_query(connection, info_query)
    for data in results:
        data = list(data)
        table.append(data)
    return pd.DataFrame(table, columns = column_names)
