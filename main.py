import GUI
import SQL

user_input_global = None

def user_input_received(user_input):
    global user_input_global
    user_input_global = user_input
    #TODO EDGE CASE HERE WITH NAMES LONGER THAN 2
    if(user_input_global == 'ADMIN'):
        GUI.broadcast(True, "Now logged in as: {}".format(user_input_global))
        GUI.close_gui()
        GUI.AdminPortal()
    else:
        if(SQL.personExists(user_input_global) == True):
            GUI.broadcast(True, "User Found! Now logged in as: {}".format(user_input_global))
            GUI.close_gui()
        else:
            GUI.broadcast(False, "No User Found")
    

if __name__ == "__main__":
    GUI.Initialize(user_input_received)
    #GUI.AdminPortal()
    #GUI.test()
    # At this point, the GUI window has been closed
    print("The GUI has been closed.")
    if user_input_global is not None:
        print("User input was:", user_input_global)
    else:
        print("No user input was received before the GUI was closed.")