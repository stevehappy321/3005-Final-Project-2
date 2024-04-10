import tkinter as tk
import SQL

#Ryan

root = None
curFrame = None
buttonFrame2 = None
x=0
addCounter = False
def AdminPortal():
    print("Admin Portal")
    
    ############################
    ###### BEGIN BUTTON 1 ###### 
    ############################


    def button1Click():
        global frame

        frame = tk.Frame(root)
        frame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)

        listbox = tk.Listbox(frame, font=('Helvetica', '15'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #gets all rooms
        equip = SQL.getAllSomething("Rooms")
        listbox.insert(tk.END, "RoomID, Room Name, Capacity, Room Purpose")
        # Insert items into the Listbox
        for item in equip:
            listbox.insert(tk.END, str(item))

        forgetButtons()
        #for filtering by un-used rooms
        def filter():
            global x
            if(x == 0):
                button6.config(foreground='white', background='#9389E5')   
                listbox.delete(0, tk.END)
                #selects all rooms where there does not exist a private session or fitnessclass as its registered rooms
                equip = SQL.getAllSomething("Rooms r WHERE NOT EXISTS (SELECT * FROM PrivateSession ps WHERE ps.RoomID = r.RoomID) AND NOT EXISTS (SELECT * FROM FitnessClass fc WHERE fc.RoomID = r.RoomID);")
                listbox.insert(tk.END, "RoomID, Name, Capacity, Type of Room")
                #insert
                for item in equip:
                    listbox.insert(tk.END, str(item))
                x=x+1
            else:
                reset()
                x=0
        #reset the view to base mode
        def reset():
                button6.config(foreground='Black', background='#9389E5') 
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("Rooms")
                listbox.insert(tk.END, "RoomID, Name, Capacity, Type of Room")
                # Insert items into the Listbox
                for item in equip:
                    listbox.insert(tk.END, str(item))
        #adds a new room to the building
        def addNew():
            #stops continuous button adding
            global addCounter
            if addCounter == True:
                return
            button7.config(foreground='white', background='#E59989')
            login_label = tk.Label(frame, text="Enter Room Details (Seperate by commas and spaces *no brackets*)", font=('Helvetica', '14'))
            login_label.pack()
            login_entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
            login_entry.pack(padx=40)
            #if the user clicks submit, send the query along
            def dingl():
                user_input = login_entry.get()
                SQL.addSomething("Rooms (Name, Capacity, Type) VALUES ({});".format(user_input))
                reset()
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
            button8.pack()
            addCounter = True
        #deletes the room based on the selected index
        def delete():
            index = listbox.curselection()
            selected_item = listbox.get(index)
            desired = selected_item.split(",")
            SQL.deleteSomething("Rooms Where RoomID = {};".format(desired[0].replace("(", "")))
            reset()

        global buttonFrame2
        buttonFrame2 = tk.Frame(root)
        buttonFrame2.pack(side=tk.BOTTOM, pady=30)
        button6 = tk.Button(buttonFrame2, text="Filter By Un-Used", command=filter, height=2, width=20, font=('Helvetica', '15'), bg='#9389E5')
        button6.pack(side=tk.LEFT, padx=10)
        button7 = tk.Button(buttonFrame2, text="Add New", command=addNew, height=2, width=20, font=('Helvetica', '15'), bg='#E59989')
        button7.pack(side=tk.LEFT, padx=10)
        button77 = tk.Button(buttonFrame2, text="Delete Selected", command=delete, height=2, width=20, font=('Helvetica', '15'), bg='#89BAE5')
        button77.pack(side=tk.LEFT, padx=10)
      
   
    ############################
    ###### BEGIN BUTTON 2 ###### 
    ############################

    def button2Click():
        global frame
        #used to filter the equipment by conditon "Old"
        def filter():
            #if x > 0 then filter otherwise go back normal
            global x
            if(x == 0):
                #clears the listbox and filters all based on Condition DESC   
                button6.config(foreground='white', background='#9389E5')
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("Equipment ORDER BY Condition DESC;")
                listbox.insert(tk.END, "ItemID, Item Name, Item Category, Purchase Date, Condition, Room Location, LastMaintenenace")
                #formats
                for item in equip:
                    listbox.insert(tk.END, str(item).replace("datetime.date", ""))
                x=x+1
            else:
                #resets view after filter clicked twice
                reset()
                x=0
        #resets the view to show all equipment
        def reset():
                button6.config(foreground='Black', background='#9389E5')  
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("Equipment")
                listbox.insert(tk.END, "ItemID, Item Name, Item Category, Purchase Date, Condition, Room Location, LastMaintenenace")
                # Insert items into the Listbox
                for item in equip:
                    listbox.insert(tk.END, str(item).replace("datetime.date", ""))
        #adds a new piece of equipment
        def addNew():
            #so user cant keep adding add buttons
            global addCounter
            if addCounter == True:
                return
            button7.config(foreground='white', background='#E59989')
            login_label = tk.Label(frame, text="Enter New Equipment Details", font=('Helvetica', '14'))
            login_label.pack()
            login_entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
            login_entry.pack(padx=40)
            #if user clicks dingl it will add a new Equipment to db based on inputted values
            def dingl():
                user_input = login_entry.get()
                SQL.addSomething("Equipment (Name, Type, PurchaseDate, Condition, RoomID, LastMaintenance) VALUES ({});".format(user_input))
                #resets view
                reset()
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
            button8.pack()
            addCounter = True
        #deletes the Equipment using the listbox selection
        def delete():
            index = listbox.curselection()
            selected_item = listbox.get(index)
            desired = selected_item.split(",")
            #deleted the Equipment by the ID
            SQL.deleteSomething("Equipment Where EquipmentSerialNumber = {};".format(desired[0].replace("(", "")))
            reset()

        global frame
        frame = tk.Frame(root)
        frame.pack(padx=100, pady=60, fill=tk.BOTH, expand=True)
        
        # Create the Scrollbar
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the Listbox and attach the Scrollbar, not seen elserwhere - too much work for not much return
        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=('Helvetica', '15'))
        listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        global buttonFrame2
        buttonFrame2 = tk.Frame(root)
        buttonFrame2.pack(side=tk.BOTTOM, pady=30)
        button6 = tk.Button(buttonFrame2, text="Filter Under Maintenance / Old", command=filter, height=2, width=30, font=('Helvetica', '15'), bg='#9389E5')
        button6.pack(side=tk.LEFT, padx=10)
        button7 = tk.Button(buttonFrame2, text="Add New", command=addNew, height=2, width=20, font=('Helvetica', '15'), bg='#E59989')
        button7.pack(side=tk.LEFT, padx=10)
        button77 = tk.Button(buttonFrame2, text="Delete Selected", command=delete, height=2, width=20, font=('Helvetica', '15'), bg='#89BAE5')
        button77.pack(side=tk.LEFT, padx=10)
        
        scrollbar.config(command=listbox.yview)
        #initially sets view to all equipment
        equip = SQL.getAllSomething("Equipment")
        listbox.insert(tk.END, "ItemID, Item Name, Item Category, Purchase Date, Condition, Room Location, LastMaintenance")
        # Insert items into the Listbox
        for item in equip:
            listbox.insert(tk.END, str(item).replace("datetime.date", ""))
        
        forgetButtons()


    ############################
    ###### BEGIN BUTTON 3 ###### 
    ############################


    def button3Click():
        global frame

        frame = tk.Frame(root)
        frame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)

        listbox = tk.Listbox(frame, font=('Helvetica', '15'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #gets all fitness Classes
        equip = SQL.getAllSomething("FitnessClass")
        listbox.insert(tk.END, "ClassID, ClassName, TrainerID, RoomID, ClassDate, StartTime, EndTime, Cost, Capacity")
        # Insert items into the Listbox
        for item in equip:
            newItem = str(item).replace("datetime.date", "")
            newItem = str(newItem).replace("datetime.time", "")
            listbox.insert(tk.END, newItem)
        #filters all fitnessClasses by (ClassDate + SessionTIME) ASC
        def filter():
            #if we have filtered, go back to default if pressed again
            global x
            if(x == 0):
                button6.config(foreground='white', background='#9389E5')   
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("FitnessClass ORDER BY (ClassDate + SessionTIME) ASC;")
                #print(equip)
                listbox.insert(tk.END, "ClassID, ClassName, TrainerID, RoomID, ClassDate, StartTime, EndTime, Cost, Capacity")
                for item in equip:
                    newItem = str(item).replace("datetime.date", "")
                    newItem = str(newItem).replace("datetime.time", "")
                    listbox.insert(tk.END, str(newItem))
                x=x+1
            else:
                reset()
                x=0
        #reset view to default
        def reset():
                button6.config(foreground='Black', background='#9389E5')
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("FitnessClass")
                listbox.insert(tk.END, "ClassID, ClassName, TrainerID, RoomID, ClassDate, StartTime, EndTime, Cost, Capacity")
                # Insert items into the Listbox
                for item in equip:
                    newItem = str(item).replace("datetime.date", "")
                    newItem = str(newItem).replace("datetime.time", "")
                    listbox.insert(tk.END, newItem)
        #adds new FitnessClass
        def addNew():
            #so the user cant keep adding stuff
            global addCounter
            if addCounter == True:
                return
            button7.config(foreground='white', background='#E59989')
            login_label = tk.Label(frame, text="Enter Fitness Class Details", font=('Helvetica', '14'))
            login_label.pack()
            login_entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
            login_entry.pack(padx=40)
            #adds the users input to the fintessclasses
            def dingl():
                user_input = login_entry.get()
                SQL.addSomething("FitnessClass (ClassName, TrainerID, RoomID, ClassDate, SessionTime, EndTime, Cost, Capacity) VALUES ({});".format(user_input))
                reset()
                login_label.pack_forget()
                login_entry.pack_forget()
                button8.pack_forget()
                #removes text from textbox
                login_entry.delete(0, tk.END)
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
            button8.pack()
            addCounter = True
        #deletes the selected fitnessclass using the index in the listbox and its ID
        def delete():
            index = listbox.curselection()
            selected_item = listbox.get(index)
            desired = selected_item.split(",")
            SQL.deleteSomething("FitnessClass Where classID = {};".format(desired[0].replace("(", "")))
            reset()
        #updates the fitness class
        def update():
            global addCounter
            if addCounter == True:
                return
            button777.config(foreground='white', background='#E2EC70')
            login_label = tk.Label(frame, text="Enter Fitness Class Change", font=('Helvetica', '14'))
            login_label.pack()
            entries = []
            #Creates the fields to check
            info = {0:"ClassName", 1:"TrainerID", 2:"RoomID", 3:"ClassDate", 4:"SessionTime", 5:"EndTime", 6:"Cost", 7:"Capacity"}
            info2 = ["ClassName", "TrainerID", "RoomID", "ClassDate", "SessionTime", "EndTime", "Cost", "Capacity"]
            def dingl():
                newClass = []
                #gets the index from the box to be updated
                index = listbox.curselection()
                selected_item = listbox.get(index)
                desired = selected_item.split(",")
                #Checks the input boxes for changed values. If it finds it'll add to the newClass array
                for i in range(8):
                    if(entries[i].get() != info.get(i)):
                        #print(entries[i].get())
                        newClass.append(info.get(i))
                        newClass.append(entries[i].get())
                    entries[i].pack_forget()
                login_label.pack_forget()
                button8.pack_forget()
                #X means that we have a value to extract, when X is true we extract its value from the next element on next iteration
                x=False
                query =''
                #for each element that was changed, create the query
                for i in newClass:
                    if(i in info2 or x == True):
                        if(x==True):
                            query +='\''
                            query +=i
                            query += '\', '
                            x= False
                        else:
                            query += i
                            query += " = "
                            x=True
                #takes the ClassID from the box and inserts into query
                query += ' WHERE ClassID = {};'.format(desired[0].replace("(", ""))
                #updates the database. The format and.replace is removing the last occurance of a , for the query
                SQL.UpdateSomething("FitnessClass SET {}".format(query[::-1].replace(',', '', 1)[::-1]))
                #resets the view
                reset()

            #Creates the buttons to change the fields
            for i in range(8):
                string = str(info.get(i))
                entry = tk.Entry(frame, font=('Helvetica', '15'), width=16)
                entry.pack()  
                entry.insert(0, string)  
                entries.append(entry)  
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
            button8.pack()
            addCounter = True
        

        global buttonFrame2
        buttonFrame2 = tk.Frame(root)
        buttonFrame2.pack(side=tk.BOTTOM, pady=30)
        button6 = tk.Button(buttonFrame2, text="Filter By Upcoming", command=filter, height=2, width=20, font=('Helvetica', '15'), bg='#9389E5')
        button6.pack(side=tk.LEFT, padx=10)
        button7 = tk.Button(buttonFrame2, text="Add New", command=addNew, height=2, width=20, font=('Helvetica', '15'), bg='#E59989')
        button7.pack(side=tk.LEFT, padx=10)
        button77 = tk.Button(buttonFrame2, text="Delete Selected", command=delete, height=2, width=20, font=('Helvetica', '15'), bg='#89BAE5')
        button77.pack(side=tk.LEFT, padx=10)
        button777 = tk.Button(buttonFrame2, text="Update Selected", command=update, height=2, width=20, font=('Helvetica', '15'), bg='#E2EC70')
        button777.pack(side=tk.LEFT, padx=10)

        forgetButtons()


    ############################
    ###### BEGIN BUTTON 4 ###### 
    ############################


    def button4Click():
        global frame

        frame = tk.Frame(root)
        frame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)

        listbox = tk.Listbox(frame, font=('Helvetica', '15'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #selects desired info from users. We have to join because we want the first and last name in member, but mainly the payment info in payments
        equip = SQL.StrictSelect("SELECT m.MemberID, m.FirstName, m.LastName, p.PaymentDate, p.AmountPayed, p.AmountOwed, p.PaymentMethod FROM Members m JOIN Payment p ON m.MemberID = p.MemberID;")
        
        listbox.insert(tk.END, "MemberID, FirstName, LastName, Last Payment Date, AmountPayed, AmountOwed, PaymentMethod")
        # Insert items into the Listbox
        for item in equip:
            item = str(item).replace("datetime.date", "")
            item = item.replace("Decimal", "")
            listbox.insert(tk.END, item)
        #filter based on the p.AmountOwed field --> Desc;
        def filter():
            global x
            if(x == 0):
                button6.config(foreground='white', background='#9389E5')   
                listbox.delete(0, tk.END)
                equip = SQL.StrictSelect("SELECT m.MemberID, m.FirstName, m.LastName, p.PaymentDate, p.AmountPayed, p.AmountOwed, p.PaymentMethod FROM Members m JOIN Payment p ON m.MemberID = p.MemberID ORDER BY p.amountOwed DESC;")
                listbox.insert(tk.END, "MemberID, FirstName, LastName, Last Payment Date, AmountPayed, AmountOwed, PaymentMethod")
                for item in equip:
                    item = str(item).replace("datetime.date", "")
                    item = item.replace("Decimal", "")
                    listbox.insert(tk.END, item)
                x=x+1
            else:
                reset()
                x=0
        #resets the view to default
        def reset():
                button6.config(foreground='Black', background='#9389E5') 
                listbox.delete(0, tk.END)
                equip = SQL.StrictSelect("SELECT m.MemberID, m.FirstName, m.LastName, p.PaymentDate, p.AmountPayed, p.AmountOwed, p.PaymentMethod FROM Members m JOIN Payment p ON m.MemberID = p.MemberID;")
                listbox.insert(tk.END, "MemberID, FirstName, LastName, Last Payment Date, AmountPayed, AmountOwed, PaymentMethod")
                # Insert items into the Listbox
                for item in equip:
                    item = str(item).replace("datetime.date", "")
                    item = item.replace("Decimal", "")
                    listbox.insert(tk.END, item)

        global buttonFrame2
        buttonFrame2 = tk.Frame(root)
        buttonFrame2.pack(side=tk.BOTTOM, pady=30)
        button6 = tk.Button(buttonFrame2, text="Filter By Amount Owed", command=filter, height=2, width=20, font=('Helvetica', '15'), bg='#9389E5')
        button6.pack()

        forgetButtons()
    
    
    ############################
    ##### MAIN WINDOW PANE ##### 
    ############################

    def returnButton():
        button1.pack(side=tk.LEFT, padx=10)
        button2.pack(side=tk.LEFT, padx=10)
        button3.pack(side=tk.LEFT, padx=10)
        button4.pack(side=tk.LEFT, padx=10)
        button5.pack_forget()
        frame.destroy()
        buttonFrame2.destroy()
        global addCounter
        addCounter = False

    def forgetButtons():
        button1.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        button4.pack_forget()
        button5.pack(side=tk.LEFT, padx=10)

    # Create the main window
    root = tk.Tk()
    root.title("Admin Controls")
    root.geometry("1400x600")  # Width x Height

    # Create and pack the buttons within the button frame
    buttonFrame = tk.Frame(root)
    buttonFrame.pack(side=tk.BOTTOM, pady=20)
    button1 = tk.Button(buttonFrame, text="Room Booking Mgmnt", command=button1Click, height=2, width=20, font=('Helvetica', '15'), bg='#89BAE5')
    button2 = tk.Button(buttonFrame, text="Equipment Maintenance Monitoring", command=button2Click, height=2, width=30, font=('Helvetica', '15'), bg='#E59989')
    button3 = tk.Button(buttonFrame, text="Class Schedule Updating", command=button3Click, height=2, width=20, font=('Helvetica', '15'), bg='#9389E5')
    button4 = tk.Button(buttonFrame, text="Billing and Payment Proccessing", command=button4Click, height=2, width=30, font=('Helvetica', '15'), bg='#7A2727')
    button5 = tk.Button(buttonFrame, text="Return", command=returnButton, height=2, width=20, font=('Helvetica', '15'), bg='#7A2727')

    button1.pack(side=tk.LEFT, padx=10)
    button2.pack(side=tk.LEFT, padx=10)
    button3.pack(side=tk.LEFT, padx=10)
    button4.pack(side=tk.LEFT, padx=10)

    # Start the Tkinter event loop
    root.mainloop()
