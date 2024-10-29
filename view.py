import courses_module as cm
import personal as p
from IPython.display import display

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

option = 0

view_options = """
1. Completion Type
2. Course Type
. Prerequisites of Courses That Require Prerequisites
"""

completion_options = """
1. Completed Courses
2. Current Courses
3. Planned Courses
4. Available Courses
5. Prequisite Requires Courses
"""

course_type_options = """
1. Math Courses
2. Non-Math Courses
3. PD Courses
"""

def query1(type1, type2):
    query = """
    SELECT *
    FROM
        {} AS C
    WHERE 
        {} = "{}"
    ORDER BY
    {} DESC,
    {} ASC,
	Term ASC,
    Credits ASC,
    {} ASC,
    Credits ASC,
    CourseType ASC;
    """.format(cm.COURSE_TABLE, type1, type2, cm.term_order, cm.completion_order, cm.course_type_order)

    return query

print("{}".format(view_options))

v = int(input("What would you like to view?: "))

def completion():
    print("{}".format(completion_options))
    n = int(input("Which completion status would you like to view?: "))
    if n == 1:
        option = "Completed"
    elif n == 2:
        option = "Current"
    elif n == 3:
        option = "Planned"
    elif n == 4:
        option = "Available"
    elif n == 5:
        option = "Prereq"
    else:
        return
    
    query = query1("Completion", option)

    return query

def course_type():
    print("{}".format(course_type_options))
    n = int(input("Which type of course would you like to view?: "))
    if n == 1:
        option = "Math"
    elif n == 2:
        option = "Non-Math"
    elif n == 3:
        option = "PD"
    else:
        return
    
    query = query1("CourseType", option)

    return query

table = []

def views():
    if v == 1:
        cm.display_info(connection, completion(), cm.COURSE_INFO_COLUMNS, table)
    elif v == 2:
        cm.display_info(connection, course_type(), cm.COURSE_INFO_COLUMNS, table)
    else:
        return
    return

views()