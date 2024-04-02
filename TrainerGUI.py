import tkinter as tk
import SQL
import TrainerBackend

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
        startTime = workingHours["startTIme"]
        endTime = workingHours["endTime"]

        # Insert items into the Listboxes
        listbox_startingHour = tk.Listbox(frame, font=('Helvetica', '16'), height=10, width=50)
        listbox_startingHour.place(x-20, y=20)

        listbox = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        listbox.insert(tk.END, "CURRENT WORKING HOURS" + startTime)
        listbox.insert(tk.END, "starting time: " + startTime)
        listbox.insert(tk.END, "ending time: " + endTime)

        #forgetButtons()

        def reset():
            #reset working hours to 9-5
            return;
                
        def addNew():
            global addCounter
            if addCounter == True:
                return
            button7.config(foreground='white', background='#9389E5')
            login_label = tk.Label(frame, text="Enter Room Details (Seperate by commas and spaces *no brackets*)", font=('Helvetica', '14'))
            login_label.pack()
            login_entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
            login_entry.pack(padx=40)
            def dingl():
                user_input = login_entry.get()
                SQL.addSomething("Rooms (Name, Capacity, Type) VALUES ({});".format(user_input))
                reset()
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
            button8.pack()
            addCounter = True

        def delete():
            index = listbox.curselection()
            selected_item = listbox.get(index)
            desired = selected_item.split(",")
            SQL.deleteSomething("Rooms Where RoomID = {};".format(desired[0].replace("(", "")))
            reset()

        global trainerButtonFrame
        trainerButtonFrame = tk.Frame(root)
        trainerButtonFrame.pack(side=tk.BOTTOM, pady=30)
        button7 = tk.Button(trainerButtonFrame, text="Add New", command=addNew, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button7.pack(side=tk.LEFT, padx=10)
        button77 = tk.Button(trainerButtonFrame, text="Delete Selected", command=delete, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button77.pack(side=tk.LEFT, padx=10)

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


        executeSearchMembersButton = tk.Button(
            trainerButtonFrame, 
            text="Search", 
            command=TrainerBackend.searchMemberByName("""search name"""), 
            height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
