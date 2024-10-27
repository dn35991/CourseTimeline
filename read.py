import courses_module as cm
import personal as p
import pandas as pd
from IPython.display import display

connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

course_info_table_query = """
SELECT *
FROM 
    {}
ORDER BY
    Term ASC,
    Credits ASC,
    CourseType ASC;
""".format(cm.COURSE_TABLE)

results = cm.read_query(connection, course_info_table_query)

table = []

for data in results:
    data = list(data)
    table.append(data)

display(pd.DataFrame(table, columns = cm.COURSE_INFO_COLUMNS))