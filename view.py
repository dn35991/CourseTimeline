import courses_module as cm
import personal as p
from IPython.display import display

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)
view_options = ["Course Type", "Completion Type", "Term", "Course Code", "Grade", "Prerequisite Courses"]
cm.print_list(view_options)
view = int(input("What would you like to view?: "))
option = 0

def course_query1(column):
    if column == 1 or column == 2:
        column_name = cm.COURSE_COLUMNS[column + 2]
        cm.print_list(cm.dict_value(cm.COURSE_DICT, column + 2))
        item = int(input(f"What {view_options[column - 1].lower()} would you like to view?: "))
        query = f"""
        SELECT *
        FROM
            {cm.COURSE_TABLE} AS C
        WHERE 
            {column_name} = "{(cm.dict_value(cm.COURSE_DICT, column + 2))[item - 1]}"
        ORDER BY
            {cm.ORDERING}
        """
    elif column == 3:
        column_name = cm.COURSE_COLUMNS[column + 2]
        item = input(f"Which {view_options[column - 1].lower()} would you like to view?: ")
        query = f"""
        SELECT *
        FROM
            {cm.COURSE_TABLE} AS C
        WHERE 
            {column_name} = "{item}"
        ORDER BY
            {cm.ORDERING}
        """
    elif column == 4:
        return

    return query

table = []

def views():
    if 1 <= view <= 5:
        query = course_query1(view)
    else:
        return
    cm.display_info(connection, query, cm.COURSE_COLUMNS, table)

views()