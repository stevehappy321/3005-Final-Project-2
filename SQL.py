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
   
def getAllSomething(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM {}".format(e))
        records = cur.fetchall()
        return records
    
def addSomething(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("Insert INTO {}".format(e))
        conn.commit()

def deleteSomething(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("Delete From {}".format(e))
        conn.commit()

def UpdateSomething(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("UPDATE {}".format(e))
        conn.commit()

def StrictSelect(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("{}".format(e))
        records = cur.fetchall()
        return records

def getMemberNumber(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("Select MemberID From Members Where FirstName = {}".format(e))
        records = cur.fetchall()
        return records
    
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
