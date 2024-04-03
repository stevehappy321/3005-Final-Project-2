import tkinter as tk
import SQL

testValue = 'Jane Doe'
testValue2 = testValue.split(" ")
frame = None
globalBool = True
updateCounter = False
currentSelection = ""
def MemberPortal(e):
    e = testValue

    def button1_click():
        forgetButtons()
        global frame
        global updateCounter
        frame = tk.Frame(root)
        frame.pack(padx=150, pady=40, fill=tk.BOTH, expand=True)
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
            login_label = tk.Label(frame, text="Enter Personal Info Change", font=('Helvetica', '14'))
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
    button3 = tk.Button(button_frame, text="Schedule Management", command=quit, height=2, width=20, font=('Helvetica', '16'), bg='#9389E5')
    button5 = tk.Button(button_frame, text="Return", command=returnButton, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')

    button1.pack(side=tk.LEFT, padx=10)
    button2.pack(side=tk.LEFT, padx=10)
    button3.pack(side=tk.LEFT, padx=10)


    # Start the Tkinter event loop
    root.mainloop()