import courses_module as cm
import personal as p

# This program will allow you to add a single course and all of its information into the course information table.
#   Be sure to write each input as specificied in the question prompts.
 
connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

course_code = input("What is the course code (ABCD 000)?: ")
course_name = input("What is the name of the course?: ")
credits = input("How many credits is the course worth?: ")
course_type = input("What type of course is it (Math, Non-Math, PD)?: ")
completion = input("Is the course Available/Current/Planned/Prereq/Completed?: ")
term = input("What term is/will the course be completed? ")
grade = input("What grade has been acheived for the course?: ")

add_query1 = """
INSERT INTO
    {}
VALUES
    ("{}", "{}", {}, "{}", "{}", "{}", {});
""".format(cm.COURSE_TABLE, course_code, course_name, credits, course_type, completion, term, grade)

add_query2 = """
INSERT INTO
    {}
VALUES
    ("{}", "{}", {}, "{}", "{}", NULL, NULL);
""".format(cm.COURSE_TABLE, course_code, course_name, credits, course_type, completion, grade)

add_query3 = """
INSERT INTO
    {}
VALUES
    ("{}", "{}", {}, "{}", "{}", "{}", NULL);
""".format(cm.COURSE_TABLE, course_code, course_name, credits, course_type, completion, term)

def add_course():
    if completion == "Available" or completion == "Prereq":
        cm.execute_query(connection, add_query2)
        print("{} Course Added".format(completion))
    elif completion == "Planned":
        cm.execute_query(connection, add_query3)
        print("{} Course Added".format(completion))
    else:
        cm.execute_query(connection, add_query1)
        print("{} Course Added".format(completion))
    return

add_course()
