import courses_module as cm
import personal as p

server_connection = cm.server_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD)

database_query = """
CREATE DATABASE {};
""".format(cm.DATABASE)

course_table_query = """
CREATE TABLE {} (
    CourseCode VARCHAR(30) NOT NULL,
    CourseName VARCHAR(10000),
    Credits DECIMAL(10,2),
    CourseType VARCHAR(20),
    Completion VARCHAR(20),
    Term VARCHAR(5),
    Grade INT,
    PRIMARY KEY (CourseCode)
);
""".format(cm.COURSE_TABLE)

prereq_table_query = """
CREATE TABLE {} (
    CourseCode VARCHAR(30) NOT NULL,
    PrereqCode VARCHAR(30),
    EqPrereq VARCHAR(15),
    MinGrade INT,
    PRIMARY KEY (CourseCode)
);
""".format(cm.PREREQ_TABLE)

cm.execute_query(server_connection, database_query)

database_connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

cm.execute_query(database_connection, course_table_query)
cm.execute_query(database_connection, prereq_table_query)