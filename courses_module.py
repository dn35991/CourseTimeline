import mysql.connector
from mysql.connector import Error
import pandas as pd
from IPython.display import display

# This is the module used in all of the programs for this project. The global constants "DATABSE", "COURSE_TABLE", 
#   and "PREREQ_TABLE" can be changed, but is not recommended. Before begining to run any programs, make sure
#   to edit the file "personal.py" where you must enter the values for "HOST_NAME", "USERNAME", and "PASSWORD"

DATABASE = "courses"
COURSE_TABLE = "course_info"
PREREQ_TABLE = "prerequisite_courses"
COURSE_INFO_COLUMNS = ["CourseCode", "CourseName", "Credits", "CourseType", "Completion", "Term", "Grade"]
PREREQ_INFO_COLUMNS = ["CourseCode", "PrereqCode", "MinGrade"]

term_order = """
(CASE WHEN Term = NULL THEN 1
          ELSE 2
    END)
"""
completion_order = """
(CASE WHEN C.Completion = "Completed" THEN 1
          WHEN C.Completion = "Current" THEN 2
          WHEN C.Completion = "Planned" THEN 3
          WHEN C.Completion = "Available" THEN 4
          WHEN C.Completion = "Prereq" THEN 5
          ELSE 6
    END)
"""

course_type_order = """
(CASE WHEN C.CourseType = "Non-Math" THEN 1
		  WHEN C.CourseType = "PD" THEN 2
          WHEN C.CourseType = "Math" THEN 3
          ELSE 4
	END)
"""

course_info_table_query = """
SELECT *
FROM 
    {} AS C
ORDER BY 
    {} DESC,
    {} ASC,
	Term ASC,
    Credits ASC,
    {} ASC,
    Credits ASC,
    CourseType ASC;
""".format(COURSE_TABLE, term_order, completion_order, course_type_order)

prereq_info_table_query = """
SELECT 
	PC.CourseCode AS CourseCode,
    PC.PrereqCode AS PrereqCode,
    PC.MinGrade AS MinGrade
FROM 
	{} as PC
INNER JOIN
	{} as C
ON
	C.CourseCode = PC.CourseCode
ORDER BY 
    {} DESC,
    {} DESC,
	C.Term ASC,
    C.Credits ASC,
    {} ASC;
""".format(PREREQ_TABLE, COURSE_TABLE, term_order, completion_order, course_type_order)

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

def display_info(connection, info_query, column_names, table):
    results = read_query(connection, info_query)
    for data in results:
        data = list(data)
        table.append(data)
    return display(pd.DataFrame(table, columns = column_names))
