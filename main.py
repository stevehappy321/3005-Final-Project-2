import AdminGUI, MemberGUI, TrainerGUI, InitializeGUI
import SQL

#Ryan

user_input_global = None

def user_input_received(user_input):
    global user_input_global
    user_input_global = user_input
    user_input_global = user_input_global.split(":")

    if(user_input_global[0] == 'Admin' and user_input_global[-2] == 'ADMIN'):
        InitializeGUI.broadcast(True, "Now logged in as: {}".format(user_input_global[-2]))
        InitializeGUI.close_gui()
        AdminGUI.AdminPortal()

    elif (user_input_global[0] == 'Member'):
        if(SQL.memberExists(user_input_global[-2]) == True):
            InitializeGUI.broadcast(True, "User Found! Now logged in as: {}".format(user_input_global[-2]))
            InitializeGUI.close_gui()
            MemberGUI.MemberPortal(user_input_global[-2])
        else:
            InitializeGUI.broadcast(False, "No Member Found")

    elif (user_input_global[0] == 'Trainer'):
        if (SQL.userExists("Trainers", user_input_global[-2]) == True):
            InitializeGUI.broadcast(True, "User Found! Now logged in as: {}".format(user_input_global[-2]))
            InitializeGUI.close_gui()
            TrainerGUI.trainerPortal(user_input_global[-2])
        else:
            InitializeGUI.broadcast(False, "No Trainer Found")
            
    else:
        InitializeGUI.broadcast(False, "Login Not Valid. Try ADMIN")
    

if __name__ == "__main__":
    InitializeGUI.Initialize(user_input_received)
    if user_input_global is not None:
        print("User input was:", user_input_global[1])
    else:
        print("No user input was received before the AdminGUI was closed.")