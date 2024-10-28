import courses_module as cm
import personal as p

# This program will allow you to change a course to "available" status

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

course_code = input("What is the course code of the available course?: ")

completion_query = """
UPDATE
    {}
SET 
    Completion = "Available"
WHERE
    CourseCode = "{}";
""".format(cm.COURSE_TABLE, course_code)

term_query = """
UPDATE
    {}
SET 
    term = NULL
WHERE
    CourseCode = "{}";
""".format(cm.COURSE_TABLE, course_code)

grade_query = """
UPDATE
    {}
SET 
    Grade = NULL
WHERE
    CourseCode = "{}";
""".format(cm.COURSE_TABLE, course_code)

cm.execute_query(connection, completion_query)
cm.execute_query(connection, term_query)
cm.execute_query(connection, grade_query)
