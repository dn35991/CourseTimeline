import courses_module as cm
import personal as p

# This program will allow you to delete a course from the database entirely (both tables)

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

course_code = input("Which course code would you like to delete?: ")

delete_course_query = f"""
DELETE FROM {cm.COURSE_TABLE}
WHERE
    CourseCode = "{course_code}";
"""

delete_prereq_query = f"""
DELETE FROM {cm.PREREQ_TABLE}
WHERE
    CourseCode = "{course_code}";
"""

cm.execute_query(connection, delete_course_query)
cm.execute_query(connection, delete_prereq_query)