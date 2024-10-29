import courses_module as cm
import personal as p

# This program will allow you to add a single course and all of its information into the course information table.
#   Be sure to write each input as specificied in the question prompts.
 
connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

course_code = input("What is the course code (ABCD 000)?: ")
course_name = input("What is the name of the course?: ")
credits = input("How many credits is the course worth?: ")
cm.print_list(cm.COURSE_TYPE)
course_type = int(input("What type of course is it?: "))
cm.print_list(cm.COMPLETION_TYPES)
completion = int(input("What is the completion status of the course?: "))
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

def add_query(course_code, course_name, credits, course_type, completion, term, grade):
    query = f"""
    INSERT INTO
        {cm.COURSE_TABLE}
    VALUES
        ("{course_code}", "{course_name}", {credits}, "{cm.COURSE_TYPE[course_type - 1]}", "{cm.COMPLETION_TYPES[completion - 1]}", {term}, {grade})
    """
    cm.execute_query(connection, query)
    return

def add_course():
    if completion == 4 or completion == 5:
        add_query(course_code, course_name, credits, course_type, completion, "NULL", "NULL")
        print(f"{cm.COMPLETION_TYPES[completion - 1]} Course Added")
    elif completion == 3 or completion == 2:
        add_query(course_code, course_name, credits, course_type, completion, f"\"{term}\"", "NULL")
        print(f"{cm.COMPLETION_TYPES[completion - 1]} Course Added")
    elif completion == 1:
        add_query(completion, course_name, credits, course_type, completion, f"\"{term}\"", grade)
        print(f"{cm.COMPLETION_TYPES[completion - 1]} Course Added")
    else:
        print("No course was added")
        return
    
add_course()