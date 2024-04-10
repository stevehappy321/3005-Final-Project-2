import psycopg2

# Replace these variables with your actual database connection details
dbname = 'FinalProject'
user = 'postgres'
password = 'postgres'
host = 'localhost'

#Steve

def userExists(table, e):
    name = e.split(" ")
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        #Covers person with 1 name (error)
        if(len(name) == 1):
            name.append("Invalid")

        findPerson = f"SELECT * FROM {table} WHERE firstname = '{name[0]}' AND lastname = '{name[1]}'"
        print("Query: " + findPerson)

        cur.execute(findPerson)
        potential = cur.fetchone()
        print(potential)

        conn.close()
        return potential != None

#Ryan
#checks if a member exists in the database. Used to initialize
def memberExists(e):
    name = e.split(" ")
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        #Covers person with 1 name (error)
        if(len(name) == 1):
            name.append("Invalid")
        findStudent = "SELECT * FROM Members WHERE firstname = '{}' AND lastname = '{}';".format(name[0], name[1])
        cur.execute(findStudent)
        potential = cur.fetchone()

        if potential:
            conn.close()
            return True
        else:
            conn.close()
            return False

#gets all of something
def getAllSomething(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM {}".format(e))
        records = cur.fetchall()
        return records
    
#adds something
def addSomething(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("Insert INTO {}".format(e))
        conn.commit()

#deletes something
def deleteSomething(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("Delete From {}".format(e))
        conn.commit()

#updates something
def UpdateSomething(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("UPDATE {}".format(e))
        conn.commit()

#allows users to strictly select items if needed
def StrictSelect(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("{}".format(e))
        records = cur.fetchall()
        return records
    
#gets a members number based on their first and last name
def getMemberNumber(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("Select MemberID From Members Where FirstName = {}".format(e))
        records = cur.fetchall()
        return records

#this function gives all power to the calling query.
#fairly specific query needed so we leave it to the user
#counts the number of people in a class to check for capacity though
def getNumberOfMembers(e, classID):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("{}".format(e))
        records = cur.fetchall()
        found = False
        classID = int(classID)
        for a_tuple in records:
            if a_tuple[0] == classID:
                if a_tuple[1] > a_tuple[2]:
                    found = True
                    break

        if not found:
            return False
        return True

def getAllConditional(table, condition = None):
    return (
        getAllSomething(table) if (condition == None) 
        else StrictSelect(
            f"""
            SELECT * FROM {table}
            WHERE {condition}
            """
            )
    )