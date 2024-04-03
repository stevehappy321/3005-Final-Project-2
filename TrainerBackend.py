import SQL
import Utility

def setTrainerHours(trainerID, startTime, endTime):
    SQL.UpdateSomething(
        f"""
            TRAINERS
            SET startTime = {startTime}, endTime = {endTime}
            WHERE trainerID = {trainerID}
        """)

def setTrainerStartHours(trainerID, time):
    SQL.UpdateSomething(
        f"""
            TRAINERS
            SET startTime = {time}
            WHERE trainerID = {trainerID}
        """)
    
def setTrainerEndHours(trainerID, time):
    SQL.UpdateSomething(
        f"""
            TRAINERS
            SET endTime = {time}
            WHERE trainerID = {trainerID}
        """)

def getTrainerHours(trainerID):
    trainerHours = SQL.StrictSelect( #trainer's working hours
        f"""
        SELECT StartTime, EndTime FROM Trainers
        WHERE trainerID = {trainerID}
        """)[0] #get the only tuple in the list

    print(trainerHours)

    return Utility.tupleToDict( trainerHours, ["startTime", "endTime"] )

def getTrainerAvailability(date, trainerID):
    startTime = getTrainerHours(trainerID)["startTime"]
    endTime = getTrainerHours(trainerID)["endTime"]

    busyIntervalsRecords = SQL.StrictSelect( #list of date-time pairs where this trainer is busy
        f"""
        SELECT classDate AS date, sessionTime AS startTime, endTime FROM FitnessClass
        WHERE trainerID = {trainerID} AND classDate = '{date}'
        UNION
        SELECT sessionDate AS date, sessionTime AS startTime, endTime FROM PrivateSession
        WHERE trainerID = {trainerID} AND sessionDate = '{date}'
        """)

    busyIntervals = []
    for occupiedInterval in busyIntervalsRecords:
        busyIntervals.append( Utility.tupleToDict(occupiedInterval, ["date", "startTime", "endTime"]) )

    print( computeAvailability(startTime, endTime, busyIntervals) );


def computeAvailability(startTime, endTime, busyIntervals):
    freeIntervals = []

    print(busyIntervals)

    for i in range( 0, len(busyIntervals) ):
        if i == 0:
            freeIntervals.append( (startTime, busyIntervals[i]["startTime"]) )
        else:
            freeIntervals.append( (busyIntervals[i-1]["endTime"], busyIntervals[i]["startTime"]) )

        print(freeIntervals)
    
    if busyIntervals[len(busyIntervals)-1]["endTime"] != endTime:
        freeIntervals.append( (busyIntervals[len(busyIntervals)-1]["endTime"], endTime) )

    return freeIntervals;


def searchMemberByName(name):
    givenNamesList = name.split(' '); #split name by space
    members = []

    if len(givenNamesList) == 1:
         members = SQL.StrictSelect(
            f"""
            SELECT * FROM Members WHERE 
            FirstName LIKE {name} OR 
            LastName LIKE {name}
            """)

    elif len(givenNamesList) > 1:
        firstName = givenNamesList[0]
        lastName = givenNamesList[len(givenNamesList) - 1]

        members = SQL.StrictSelect(
            f"""
            SELECT * FROM Members WHERE 
            FirstName LIKE {firstName} OR 
            LastName LIKE {lastName}
            """)

    return members;