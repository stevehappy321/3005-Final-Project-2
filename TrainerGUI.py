import tkinter as tk
import datetime

import SQL
import TrainerBackend
import Utility

#root = None
#masterFrame = None
#subfunctionFrame = None

#manageHoursFrame = None
#earchMembersFrame = None
"""
layers:
    masterFrame
        manage hours
        search members
        prompts

    subfunctionFrame
        change start/end time


    prompts - REMOVED
        label
        entry
        submit
"""
masterFrame = None
subfunctionFrame = None

x=0
addCounter = False

changingStartTime = False
changingEndTime = False

indent = '    '

def trainerPortal(e):
    firstName = e.split(' ')[0]
    lastName = e.split(' ')[1]

    trainerID = SQL.StrictSelect(
        f"""
        SELECT * FROM Trainers t
        WHERE t.firstName = '{firstName}' AND t.lastName = '{lastName}'
        """
    )[0][0]

    print("Trainer Portal")

    def manageHours_click():
        print("Hours Management")  
        regenerateGUI()
        
        global manageHoursFrame

        manageHoursFrame = tk.Frame(root)
        manageHoursFrame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)

        #generate listbox
        listbox = tk.Listbox(manageHoursFrame, font=('Helvetica', '16'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #forgetButtons()

        def refresh(): #refresh main listbox
            workingHours = TrainerBackend.getTrainerHours(trainerID)

            listbox.delete(0, tk.END)
            listbox.insert(tk.END, "CURRENT WORKING HOURS")
            listbox.insert(tk.END, "Starting time: " + workingHours["startTime"].strftime("%H:%M"))
            listbox.insert(tk.END, "Ending time: " + workingHours["endTime"].strftime("%H:%M"))

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
                label = tk.Label(manageHoursFrame, text= "Enter your new starting time as hh:mm", font=('Helvetica', '14'))
                entry = tk.Entry(manageHoursFrame, font=('Helvetica', '14'), width=30)
                submit = tk.Button(manageHoursFrame, text="Submit", command=confirm, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')

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
                label = tk.Label(manageHoursFrame, text= "Enter your new end time as hh:mm", font=('Helvetica', '14'))
                entry = tk.Entry(manageHoursFrame, font=('Helvetica', '14'), width=30)
                submit = tk.Button(manageHoursFrame, text="Submit", command=confirm, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')

            label.pack()
            entry.pack(padx=40)
            submit.pack()

            changingEndTime = True            

        refresh()

        global subfunctionFrame
        subfunctionFrame = tk.Frame(root)
        subfunctionFrame.pack(side=tk.BOTTOM, pady=30)

        changeStartTime_button = tk.Button(subfunctionFrame, text="Change Start Hours", command=changeStartTime, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        changeStartTime_button.pack(side=tk.LEFT, padx=10)
        changeEndTime_button = tk.Button(subfunctionFrame, text="Change End Hours", command=changeEndTime, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        changeEndTime_button.pack(side=tk.LEFT, padx=10)




    def searchMembers_click():
        print("Search Members")  

        def refresh():
            membersMatchingName = TrainerBackend.searchMemberByName( entry.get() )

            for i in range( 0, len(membersMatchingName) ):
                membersMatchingName[i] = Utility.tupleToDict(
                    tuple= membersMatchingName[i],
                    keys= ["memberID", "firstName", "lastName", "address", "city", "phoneNumber", "email"]
                )

            print(membersMatchingName)

            listbox.delete(0, tk.END)
            for item in membersMatchingName:
                listbox.insert( tk.END, f"{item['firstName']} {item['lastName']}")
                listbox.insert( tk.END, f"{indent} Address: {item['address']}")
                listbox.insert( tk.END, f"{indent} City: {item['city']}")
                listbox.insert( tk.END, f"{indent} Phone Number: {item['phoneNumber']}")
                listbox.insert( tk.END, f"{indent} Email: {item['email']}")

        regenerateGUI()

        global searchMembersFrame
        searchMembersFrame = tk.Frame(root)
        searchMembersFrame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)

        #generate listbox
        listbox = tk.Listbox(searchMembersFrame, font=('Helvetica', '16'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        label = tk.Label(searchMembersFrame, text= "Enter a name to search", font=('Helvetica', '14'))
        entry = tk.Entry(searchMembersFrame, font=('Helvetica', '14'), width=30)
        submit = tk.Button(searchMembersFrame, text="Submit", command=refresh, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')

        label.pack()
        entry.pack(padx=40)
        submit.pack()

    def destroyWidgets(master):
        if master == None:
            return;

        children = master.winfo_children()
        
        for widget in children:
            widget.destroy();

    def regenerateGUI():
        #nonlocal root;
        nonlocal masterFrame;
        nonlocal button_manageWorkingHours;
        nonlocal button_searchMembers;

        destroyWidgets(root)
        #everything below the root disappears
        #reinstantiate widgets that need to be used immediately

        masterFrame = tk.Frame(root) # Create the master button frame
        masterFrame.pack(side=tk.BOTTOM, pady=20)

        # Create the buttons within the master button frame
        button_manageWorkingHours = tk.Button(
            masterFrame, 
            text="Manage Working Hours", 
            command=manageHours_click, 
            height=2, 
            width=20, 
            font=('Helvetica', '16'), 
            bg='#89BAE5')
        
        button_searchMembers = tk.Button(
            masterFrame, 
            text="Search Members", 
            command=searchMembers_click, 
            height=2, 
            width=30, 
            font=('Helvetica', '16'), 
            bg='#E59989')

        button_manageWorkingHours.pack(side=tk.LEFT, padx=10)
        button_searchMembers.pack(side=tk.LEFT, padx=10)
                    
    #"""
    #global root
    #global masterFrame

    # Create the main window
    root = tk.Tk()
    root.title("Trainer Controls")
    root.geometry("1400x600")  # Width x Height

    # Create and pack the buttons within the master button frame
    masterFrame = tk.Frame(root)
    masterFrame.pack(side=tk.BOTTOM, pady=20)
    
    button_manageWorkingHours = tk.Button(
        masterFrame, 
        text="Manage Working Hours", 
        command=manageHours_click, 
        height=2, 
        width=20, 
        font=('Helvetica', '16'), 
        bg='#89BAE5')
    
    button_searchMembers = tk.Button(
        masterFrame, 
        text="Search Members", 
        command=searchMembers_click, 
        height=2, 
        width=30, 
        font=('Helvetica', '16'), 
        bg='#E59989')

    button_manageWorkingHours.pack(side=tk.LEFT, padx=10)
    button_searchMembers.pack(side=tk.LEFT, padx=10)
    #"""

    # Start the Tkinter event loop
    root.mainloop()


"""
class PromptEntry:
    def __init__(self, masterFrame, prompt, callback):
        self.label = tk.Label(masterFrame, text=prompt, font=('Helvetica', '14'))
        self.entry = tk.Entry(masterFrame, font=('Helvetica', '14'), width=30)
        self.submit = tk.Button(masterFrame, text="Submit", command=callback, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
"""