import tkinter as tk
import datetime

import SQL
import TrainerBackend
import Utility

root = None
curFrame = None
trainerButtonFrame = None
x=0
addCounter = False

def trainerPortal(trainerID):
    print("Trainer Portal")

    def manageHours_click():
        global frame

        frame = tk.Frame(root)
        frame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)

        workingHours = TrainerBackend.getTrainerHours(trainerID)
        print(workingHours)
        startTime = workingHours["startTime"]
        endTime = workingHours["endTime"]

        # Insert items into the Listboxes
        listbox = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        listbox.insert(tk.END, "CURRENT WORKING HOURS")
        listbox.insert(tk.END, "Starting time: " + startTime.strftime("%H:%M"))
        listbox.insert(tk.END, "Ending time: " + endTime.strftime("%H:%M"))

        #forgetButtons()

        def reset(): #reset working hours to 9-5
            TrainerBackend.setTrainerStartHours(
                trainerID, 
                datetime.time(hour=9, minute=0), 
            )
            
            TrainerBackend.setTrainerEndHours(
                trainerID, 
                datetime.time(hour=17, minute=0)
            )

        def changeStartTime():
            label = tk.Label(
                frame, 
                text= "Enter your new starting time as hh:mm", 
                font=('Helvetica', '14'))
            label.pack()

            entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
            entry.pack(padx=40)

            def confirm():
                value = entry.get()
                timeArr = value.split(':') #returns array as [h, m]

                TrainerBackend.setTrainerStartHours(
                    trainerID, 
                    datetime.time(hour=timeArr[0], minute=timeArr[1]), 
                )

            submit = tk.Button(frame, text="Submit", command=confirm, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
            submit.pack()

        def changeEndTime():
            label = tk.Label(
                frame, 
                text= "Enter your new end time as hh:mm", 
                font=('Helvetica', '14'))
            label.pack()

            entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
            entry.pack(padx=40)

            def confirm():
                value = entry.get()
                timeArr = value.split(':') #returns array as [h, m]

                TrainerBackend.setTrainerEndHours(
                    trainerID, 
                    datetime.time(hour=timeArr[0], minute=timeArr[1]), 
                )

            submit = tk.Button(frame, text="Submit", command=confirm, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
            submit.pack()

        global trainerButtonFrame
        trainerButtonFrame = tk.Frame(root)
        trainerButtonFrame.pack(side=tk.BOTTOM, pady=30)
        changeStartTime_button = tk.Button(trainerButtonFrame, text="Change Start Hours", command=changeStartTime, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        changeStartTime_button.pack(side=tk.LEFT, padx=10)
        changeEndTime_button = tk.Button(trainerButtonFrame, text="Change End Hours", command=changeEndTime, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        changeEndTime_button.pack(side=tk.LEFT, padx=10)

        """
        button_incrementStartHour = tk.Button(
            trainerButtonFrame, 
            text="↑", 
            command=manageHours_click(), 
            height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        
        button_decrementStartHour = tk.Button(
            trainerButtonFrame, 
            text="↓", 
            command=manageHours_click(), 
            height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')

        button_incrementEndHour = tk.Button(
            trainerButtonFrame, 
            text="↑", 
            command=manageHours_click(), 
            height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        
        button_decrementEndHour = tk.Button(
            trainerButtonFrame, 
            text="↓", 
            command=manageHours_click(), 
            height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        """
    def searchMembers_click():

        executeSearchMembersButton = tk.Button(
            trainerButtonFrame, 
            text="Search", 
            command=TrainerBackend.searchMemberByName("""search name"""), 
            height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        
    # Create the main window
    root = tk.Tk()
    root.title("Trainer Controls")
    root.geometry("1400x600")  # Width x Height

    # Create and pack the buttons within the button frame
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=20)

    button_manageWorkingHours = tk.Button(
        button_frame, 
        text="Manage Working Hours", 
        command=manageHours_click, 
        height=2, 
        width=20, 
        font=('Helvetica', '16'), 
        bg='#89BAE5')
    button_searchMembers = tk.Button(
        button_frame, 
        text="Search Members", 
        command=searchMembers_click, 
        height=2, 
        width=30, 
        font=('Helvetica', '16'), 
        bg='#E59989')

    button_manageWorkingHours.pack(side=tk.LEFT, padx=10)
    button_searchMembers.pack(side=tk.LEFT, padx=10)

    # Start the Tkinter event loop
    root.mainloop()
