import courses_module as cm
import personal as p

# This program will allow you to delete a single entry from either tables in the database

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

table = int(input("Which table would you like to access (1. {} | 2. {})?: ".format(cm.COURSE_TABLE, cm.PREREQ_TABLE)))
course_code = input("What is the course code of the entry?: ")

delete_course_query = """
DELETE FROM {}
WHERE
    CourseCode = "{}";
""".format(cm.COURSE_TABLE, course_code)

def delete_entry():
    if table == 1:
        cm.execute_query(connection, delete_course_query)
    elif table == 2:
        prereq_code = input("What is the corresponding prerequisite code for this entry?: ")
        delete_prereq_query = """
        DELETE FROM {}
        WHERE
            CourseCode = "{}" AND PrereqCode = "{}";
        """.format(cm.PREREQ_TABLE, course_code, prereq_code)

        cm.execute_query(connection, delete_prereq_query)
    else:
        return
    return

delete_entry()
