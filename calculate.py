import courses_module as cm
import personal as p

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

calculation_options = [
    "Average Grade",
    "Number of Course Type"
]

cm.print_list(calculation_options)
type = int(input("WHat would you like to calculate?: "))

def calculate_avg():
    query =f"""
    SELECT 
        AVG(Grade)
    FROM
        course_info
    WHERE 
        Completion = "Completed" AND
        Grade IS NOT NULL
    """
    return query

def num_course_type():
    cm.print_list(cm.COMPLETION_TYPES)
    completion = int(input("What completion status would you like to calculate?: "))
    query = f"""
    SELECT
        COUNT(CourseCode)
    FROM 
        course_info
    WHERE 
        Completion = "{cm.COMPLETION_TYPES[completion - 1]}";
    """
    return query

table = []

def calculate():
    if type == 1:
        query = calculate_avg()
        cm.display_info(connection, query, ["Cumulative Average"], table)
    elif type == 2:
        query = num_course_type()
        cm.display_info(connection, query, ["Number of Courses"], table)
    else:
        return
    

calculate()
    