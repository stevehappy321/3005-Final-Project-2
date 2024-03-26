import AdminGUI
import InitializeGUI
import SQL

user_input_global = None

def user_input_received(user_input):
    global user_input_global
    user_input_global = user_input
    if(user_input_global == 'ADMIN'):
        InitializeGUI.broadcast(True, "Now logged in as: {}".format(user_input_global))
        InitializeGUI.close_gui()
        AdminGUI.AdminPortal()
    else:
        if(SQL.personExists(user_input_global) == True):
            InitializeGUI.broadcast(True, "User Found! Now logged in as: {}".format(user_input_global))
            InitializeGUI.close_gui()
        else:
            InitializeGUI.broadcast(False, "No User Found")
    

if __name__ == "__main__":
    #InitializeGUI.Initialize(user_input_received)
    AdminGUI.AdminPortal()
    #AdminGUI.test()
    print("The AdminGUI has been closed.")
    if user_input_global is not None:
        print("User input was:", user_input_global)
    else:
        print("No user input was received before the AdminGUI was closed.")