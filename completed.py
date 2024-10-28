import courses_module as cm
import personal as p

# This program will allow you to change a course to "completed" status and add the term it was completed
#   in and the grade achieved

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

course_code = input("What is the course code of the completed course?: ")
term = input("Which term was this course completed in?: ")
grade = input("What is the grade achieved for this course?: ")

completion_query = """
UPDATE
    {}
SET 
    Completion = "Completed"
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
    Grade = {}
WHERE
    CourseCode = "{}";
""".format(cm.COURSE_TABLE, grade, course_code)

cm.execute_query(connection, completion_query)
cm.execute_query(connection, term_query)
cm.execute_query(connection, grade_query)
