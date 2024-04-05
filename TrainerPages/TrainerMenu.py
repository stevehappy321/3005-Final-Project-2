import tkinter as tk
import datetime

import TrainerBackend as Backend
from TrainerPages import TrainerManageHours
from TrainerPages import TrainerSearchMembers

"""
frame structure:

root
    master
        manage hours
            #change start time
            #change end time
        search members

all widgets, once created, exist forever and are not destroyed
    unused widgets are hidden
"""

def trainerPortal(trainerID):
    def manageHours():
        TrainerSearchMembers.detach(); #detach all subpages but manage hours
        TrainerManageHours.manageHours(trainerID, frame)

    def searchMembers():
        TrainerManageHours.detach();
        TrainerSearchMembers.manageHours(trainerID, frame)

    # Create the main window
    root = tk.Tk()
    root.title("Trainer Controls")
    root.geometry("1400x600")  # Width x Height

    #master frame
    frame = tk.Frame(root)
    #frame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)
    frame.pack(side=tk.BOTTOM, pady=20)

    manageHoursButton = tk.Button(
        frame, 
        text="Manage Working Hours", 
        command=manageHours, 
        height=2, 
        width=20, 
        font=('Helvetica', '16'), 
        bg='#89BAE5')

    searchMembersButton = tk.Button(
        frame, 
        text="Search Members", 
        command=searchMembers, 
        height=2, 
        width=30, 
        font=('Helvetica', '16'), 
        bg='#E59989')

    manageHoursButton.pack(side=tk.LEFT, padx=10)
    searchMembersButton.pack(side=tk.LEFT, padx=10)

    # Start the Tkinter event loop
    root.mainloop()