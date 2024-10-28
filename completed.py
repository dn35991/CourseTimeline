import courses_module as cm
import personal as p

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

course_code = input("What course has been completed (course code)?: ")
completion_query = """
UPDATE
    {}
SET 
    Completion = "Completed"
WHERE
    CourseCode = "{}";
""".format(cm.COURSE_TABLE, course_code)