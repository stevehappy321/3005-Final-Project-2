import AdminGUI, MemberGUI
import InitializeGUI
import SQL

import TrainerGUI
import TrainerBackend
from  TrainerPages import TrainerMenu #alternative to TrainerGUI

import datetime

#Ryan

user_input_global = None
"""
def user_input_received(user_input):    
    global user_input_global
    user_input_global = user_input
    if(user_input_global == 'ADMIN'):
        InitializeGUI.broadcast(True, "Now logged in as: {}".format(user_input_global))
        InitializeGUI.close_gui()
        AdminGUI.AdminPortal()
    else:
        if(SQL.personExists2('Trainers', user_input_global) == True):
            allNames = user_input_global.split(' ')

            firstName = allNames[0]
            lastName = allNames[1] if len(allNames) >= 2 else ''
            print(firstName, lastName)

            trainerID = SQL.StrictSelect(
                "SELECT trainerID "
                "FROM Trainers "
                f"WHERE firstname = '{firstName}' AND lastname = '{lastName}'")[0][0]
            
            print('trainer id query = ')
            print(trainerID)
            
            #InitializeGUI.broadcast(True, "User Found! Now logged in as: {}".format(user_input_global))
            InitializeGUI.close_gui()
            #TrainerGUI.trainerPortal(trainerID);
            TrainerMenu.trainerPortal(trainerID)
        else:
            InitializeGUI.broadcast(False, "No User Found")
    """

print( TrainerBackend.getTrainerAvailableInvervals(datetime.date(2024, 4, 20) , 2) )
TrainerGUI.trainerPortal(2)
#AdminGUI.AdminPortal()

if __name__ == "__main__":
    #InitializeGUI.Initialize(user_input_received)
    #AdminGUI.AdminPortal()
    #MemberGUI.MemberPortal(user_input_global)
    #TrainerGUI.TrainerPortal()
    if user_input_global is not None:
        print("User input was:", user_input_global)
    else:
        print("No user input was received before the AdminGUI was closed.")