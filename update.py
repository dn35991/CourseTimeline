import courses_module as cm
import personal as p

# This program will allow you to update a single entry for a specific course code in either table. Make sure 
#   your input matches exactly to the entries or columns in the database

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)
table = int(input("Which table is being updated (1 for \"{}\" | 2 for \"{}\")?: "))
course_code = input("What is the course code of the entry?: ")
prereq_code = input("What is the prerequisite code for the entry?: ")
set1 = input("What column is being updated?: ")
set2 = input("What is the column being updated to?: ")

update_course_query1 = """
UPDATE 
    {}
SET {} = "{}"
WHERE CourseCode = "{}";
""".format(cm.COURSE_TABLE, set1, set2, course_code)

update_course_query2 = """
UPDATE 
    {}
SET {} = {}
WHERE CourseCode = "{}";
""".format(cm.COURSE_TABLE, set1, set2, course_code)

update_prereq_query1 = """
UPDATE 
    {}
SET {} = "{}"
WHERE CourseCode = "{}" AND PrereqCode = "{}";
""".format(cm.PREREQ_TABLE, set1, set2, course_code, prereq_code)

update_prereq_query2 = """
UPDATE 
    {}
SET {} = {}
WHERE CourseCode = "{}" AND PrereqCode = "{}";
""".format(cm.PREREQ_TABLE, set1, set2, course_code, prereq_code)

def update_table():
    if table == 1:
        if (set1 == "Grade" or set1 == "Credits"):
            cm.execute_query(connection, update_course_query2)
        else:
            cm.execute_query(connection, update_course_query1)
    elif table == 2:
        if (set1 == "MinGrade"):
            cm.execute_query(connection, update_prereq_query2)
        else:
            cm.execute_query(connection, update_prereq_query1)
    else:
        return
    return

update_table()