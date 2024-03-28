import SQL
import Utility
import datetime

def setTrainerHours(startTime, endTime):
    x = x
    SQL.UpdateSomething()

def getTrainerAvailability(date, trainerID):
    trainerHours = SQL.StrictSelect( #trainer's working hours
        f"""
        SELECT StartTime, EndTime FROM Trainers
        WHERE trainerID = {trainerID}
        """)[0] #get the only tuple in the list

    startTime = trainerHours[0] #tuple index access - 0 = start time, 1 = end time
    endTime = trainerHours[1]

    unavailableTimesRecords = SQL.StrictSelect( #list of date-time pairs where this trainer is busy
        f"""
        SELECT classDate AS date, sessionTime AS startTime, endTime FROM FitnessClass
        WHERE trainerID = {trainerID} AND classDate = '{date}'
        UNION
        SELECT sessionDate AS date, sessionTime AS startTime, endTime FROM PrivateSession
        WHERE trainerID = {trainerID} AND sessionDate = '{date}'
        """)

    unavailableTimes = []
    for tuple in unavailableTimesRecords:
        unavailableTimes.append( Utility.tupleToDict(tuple, ["date", "startTime", "endTime"]) )

    print( computeAvailability(startTime, endTime, unavailableTimes) );


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