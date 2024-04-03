import psycopg2

# Replace these variables with your actual database connection details
dbname = 'FinalProject'
user = 'postgres'
password = 'postgres'
host = 'localhost'

#Ryan

def personExists2(table, e):
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

def personExists(e):
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
