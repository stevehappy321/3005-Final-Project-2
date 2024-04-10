import AdminGUI, MemberGUI, TrainerGUI, InitializeGUI
import SQL

#Ryan

userInputGlobal = None

#takes the input from the initializedGUI
def user_input_received(user_input):
    global userInputGlobal
    #gets the username and method of login
    userInputGlobal = user_input
    userInputGlobal = userInputGlobal.split(":")
    #if the method for logging in was admin and their credentials was ADMIN, start the GUI
    if(userInputGlobal[0] == 'Admin' and userInputGlobal[-2] == 'ADMIN'):
        InitializeGUI.broadcast(True, "Now logged in as: {}".format(userInputGlobal[-2]))
        InitializeGUI.closeGUI()
        AdminGUI.AdminPortal()
    #if the method for logging in was Member and their credentials was a valid member, start the member GUI
    elif (userInputGlobal[0] == 'Member'):
        if(SQL.memberExists(userInputGlobal[-2]) == True):
            InitializeGUI.broadcast(True, "User Found! Now logged in as: {}".format(userInputGlobal[-2]))
            InitializeGUI.closeGUI()
            MemberGUI.MemberPortal(userInputGlobal[-2])
        else:
            InitializeGUI.broadcast(False, "No Member Found")
    #if the method for logging in was Trainer and their credentials was a valid Trainer, start the member GUI
    elif (userInputGlobal[0] == 'Trainer'):
        if (SQL.userExists("Trainers", userInputGlobal[-2]) == True):
            InitializeGUI.broadcast(True, "User Found! Now logged in as: {}".format(userInputGlobal[-2]))
            InitializeGUI.closeGUI()
            TrainerGUI.trainerPortal(userInputGlobal[-2])
        else:
            InitializeGUI.broadcast(False, "No Trainer Found")
    #Admin Credential TIP prompt
    else:
        InitializeGUI.broadcast(False, "Login Not Valid. Try ADMIN")
    

#when program starts it'll initialize the GUI and create a variable that returns input in the initializeGUI file
if __name__ == "__main__":
    InitializeGUI.Initialize(user_input_received)
    #below is just for testing
    if userInputGlobal is not None:
        print("User input was:", userInputGlobal[1])