import SQL

def getTrainerAvailability(trainerID):
    trainerHours = SQL.StrictSelect( #trainer's working hours
        f"""
        SELECT StartTime, EndTime FROM Trainers
        WHERE trainerID = {trainerID}
        """
    )[0]
    print(trainerHours)

    startTime = trainerHours[0]
    endTime = trainerHours[1]

    unavailableTimes = SQL.StrictSelect( #list of date-time pairs where this trainer is busy
        f"""
        SELECT classDate AS date, sessionTime AS time FROM FitnessClass
        WHERE trainerID = {trainerID}

        UNION

        SELECT sessionDate AS date, sessionTime AS time FROM PrivateSession
        WHERE trainerID = {trainerID}
        """
    )
    print( computeAvailability(startTime, endTime, unavailableTimes) );


def computeAvailability(startTime, endTime, busyIntervals):
    freeIntervals = []

    for i in range( 0, len(busyIntervals) ):
        if i == 0:
            freeIntervals.append( {startTime, busyIntervals[i][0]} )
        else:
            freeIntervals.append( {busyIntervals[i-1][1], busyIntervals[i][0]} )
    
    if busyIntervals[len(busyIntervals)-1][1] != endTime:
        freeIntervals.append( {busyIntervals[len(busyIntervals)-1][1], endTime} )

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
            """
            
        )

    elif len(givenNamesList) > 1:
        firstName = givenNamesList[0]
        lastName = givenNamesList[len(givenNamesList) - 1]

        members = SQL.StrictSelect(
            f"""
            SELECT * FROM Members WHERE 
            FirstName LIKE {firstName} OR 
            LastName LIKE {lastName}
            """
        )

    return members;