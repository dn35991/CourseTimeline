import courses_module as cm
import personal as p

# This program will allow you to add the prerequisites of one course into the prerequisite information table.
#   Continute writing each prerequisite until you do not need anymore. When no more prerequisites are required,
#   leave the questions blank and the program will end (press enter on both questions).
 
connection = cm.database_connection(p.HOST_NAME, p.USERNAME, p.PASSWORD, cm.DATABASE)

course_code = input("What is the course code? ")
pcode = ""
minimum = 0

def add_prereqs():
    n = 0
    while True:
        pcode = input("What is the prerequisite course code?: ")
        minimum = input("What is the minimum grade required?: ")

        if pcode == "":
            print("{} Prerequistes Added for {}".format(n, course_code))
            return
        elif minimum == "":
            add_prereq_query = """
            INSERT INTO
                {}
            VALUES
                ("{}", "{}", NULL);
            """.format(cm.PREREQ_TABLE, course_code, pcode)

            cm.execute_query(connection, add_prereq_query)
            n = n + 1 
        else:
            add_prereq_query = """
            INSERT INTO
                {}
            VALUES
                ("{}", "{}", {});
            """.format(cm.PREREQ_TABLE, course_code, pcode, minimum)

            cm.execute_query(connection, add_prereq_query)
            n = n + 1 

    print("{} Prerequistes Added for {}".format(n, course_code))

add_prereqs()

