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

changingStartTime = False
changingEndTime = False

def trainerPortal(trainerID):
    print("Trainer Portal")        

    def manageHours_click():
        global frame

        frame = tk.Frame(root)
        frame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)

        #generate listboxes
        listbox = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #forgetButtons()

        def refresh(): #refresh main listbox
            workingHours = TrainerBackend.getTrainerHours(trainerID)
            startTime = workingHours["startTime"]
            endTime = workingHours["endTime"]

            listbox.delete(0, tk.END)
            listbox.insert(tk.END, "CURRENT WORKING HOURS")
            listbox.insert(tk.END, "Starting time: " + startTime.strftime("%H:%M"))
            listbox.insert(tk.END, "Ending time: " + endTime.strftime("%H:%M"))

        def changeStartTime():
            def confirm():
                value = entry.get()
                timeArr = value.split(':') #returns array as [h, m]

                hour = timeArr[0]
                minute = 0 if len(timeArr) < 2 else timeArr[1]

                if hour.isnumeric() and minute.isnumeric() and len(timeArr) == 2:
                    TrainerBackend.setTrainerStartTime(
                        trainerID, 
                        datetime.time(hour=int(timeArr[0]), minute=int(timeArr[1])), 
                    )

                entry.destroy()
                label.destroy()
                submit.destroy()

                global changingStartTime
                changingStartTime = False

                refresh();
            
            global changingStartTime
            if not changingStartTime:
                label = tk.Label(frame, text= "Enter your new starting time as hh:mm", font=('Helvetica', '14'))
                entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
                submit = tk.Button(frame, text="Submit", command=confirm, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')

            label.pack()
            entry.pack(padx=40)
            submit.pack()

            changingStartTime = True

        def changeEndTime():
            def confirm():
                value = entry.get()
                timeArr = value.split(':') #returns array as [h, m]

                hour = timeArr[0]
                minute = 0 if len(timeArr) < 2 else timeArr[1]

                if hour.isnumeric() and minute.isnumeric() and len(timeArr) == 2:
                    TrainerBackend.setTrainerEndTime(
                        trainerID, 
                        datetime.time(hour=int(timeArr[0]), minute=int(timeArr[1])), 
                    )
                
                entry.destroy()
                label.destroy()
                submit.destroy()

                global changingEndTime
                changingEndTime = False

                refresh();
            
            global changingEndTime
            if not changingEndTime:
                label = tk.Label(frame, text= "Enter your new end time as hh:mm", font=('Helvetica', '14'))
                entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
                submit = tk.Button(frame, text="Submit", command=confirm, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')

            label.pack()
            entry.pack(padx=40)
            submit.pack()

            changingEndTime = True            

        refresh();

        global trainerButtonFrame
        trainerButtonFrame = tk.Frame(root)
        trainerButtonFrame.pack(side=tk.BOTTOM, pady=30)
        changeStartTime_button = tk.Button(trainerButtonFrame, text="Change Start Hours", command=changeStartTime, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        changeStartTime_button.pack(side=tk.LEFT, padx=10)
        changeEndTime_button = tk.Button(trainerButtonFrame, text="Change End Hours", command=changeEndTime, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        changeEndTime_button.pack(side=tk.LEFT, padx=10)
        
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

def searchMembers_click():
    executeSearchMembersButton = tk.Button(
        trainerButtonFrame, 
        text="Search", 
        command=TrainerBackend.searchMemberByName("""search name"""), 
        height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')


class PromptEntry:
    def __init__(self, masterFrame, prompt, callback):
        self.label = tk.Label(masterFrame, text=prompt, font=('Helvetica', '14'))
        self.entry = tk.Entry(masterFrame, font=('Helvetica', '14'), width=30)
        self.submit = tk.Button(masterFrame, text="Submit", command=callback, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
