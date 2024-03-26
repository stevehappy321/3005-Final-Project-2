import AdminGUI
import SQL

user_input_global = None

def user_input_received(user_input):
    global user_input_global
    user_input_global = user_input
    #TODO EDGE CASE HERE WITH NAMES LONGER THAN 2
    if(user_input_global == 'ADMIN'):
        AdminGUI.broadcast(True, "Now logged in as: {}".format(user_input_global))
        AdminGUI.close_gui()
        AdminGUI.AdminPortal()
    else:
        if(SQL.personExists(user_input_global) == True):
            AdminGUI.broadcast(True, "User Found! Now logged in as: {}".format(user_input_global))
            AdminGUI.close_gui()
        else:
            AdminGUI.broadcast(False, "No User Found")
    

if __name__ == "__main__":
    #AdminGUI.Initialize(user_input_received)
    AdminGUI.AdminPortal()
    #AdminGUI.test()
    # At this point, the AdminGUI window has been closed
    print("The AdminGUI has been closed.")
    if user_input_global is not None:
        print("User input was:", user_input_global)
    else:
        print("No user input was received before the AdminGUI was closed.")