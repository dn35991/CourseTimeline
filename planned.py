import courses_module as cm
import personal as p

# This program will allow you to change a course to "planned" status and add the term that 
#   the course is planned to be taken in

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

course_code = input("What is the course code of the planned course?: ")
term = input("What term is this course being planned?: ")

completion_query = """
UPDATE
    {}
SET 
    Completion = "Planned"
WHERE
    CourseCode = "{}";
""".format(cm.COURSE_TABLE, course_code)

term_query = """
UPDATE
    {}
SET 
    term = "{}"
WHERE
    CourseCode = "{}";
""".format(cm.COURSE_TABLE, term, course_code)

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
