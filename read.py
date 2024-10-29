import courses_module as cm
import personal as p
import pandas as pd

# This program will allow you to view a specifc table with every single column and row

connection = cm.database_connection(p.HOST_NAME,p.USERNAME, p.PASSWORD, cm.DATABASE)

table_name = int(input("Which table would you like to view (1. {} | 2. {})?: ".format(cm.COURSE_TABLE, cm.PREREQ_TABLE)))

table = []

def read_table():
    if table_name == 1:
        cm.display_info(connection, cm.course_info_table_query, cm.COURSE_INFO_COLUMNS, table)
    elif table_name == 2:
        cm.display_info(connection, cm.prereq_info_table_query, cm.PREREQ_INFO_COLUMNS, table)
    else:
        return
    return

read_table()