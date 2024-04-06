import SQL
import datetime

import TrainerBackend
import Utility

def getAvailableTrainers(date, startTime, endTime):
    #get all trainers
    #remove trainers that are occupied during the specified timeframe

    allTrainersID = SQL.StrictSelect("SELECT Trainers.trainerID, Trainers.firstName, Trainers.lastName FROM Trainers") #list of tuples
    availableTrainers = []

    for trainer in allTrainersID:
        trainerID = trainer[0]
        if TrainerBackend.trainerIsAvailable(trainerID, date, startTime, endTime):
            availableTrainers.append(trainer)

    return availableTrainers