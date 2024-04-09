import tkinter as tk
from tkinter import messagebox
import SQL, MemberBackend

import datetime
from datetime import datetime

testValue2 = []
frame = None
globalBool = True
updateCounter = False
currentSelection = ""
userID = 0
def MemberPortal(e):
    testValue = e
    testValue2 = testValue.split(" ")
    userID = SQL.getMemberNumber("'{}' AND LastName = '{}'".format(testValue2[0], testValue2[1]))
    userID = str(userID).replace("[(", "").replace(",)]", "")
    userID = int(userID)
    #If User Updates name it will still work
    def updateName():
        needed = SQL.StrictSelect("Select Firstname, Lastname From Members Where memberId = {}".format(userID))
        needed = (str(needed[0]).replace(",", "").replace("(", "").replace(")", "").replace("\'", ""))
        if(testValue != needed):
            root.destroy()
            MemberPortal(needed)
        return 
    def button1_click():
        updateName()
        forgetButtons()
        global frame
        global updateCounter
        frame = tk.Frame(root)
        frame.pack(padx=150, pady=20, fill=tk.BOTH, expand=True)
        listbox = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        listbox.insert(tk.END, "                           Personal Info")
        equip = SQL.getAllSomething("Members WHERE FirstName = '{}' AND LastName = '{}';".format(testValue2[0], testValue2[1]))
        equip = str(equip)
        cleaned_string = equip.replace('[(', '').replace(')]', '').replace(',', '').replace("'", '')
        # Insert items into the Listbox
        equip = cleaned_string.split(" ")
        addrString =''
        info2 = ["MemberID:   ", "First Name:  ", "Last Name:  ", "Address:      ", "City:             ", "Phone #:      ", "Email:           "]
        for i in range(9):
            if(i == 3 or i==4 or i==5):
                addrString += equip[i] + ' '
                if(i == 5):
                    listbox.insert(tk.END, info2[3] + addrString)
                    continue
            else:
                if(i>=6):    
                    listbox.insert(tk.END, info2[i-2] + equip[i])
                else:
                    listbox.insert(tk.END, info2[i] + equip[i])

        def on_select(event):
            current_selection = event.widget.curselection()
            if current_selection:  # Check if there's any selection
                current_index = current_selection[0]
                if current_index == 0:  # If the first item is selected
                    # Revert to the previous selection (or clear selection if no previous)
                    listbox.selection_clear(0, tk.END)
                    for index in previous_selection:
                        listbox.selection_set(index)
            else:
                # No item is selected; this block can be useful for additional logic if needed
                pass
        # Update the previous selection
        global previous_selection
        previous_selection = listbox.curselection()

        def reset():
                returnButton()
                button1_click()

        def update():
            global updateCounter
            if updateCounter == True:
                return
            updateCounter = True
            button777.config(foreground='white', background='#9389E5')
            login_label = tk.Label(frame, text="Enter Personal Info Change.", font=('Helvetica', '14'))
            login_label.pack()
            login_label = tk.Label(frame, text="(Select the item and then type in the desinated box)", font=('Helvetica', '14'))
            login_label.pack()
            login_label = tk.Label(frame, text="*Please only change 1 element at a time*", font=('Helvetica', '14'))
            login_label.pack()
            entries = []
            #Creates the fields to check
            info = {0:"MemberID", 1:"FirstName", 2:"LastName", 3:"Address", 4:"City", 5:"PhoneNumber", 6:"Email"}
            info2 = ["MemberID", "FirstName", "LastName", "Address", "City", "PhoneNumber", "Email"]

            def dingl():
                newClass = []
                MemberID = listbox.get(1)
                MemberID = MemberID.replace(":", "").replace(" ", "").replace("MemberID", "")
            #gets the index from the box to be updated
                index = listbox.curselection()
                selected_item = listbox.get(index)
                desired = selected_item.split(",")
                #Checks the input boxes for changed values. If it finds it'll add to the newClass array
                for i in range(7):
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
                if(newClass[0] == 'MemberID'):
                    newClass.pop(0)
                    newClass.pop(0)
                    if (len(newClass) == 0 ):
                        reset()
                        return
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
                print(newClass)
                query += ' WHERE MemberID = {};'.format(MemberID)
                SQL.UpdateSomething("Members SET {}".format(query[::-1].replace(',', '', 1)[::-1]))
                print(query)
                reset()

            #Creates the buttons to change the fields
            for i in range(7):
                string = str(info.get(i))
                entry = tk.Entry(frame, font=('Helvetica', '16'), width=16)
                entry.pack(pady=1)  
                entry.insert(0, string)  
                entries.append(entry)  
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
            button8.pack()

        listbox.bind('<<ListboxSelect>>', on_select)
        global button_frame1
        button_frame1 = tk.Frame(root)
        button_frame1.pack(side=tk.BOTTOM, pady=20)
        button777 = tk.Button(button_frame1, text="Update Info", command=update, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button777.pack(side=tk.LEFT, padx=10)








    def button2_click():
        forgetButtons()
        global frame
        frame = tk.Frame(root)
        frame.pack(padx=40, pady=20, fill=tk.BOTH, expand=True)
        listbox2 = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        listbox3 = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        listbox2.insert(tk.END, "                          Fitness Goals")
        listbox3.insert(tk.END, "                          Health Metrics")

        def update():
            global updateCounter
            if updateCounter == True:
                return
            updateCounter = True
            button777.config(foreground='white', background='#9389E5')
            login_label = tk.Label(frame, text="Enter Personal Info Change", font=('Helvetica', '14'))
            login_label.pack()
            entries = []
            #Creates the fields to check
            def dingl():
                global currentSelection
                #print("Updating")
                print(currentSelection)
                currentSelection = currentSelection.split(" ")
                dingle = []
                for item in currentSelection:
                    dingle.append(item.replace(" ", ""))

                infoUpdate = [x.strip('') for x in dingle]
                print(infoUpdate)
                if(infoUpdate == ['']):
                    print("returning")
                    returnButton()
                    button2_click()
                    return
                currentSelection = ''
                memberNumber = SQL.getMemberNumber("'{}' AND LastName = '{}'".format(testValue2[0], testValue2[1]))[0]
                memberNumber = str(memberNumber).replace(",)", "").replace("(", "")
                query =''
                if(infoUpdate[0] == 'LISTBOX2&'):
                    if(infoUpdate[1] == 'DistanceRunningGoal:' or infoUpdate[1] == 'FastestLapGoal:'or infoUpdate[1] == 'CurrentRunDistance:'or infoUpdate[1] == 'CurrentFastestLap:'):
                        query+= "FitnessStuffs SET {} = '{}' Where MemberID = {};".format(str(infoUpdate[1]).strip(":"), (entries[0].get()), int(memberNumber))
                    else:
                        query+= 'FitnessStuffs SET {} = {} Where MemberID = {};'.format(str(infoUpdate[1]).strip(":"), entries[0].get(), int(memberNumber))
                if(infoUpdate[0] == 'LISTBOX3&'):
                    if(infoUpdate[1] == 'LastMeasurementDate:'):
                        query+= 'HealthStuffs SET MeasurementDate = CURRENT_DATE Where MemberID = {};'.format(int(memberNumber))
                    elif(infoUpdate[1] == 'BloodPressure:'):
                        query+= "HealthStuffs SET BloodPressure = '{}' Where MemberID = {};".format((entries[0].get()), int(memberNumber))
                    else:
                        query+= 'HealthStuffs SET {} = {} Where MemberID = {};'.format(str(infoUpdate[1]).strip(":"), entries[0].get(), int(memberNumber))
                SQL.UpdateSomething(query)
                returnButton()
                button2_click()

            for i in range(1):
                string = str("Enter Change Here")
                entry = tk.Entry(frame, font=('Helvetica', '16'), width=16)
                entry.pack(pady=1)  
                entry.insert(0, string)  
                entries.append(entry)  
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
            button8.pack()

        insertString = f"""
                        SELECT 
                            f.DistanceRunningGoal, 
                            f.FastestLapGoal, 
                            f.BenchPressGoal, 
                            f.SquatGoal, 
                            f.SwimmingDistanceGoal, 
                            f.CurrentRunDistance, 
                            f.CurrentFastestLap, 
                            f.CurrentBenchPress, 
                            f.CurrentSquat, 
                            f.CurrentSwimDistance
                        FROM 
                            Members m
                        JOIN 
                            FitnessStuffs f ON m.MemberID = f.MemberID
                        WHERE 
                            m.FirstName = '&' AND m.LastName = '*';
                        """.replace('&', testValue2[0]).replace('*', testValue2[1])
        
        info2 = ["DistanceRunningGoal:    ", "FastestLapGoal:      ", "BenchPressGoal:     ", "SquatGoal:               ", "SwimmingDistanceGoal:  ", "CurrentRunDistance: ", "CurrentFastestLap: ", "CurrentBenchPress: ", "CurrentSquat: ", "CurrentSwimDistance: "]
        equip = SQL.StrictSelect(insertString)
        equip = str(equip)
        cleaned_string = equip.replace('[(', '').replace(')]', '').replace("'", '')
        # Insert items into the Listbox
        print(cleaned_string)
        equip = cleaned_string.split(", ")
        for i in range(len(equip)):
            if(i ==5):
               listbox2.insert(tk.END, "________________________________________________________") 
            listbox2.insert(tk.END, info2[i] + equip[i])
        
        insertString = f"""
                        SELECT  
                            h.MeasurementDate, 
                            h.Weight, 
                            h.BloodPressure, 
                            h.HeartRate,
                            h.WeightGoal, 
                            h.HeartRateGoal
                        FROM 
                            Members m
                        JOIN 
                            HealthStuffs h ON m.MemberID = h.MemberID
                        WHERE 
                            m.FirstName = '&' AND m.LastName = '*';
                        """.replace('&', testValue2[0]).replace('*', testValue2[1])
        
        equip = SQL.StrictSelect(insertString)
        equip = str(equip)
        cleaned_string = equip.replace('[(', '').replace(')]', '').replace("'", '')
        # Insert items into the Listbox
        print(cleaned_string)
        equip21 = cleaned_string.replace("Decimal(", "").replace("datetime.date(", "").replace(")", "").replace(")", "")
        equip = equip21.split(", ")
        info2 = ["LastMeasurementDate: ", "Weight: ", "BloodPressure: ", "HeartRate: ", "WeightGoal: ", "HeartRateGoal: "]
        for i in range(len(equip)):
            #print(str(i) +": " + equip[i])
            if(i == 0 or i==1 or i==2 or i==6):
                #print(equip[i])
                if(i ==2):
                    listbox3.insert(tk.END, info2[0] + " " + equip[0] + " " + equip[1] + " " + equip[2])
                if(i ==6):
                    listbox3.insert(tk.END, "_______________________________________________________")
                    listbox3.insert(tk.END, info2[i-2] + " " + equip[i])
                continue
            listbox3.insert(tk.END, info2[i-2] + " " + equip[i])
        #
        def on_select2(event):
            current_selection = event.widget.curselection()
            if current_selection:  # Check if there's any selection
                current_index = current_selection[0]
                if current_index == 0 or current_index == 6:  # If the first item or 6th
                    # Revert to the previous selection (or clear selection if no previous)
                    listbox2.selection_clear(0, tk.END)
                    for index in previous_selection:
                        listbox2.selection_set(index)  
                else:
                    global currentSelection
                    currentSelection += "LISTBOX2& "
                    currentSelection += listbox2.get(current_index)
                    #print(currentSelection)

        def on_select3(event):
            current_selection = event.widget.curselection()
            if current_selection:  # Check if there's any selection
                current_index = current_selection[0]
                if current_index == 0 or current_index == 5:  # If the first item or 6th
                    # Revert to the previous selection (or clear selection if no previous
                    listbox3.selection_clear(0, tk.END)
                    for index in previous_selection:
                        listbox3.selection_set(index)
                else:
                    global currentSelection
                    currentSelection += "LISTBOX3& "
                    currentSelection += listbox3.get(current_index)
                    #print(currentSelection)
                

        listbox2.bind('<<ListboxSelect>>', on_select2)
        listbox3.bind('<<ListboxSelect>>', on_select3)  
    
    # Update the previous selection
        global previous_selection
        previous_selection = listbox2.curselection()
        global button_frame1
        button_frame1 = tk.Frame(root)
        button_frame1.pack(side=tk.BOTTOM, pady=0)
        button777 = tk.Button(button_frame1, text="Update Info", command=update, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button777.pack(side=tk.LEFT, padx=10)


    def button3_click():
        forgetButtons()
        global frame
        frame = tk.Frame(root)
        login_label = tk.Label(frame, text="Your Fitness Classes", font=('Helvetica', '14'))
        login_label.pack(padx=0)
        login_label2 = tk.Label(frame, text="Your Private Sessions", font=('Helvetica', '14'))
        login_label3 = tk.Label(frame, text="Class Browser (Classes you are not in)", font=('Helvetica', '14'))
        frame.pack(padx=40, pady=20, fill=tk.BOTH, expand=True)
        listbox2 = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        listbox3 = tk.Listbox(frame, font=('Helvetica', '16'))
        #listbox3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        listbox2.insert(tk.END, "ClassID, ClassName, ClassDate, StartTime, EndTime, RoomNumber, Cost")
        #listbox3.insert(tk.END, "TODO")
        
        insertString = """
                    SELECT fc.ClassID, fc.ClassName, fc.ClassDate, fc.SessionTime, fc.EndTime, fc.RoomID, fc.Cost
                    FROM FitnessClass fc
                    JOIN ClassMembers cm ON fc.ClassID = cm.ClassID
                    WHERE cm.MemberID = {}
                    Order By fc.ClassDate, fc.SessionTime
                    """.format(userID)

        equip = SQL.StrictSelect(insertString)
        # Insert items into the Listbox
        if equip == []:
            listbox2.insert(tk.END, "")
            listbox2.insert(tk.END, "")
            listbox2.insert(tk.END, "No Registered Classes")

        for item in equip:
            listbox2.insert(tk.END, item)

        def addFClass():
            listbox2.delete(0, tk.END)
            listbox2.pack_forget()
            login_label.pack_forget()
            login_label3.pack(padx=0)
            listbox2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            listbox2.insert(tk.END, "Available Classes")
            listbox2.insert(tk.END, "")
            listbox2.insert(tk.END, "ClassID, ClassName, TrainerNumber, RoomNumber, ClassDate, StartTime, EndTime, Cost, Class Capacity")
            listbox2.insert(tk.END, "")
            insertString = """
                        SELECT fc.*
                        FROM FitnessClass fc
                        LEFT JOIN ClassMembers cm ON fc.ClassID = cm.ClassID AND cm.MemberID = {}
                        WHERE cm.MemberID IS NULL
                        Order By fc.ClassDate, fc.SessionTime
            """.format(userID)
            equip = SQL.StrictSelect(insertString)

            for item in equip:
                listbox2.insert(tk.END, item)

            def getClass():
                index = listbox2.curselection()
                selected_item = listbox2.get(index)
                temp = (str(selected_item).split(","))
                temp = temp[-2].replace("\'", "").replace(",", "").replace("$", "").replace(" ", "")
                print(temp)
                if((index) == (0,) or (index) == (1,) or (index) == (2,) or (index) == (3,) or selected_item == 'No Registered Classes' or selected_item ==''):
                    print("bad index")
                    return
                selected_item = str(selected_item).split(",")
                classID = selected_item[0].replace("(", "")
                insertString = """
                            SELECT 
                            fc.ClassID, fc.Capacity,
                            COUNT(cm.MemberID) AS RegisteredMembers
                        FROM 
                            FitnessClass fc
                        LEFT JOIN 
                            ClassMembers cm ON fc.ClassID = cm.ClassID
                        GROUP BY 
                            fc.ClassID, fc.ClassName, fc.Capacity
                        ORDER BY 
                            fc.ClassID;
                """
                if(SQL.getNumberOfMembers(insertString, classID)) == True:
                    SQL.addSomething("ClassMembers (ClassID, MemberID) VALUES ({}, {});".format(classID, userID))
                    messagebox.showinfo("Success!", "Successfully Registered")
                    SQL.UpdateSomething("Payment SET AmountOwed = AmountOwed + {} Where MemberID = {};".format(temp, userID))
                    returnButton()
                    button3_click()
                else:
                    messagebox.showinfo("Fail!", "Class is Full")   

            buttonAddClass.pack_forget()
            buttonLeaveClass.pack_forget()

            buttonJoinClass = tk.Button(frame, text="Join Class", command=getClass, height=2, width=20, font=('Helvetica', '16'), bg='#DA8441')
            buttonJoinClass.pack(side=tk.LEFT, padx=10)


        def withdrawFClass():
                def deleteClass():
                    index = listbox2.curselection()
                    selected_item = listbox2.get(index)
                    temp = (str(selected_item).split(","))
                    temp = temp[-1].replace("\'", "").replace(",", "").replace("$", "").replace(")", "").replace(" ", "")
                    if((index) == (0,) or selected_item == 'No Registered Classes' or selected_item ==''):
                        print("bad index")
                        return
                    selected_item = str(selected_item).split(",")
                    classID = selected_item[0].replace("(", "")
                    SQL.deleteSomething("ClassMembers WHERE ClassID = {} AND MemberID = {};".format(classID, userID))
                    SQL.UpdateSomething("Payment SET AmountOwed = AmountOwed - {} Where MemberID = {};".format(temp, userID))
                    returnButton()
                    button3_click()
                    messagebox.showinfo("Success!", "You are no longer apart of the class")


                buttonLeaveClass.pack_forget()

                buttonJoinClass = tk.Button(frame, text="Leave Class", command=deleteClass, height=2, width=20, font=('Helvetica', '16'), bg='#DA8441')
                buttonJoinClass.pack(side=tk.LEFT, padx=10)

        def viewPrivate():
            listbox3.delete(0, tk.END)
            insertString = """
                        SELECT ps.SessionID, ps.SessionDate, ps.SessionTime, ps.EndTime, ps.RoomID, ps.TrainerID, ps.Cost
                        FROM PrivateSession ps
                        WHERE ps.MemberID = {}
                        ORDER BY ps.SessionDate, ps.SessionTime;
            """.format(userID)
            login_label2.pack(padx=0)
            listbox3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            listbox3.insert(tk.END, "SessionID, SessionDate, SessionStart, SessionEnd, RoomNumber, TrainersID, Cost")
            listbox2.pack_forget()
            login_label.pack_forget()
            equip = SQL.StrictSelect(insertString)
            # Insert items into the Listbox
            for item in equip:
                listbox3.insert(tk.END, item)
            
            if equip == []:
                listbox3.insert(tk.END, "")
                listbox3.insert(tk.END, "")
                listbox3.insert(tk.END, "No Registered Sessions")
            button777.pack_forget()

            buttonLeaveClass.pack_forget()
            buttonAddClass.pack_forget()



            def withdrawPClass():
                def deleteClass():
                    index = listbox3.curselection()
                    selected_item = listbox3.get(index)
                    temp = (str(selected_item).split(","))
                    temp = temp[-1].replace("\'", "").replace(",", "").replace("$", "").replace(")", "").replace(" ", "")
                    if((index) == (0,) or selected_item == 'No Registered Sessions' or selected_item ==''):
                        print("bad index")
                        return
                    print(selected_item)
                    selected_item = str(selected_item).split(",")
                    classID = selected_item[0].replace("(", "")
                    SQL.deleteSomething("PrivateSession WHERE SessionID = {} AND MemberID = {};".format(classID, userID))
                    SQL.UpdateSomething("Payment SET AmountOwed = AmountOwed - {} Where MemberID = {};".format(temp, userID))
                    returnButton()
                    button3_click()
                    messagebox.showinfo("Success!", "You are no longer apart of that private session")


                buttonPLeaveClass.pack_forget()

                buttonJoinClass = tk.Button(frame, text="Leave Session", command=deleteClass, height=2, width=20, font=('Helvetica', '16'), bg='#DA8441')
                buttonJoinClass.pack(side=tk.LEFT, padx=10)

            def createPrivSesh():
                info = {0:"Date", 1:"Start Hours", 2:"Start Minutes", 3:"End Hours", 4:"End Minutes"}
                print("Creating Priv Sesh")
                login_label = tk.Label(frame, text="Enter the Date and Time to", font=('Helvetica', '14'))
                login_label = tk.Label(frame, text="Schedule a Priv Sesh (1pm is 13)", font=('Helvetica', '14'))
                login_label.pack()
                entries = []
                for i in range(5):
                    entry = tk.Entry(frame, font=('Helvetica', '16'), width=16)
                    entry.pack()  
                    entry.insert(0, info.get(i))   
                    entries.append(entry)
                newClass = []
                def dingl():
                    for i in range (5):
                        newClass.append(entries[i].get())
                    date = datetime.strptime(str(newClass[0]), "%Y-%m-%d").date() 
                    time1 = datetime.strptime(str(newClass[1] + " " + newClass[2] + " 00"), "%H %M %S").time()
                    time2 = datetime.strptime(str(newClass[3] + " " + newClass[4] + " 00"), "%H %M %S").time()
                    #10:30 to 12 is good on 2024-04-15
                    avail = MemberBackend.getAvailableTrainers(date, time1, time2)
                    for item in entries:
                        item.pack_forget()
                    login_label.pack_forget()
                    button8.pack_forget()
                    listbox3.delete(0, tk.END)
                    listbox3.insert(tk.END, "Available Trainers")
                    listbox3.insert(tk.END, "")
                    for i in avail:
                        listbox3.insert(tk.END, i)
                    
                    def selectTrainer():
                        index = listbox3.curselection()
                        selected_item = listbox3.get(index)
                        if selected_item == '':
                            return
                        trainerID = str(selected_item).split(",")
                        trainerID = (trainerID[0]).replace(",", "").replace("(", "")
                        trainerID = int(trainerID)
                        query = ""
                        query += "PrivateSession (TrainerID, MemberID, RoomID, SessionDate, SessionTime, EndTime, Cost) VALUES ({}, {}, 3, '{}', '{}', '{}', '100$');".format(trainerID, userID, date, time1, time2)
                        SQL.addSomething(query)
                        SQL.UpdateSomething("Payment SET AmountOwed = AmountOwed + 100 Where MemberID = {};".format(userID))
                        messagebox.showinfo("Success!", "Successfully Scheduled")
                        returnButton()
                    button9 = tk.Button(frame, text="Select Trainer", command=selectTrainer, height=1, width=20, font=('Helvetica', '12'), bg='#9389E5')
                    button9.pack(side=tk.LEFT, padx=5)

                button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
                button8.pack()
            buttonPLeaveClass = tk.Button(button_frame1, text="Withdraw From Session", command=withdrawPClass, height=2, width=20, font=('Helvetica', '16'), bg='#DA8441')
            buttonPLeaveClass.pack(side=tk.LEFT, padx=10)
            buttonPCreateClass = tk.Button(button_frame1, text="Schedule Priv Session", command=createPrivSesh, height=2, width=20, font=('Helvetica', '16'), bg='#DA8441')
            buttonPCreateClass.pack(side=tk.LEFT, padx=10)

        global button_frame1
        button_frame1 = tk.Frame(root)
        button_frame1.pack(side=tk.BOTTOM, pady=0)
        button777 = tk.Button(button_frame1, text="View Private Sessions", command=viewPrivate, height=2, width=20, font=('Helvetica', '16'), bg='#4AE957')
        button777.pack(side=tk.LEFT, padx=10)
        buttonAddClass = tk.Button(button_frame1, text="Add Class", command=addFClass, height=2, width=20, font=('Helvetica', '16'), bg='#41D9DA')
        buttonAddClass.pack(side=tk.LEFT, padx=10)
        buttonLeaveClass = tk.Button(button_frame1, text="Withdraw From Class", command=withdrawFClass, height=2, width=20, font=('Helvetica', '16'), bg='#DA8441')
        buttonLeaveClass.pack(side=tk.LEFT, padx=10)



    # Create the main window
    root = tk.Tk()
    root.title("Member Controls")
    root.geometry("1400x600")  # Width x Height
    login_label = tk.Label(root, text="Hello, {}".format(e), font=('Helvetica', '14'))
    login_label.pack(anchor='nw', padx=10)
    # Create and pack the buttons within the button frame

    def forgetButtons():
        button1.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        button5.pack(side=tk.LEFT, padx=10)

    def returnButton():
        button_frame1.destroy()
        button1.pack(side=tk.LEFT, padx=10)
        button2.pack(side=tk.LEFT, padx=10)
        button3.pack(side=tk.LEFT, padx=10)
        button5.pack_forget()
        frame.destroy()
        global updateCounter
        updateCounter = False

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=20)
    button1 = tk.Button(button_frame, text="Profile Management", command=button1_click, height=2, width=20, font=('Helvetica', '16'), bg='#89BAE5')
    button2 = tk.Button(button_frame, text="Dashboard Display", command=button2_click, height=2, width=30, font=('Helvetica', '16'), bg='#E59989')
    button3 = tk.Button(button_frame, text="Schedule Management", command=button3_click, height=2, width=20, font=('Helvetica', '16'), bg='#9389E5')
    button5 = tk.Button(button_frame, text="Return", command=returnButton, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')

    button1.pack(side=tk.LEFT, padx=10)
    button2.pack(side=tk.LEFT, padx=10)
    button3.pack(side=tk.LEFT, padx=10)


    # Start the Tkinter event loop
    root.mainloop()