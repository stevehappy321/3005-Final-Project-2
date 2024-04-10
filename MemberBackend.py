import SQL
import datetime

import TrainerBackend
import Utility

#####################################
### Whole File created by steven ####
#####################################


def getAvailableTrainers(date, startTime, endTime):
    #get all trainers
    #remove trainers that are occupied during the specified timeframe

    allTrainers = SQL.StrictSelect("SELECT Trainers.trainerID, Trainers.firstName, Trainers.lastName FROM Trainers") #list of tuples
    availableTrainers = []

    for trainer in allTrainers:
        trainerID = trainer[0]
        if TrainerBackend.trainerIsAvailable(trainerID, date, startTime, endTime):
            availableTrainers.append(trainer)

    return availableTrainers; #list of tuples

"""
def getAvailableTrainers_v2(date, startTime, endTime):
    #same as getAvailableTrainers, but returns a list of dictionaries instead of a list of tuples

    allTrainers = SQL.StrictSelect("SELECT Trainers.trainerID, Trainers.firstName, Trainers.lastName FROM Trainers") #list of tuples

    for e in allTrainers: #convert list of tuples to list of struct-type dictionaries
        e = Utility.tupleToDict(tuple, ["trainerID, firstName, lastName"])
        
    availableTrainers = []

    for trainer in allTrainers:
        if TrainerBackend.trainerIsAvailable(trainer["trainerID"], date, startTime, endTime):
            availableTrainers.append(trainer)

    return availableTrainers; #list of "structs"
"""