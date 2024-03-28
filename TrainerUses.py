import SQL

def setAvailability(trainerID):
    unavailableTimes = SQL.StrictSelect( #this returns a list of dates and times where this trainer is busy
        f"""
        SELECT classDate AS date, sessionTime AS time FROM FitnessClass
        WHERE trainerID = {trainerID}

        UNION

        SELECT sessionDate AS date, sessionTime AS time FROM PrivateSession
        WHERE trainerID = {trainerID}
        """
    )

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