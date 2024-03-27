"""
def getAllSomething(e):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM {}".format(e))
        records = cur.fetchall()
        return records
"""
import SQL

def setAvailability():
    #get all the classes and private sessions that the trainer leads
    #trainer is available during other times
    trainerClasses = SQL.getAllSomething(
        ""
    )


def searchMemberByName(name):
    givenNamesList = name.split(' '); #split name by space
    members = []

    if len(givenNamesList) == 1:
         members = SQL.StrictSelect(
            "SELECT * FROM Members WHERE "
            "FirstName LIKE {name} OR "
            "LastName LIKE {name}"
        )

    elif len(givenNamesList) > 1:
        firstName = givenNamesList[0]
        lastName = givenNamesList[len(givenNamesList) - 1]

        members = SQL.StrictSelect(
            "SELECT * FROM Members WHERE "
            "FirstName LIKE {firstName} OR "
            "LastName LIKE {lastName}"
        )

    return members;