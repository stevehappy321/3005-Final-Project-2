import psycopg2

# Replace these variables with your actual database connection details
dbname = 'FinalProject'
user = 'postgres'
password = 'postgres'
host = 'localhost'


def personExists(e):
    # The name you are searching for
    name = e.split(" ")
    # Connect to your postgres DB
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # This is the SQL query you will use
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

