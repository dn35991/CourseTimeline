import courses_module as cm
import personal as p
import queries as q
import pandas as pd

# This program will allow you to view a specifc table with every single column and row

connection = cm.database_connection(p.HOST_NAME,p.USERNAME, p.PASSWORD, cm.DATABASE)

course_info_table_query = f"""
SELECT *
FROM 
    {cm.COURSE_TABLE} AS C
ORDER BY 
    {q.ORDERING};
"""

prereq_info_table_query = f"""
SELECT 
	PC.CourseCode AS CourseCode,
    PC.PrereqCode AS PrereqCode,
    PC.MinGrade AS MinGrade
FROM 
	{cm.PREREQ_TABLE} as PC
INNER JOIN
	{cm.COURSE_TABLE} as C
ON
	C.CourseCode = PC.CourseCode
ORDER BY
    {q.ORDERING};
"""

table_name = int(input(f"Which table would you like to view (1. {cm.COURSE_TABLE} | 2. {cm.PREREQ_TABLE})?: "))

table = []

def read_table():
    if table_name == 1:
        cm.display_info(connection, course_info_table_query, cm.COURSE_COLUMNS, table)
    elif table_name == 2:
        cm.display_info(connection, prereq_info_table_query, cm.PREREQ_COLUMNS, table)
    else:
        return
    return

read_table()