import SQL
import Utility

def setTrainerHours(trainerID, startTime, endTime):
    SQL.UpdateSomething(
        f"""
            TRAINERS
            SET startTime = {startTime}, endTime = {endTime}
            WHERE trainerID = {trainerID}
        """)

def setTrainerStartTime(trainerID, time):
    SQL.UpdateSomething(
        f"""
            TRAINERS
            SET startTime = '{time}'
            WHERE trainerID = {trainerID}
        """)
    
def setTrainerEndTime(trainerID, time):
    SQL.UpdateSomething(
        f"""
            TRAINERS
            SET endTime = '{time}'
            WHERE trainerID = {trainerID}
        """)

def getTrainerHours(trainerID):
    trainerHours = SQL.StrictSelect( #trainer's working hours
        f"""
        SELECT StartTime, EndTime FROM Trainers
        WHERE trainerID = {trainerID}
        """)[0] #get the only tuple in the list

    return Utility.tupleToDict( trainerHours, ["startTime", "endTime"] )

def trainerIsAvailable(trainerID, date, startTime, endTime):
    trainerFreeIntervals = getTrainerAvailableInvervals(date, trainerID)

    for interval in trainerFreeIntervals: #interval is a tuple (startTime, endTime)
        if (
            Utility.inRange(interval[0], startTime, interval[1], True) and 
            Utility.inRange(interval[0], endTime, interval[1], True)
        ):
            return True
        
    return False

def getTrainerAvailableInvervals(date, trainerID):
    def computeFreeIntervals(startTime, endTime, busyIntervals):
        freeIntervals = []

        if len(busyIntervals) == 0:
            freeIntervals.append( (startTime, endTime) )
        
        else:
            for i in range(0, len(busyIntervals) ):
                if i == 0:
                    freeIntervals.append( (startTime, busyIntervals[i]["startTime"]) )
                else:
                    freeIntervals.append( (busyIntervals[i-1]["endTime"], busyIntervals[i]["startTime"]) )

            if busyIntervals[-1]["endTime"] != endTime:
                freeIntervals.append( (busyIntervals[-1]["endTime"], endTime) )

        return freeIntervals;


    startTime = getTrainerHours(trainerID)["startTime"]
    endTime = getTrainerHours(trainerID)["endTime"]

    busyIntervals = SQL.StrictSelect( #list of tuples where this trainer is busy
        f"""
        SELECT sessionTime AS startTime, endTime FROM FitnessClass
        WHERE trainerID = {trainerID} AND classDate = '{date}'
        UNION
        SELECT sessionTime AS startTime, endTime FROM PrivateSession
        WHERE trainerID = {trainerID} AND sessionDate = '{date}'
        """)
    
    for i in range (0, len(busyIntervals) ):
        busyIntervals[i] = Utility.tupleToDict(busyIntervals[i], ["startTime", "endTime"])

    return computeFreeIntervals(startTime, endTime, busyIntervals); #returns a list of tuple intervals that this trainer is free to teach


def searchMemberByName(name):
    givenNamesList = name.split(' '); #split name by space
    members = []

    if len(givenNamesList) == 1:
         members = SQL.StrictSelect(
            f"""
            SELECT * FROM Members WHERE 
            FirstName LIKE '{name}' OR 
            LastName LIKE '{name}'
            """)

    elif len(givenNamesList) > 1:
        firstName = givenNamesList[0]
        lastName = givenNamesList[-1]

        members = SQL.StrictSelect(
            f"""
            SELECT * FROM Members WHERE 
            FirstName LIKE '{firstName}' OR 
            LastName LIKE '{lastName}'
            """)

    return members;