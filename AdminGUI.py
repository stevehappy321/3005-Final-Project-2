import tkinter as tk
from tkinter import messagebox
import SQL

root = None
curFrame = None
button_frame1 = None
x=0
def Initialize(submit_callback):
    def button1_click():
        enable_login()
        messagebox.showinfo("Member Login", "You are now logging in as a Member")
        root.title("Member Login")
        button4.pack()
    
    def submit_click():
        # Retrieve the input from the text box
        user_input = login_entry.get()
        messagebox.showinfo("Input Received", f"Logging in as: {user_input}")
        submit_callback(user_input)
            

    def button2_click():
        enable_login()
        messagebox.showinfo("Trainer Login", "You are now logging in as a Trainer")
        root.title("Trainer Login")
        button4.pack()

    def button3_click():
        enable_login()
        messagebox.showinfo("Admin Login", "You are now logging in as a Admin")
        root.title("Admin Login")
        button4.pack()

    def Switch_login():
        login_label.pack_forget()
        login_entry.pack_forget()
        submit_button.pack_forget()
        root.title("Health Login")
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)
        button1.pack(side=tk.LEFT, padx=10)
        button2.pack(side=tk.LEFT, padx=10)
        button3.pack(side=tk.LEFT, padx=10)
        button4.pack_forget()
    
    def enable_login():
        login_label.pack()
        login_entry.pack()
        submit_button.pack()
        button1.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
    
    global root
    root = tk.Tk()
    root.title("Health Login")
    root.geometry("800x400")

    login_frame = tk.Frame(root)
    login_frame.pack(pady=50)

    login_label = tk.Label(login_frame, text="Enter First and Last Name", font=('Helvetica', '14'))
    login_label.pack()
    login_label.pack_forget()

    login_entry = tk.Entry(login_frame, font=('Helvetica', '14'), width=20)
    login_entry.pack()
    login_entry.pack_forget()

    submit_button = tk.Button(login_frame, text="Submit", command=submit_click, font=('Helvetica', '14'), bg='#A4A4A4')
    submit_button.pack()
    submit_button.pack_forget()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    button1 = tk.Button(button_frame, text="Member Login", command=button1_click, height=2, width=12, font=('Helvetica', '16'), bg='#89BAE5')
    button2 = tk.Button(button_frame, text="Trainer Login", command=button2_click, height=2, width=12, font=('Helvetica', '16'), bg='#E59989')
    button3 = tk.Button(button_frame, text="Admin Login", command=button3_click, height=2, width=12, font=('Helvetica', '16'), bg='#9389E5')
    button4 = tk.Button(button_frame, text="Switch Login", command=Switch_login, height=2, width=12, font=('Helvetica', '16'), bg='#7A2727')

    button1.pack(side=tk.LEFT, padx=10)
    button2.pack(side=tk.LEFT, padx=10)
    button3.pack(side=tk.LEFT, padx=10)

    root.mainloop()

def close_gui():
        global root
        if root:
            root.destroy()

def broadcast(boolean, message):
    global root
    if(boolean):
      messagebox.showinfo("Success!", message)   
    else:
        messagebox.showinfo("Error!", message)

def AdminPortal():
    print("Admin Portal")
    
    def button1_click():
        global frame

        frame = tk.Frame(root)
        frame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)

        listbox = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        equip = SQL.getAllSomething("Rooms")
        listbox.insert(tk.END, "RoomID, Room Name, Capacity, Room Purpose")
        # Insert items into the Listbox
        for item in equip:
            listbox.insert(tk.END, str(item))

        button1.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        button4.pack_forget()
        button5.pack(side=tk.LEFT, padx=10)

        def filter():
            global x
            if(x == 0):   
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("Rooms r WHERE NOT EXISTS (SELECT * FROM PrivateSession ps WHERE ps.RoomID = r.RoomID) AND NOT EXISTS (SELECT * FROM FitnessClass fc WHERE fc.RoomID = r.RoomID);")
                listbox.insert(tk.END, "RoomID, Name, Capacity, Type of Room")
                for item in equip:
                    listbox.insert(tk.END, str(item))
                x=x+1
            else:
                reset()
                x=0
        def reset():
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("Rooms")
                listbox.insert(tk.END, "RoomID, Name, Capacity, Type of Room")
                # Insert items into the Listbox
                for item in equip:
                    listbox.insert(tk.END, str(item))
        def addNew():
            login_label = tk.Label(frame, text="Enter Room Details (Seperate by commas and spaces *no brackets*)", font=('Helvetica', '14'))
            login_label.pack()
            login_entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
            login_entry.pack(padx=40)
            def dingl():
                user_input = login_entry.get()
                SQL.addSomething("Rooms (Name, Capacity, Type) VALUES ({});".format(user_input))
                reset()
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#7A2727')
            button8.pack()

        def delete():
            index = listbox.curselection()
            selected_item = listbox.get(index)
            desired = selected_item.split(",")
            SQL.deleteSomething("Rooms Where RoomID = {};".format(desired[0].replace("(", "")))
            reset()

        global button_frame1
        button_frame1 = tk.Frame(root)
        button_frame1.pack(side=tk.BOTTOM, pady=30)
        button6 = tk.Button(button_frame1, text="Filter By Un-Used", command=filter, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button6.pack(side=tk.LEFT, padx=10)
        button7 = tk.Button(button_frame1, text="Add New", command=addNew, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button7.pack(side=tk.LEFT, padx=10)
        button77 = tk.Button(button_frame1, text="Delete Selected", command=delete, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button77.pack(side=tk.LEFT, padx=10)
      
   

    def button2_click():
        global frame

        def filter():
            global x
            if(x == 0):   
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("Equipment ORDER BY Condition DESC;")
                listbox.insert(tk.END, "ItemID, Item Name, Item Category, Purchase Date, Condition, Room Location")
                for item in equip:
                    listbox.insert(tk.END, str(item))
                x=x+1
            else:
                reset()
                x=0
        def reset():
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("Equipment")
                listbox.insert(tk.END, "ItemID, Item Name, Item Category, Purchase Date, Condition, Room Location")
                # Insert items into the Listbox
                for item in equip:
                    listbox.insert(tk.END, str(item))
        def addNew():
            login_label = tk.Label(frame, text="Enter First and Last Name", font=('Helvetica', '14'))
            login_label.pack()
            login_entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
            login_entry.pack(padx=40)
            def dingl():
                user_input = login_entry.get()
                SQL.addSomething("Equipment (Name, Type, PurchaseDate, Condition, RoomID) VALUES ({});".format(user_input))
                reset()
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#7A2727')
            button8.pack()

        def delete():
            index = listbox.curselection()
            selected_item = listbox.get(index)
            desired = selected_item.split(",")
            SQL.deleteSomething("Equipment Where equipmentID = {};".format(desired[0].replace("(", "")))
            reset()

        global frame
        frame = tk.Frame(root)
        frame.pack(padx=100, pady=60, fill=tk.BOTH, expand=True)
        
        # Create the Scrollbar
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the Listbox and attach the Scrollbar
        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=('Helvetica', '16'))
        listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        global button_frame1
        button_frame1 = tk.Frame(root)
        button_frame1.pack(side=tk.BOTTOM, pady=30)
        button6 = tk.Button(button_frame1, text="Filter By Old", command=filter, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button6.pack(side=tk.LEFT, padx=10)
        button7 = tk.Button(button_frame1, text="Add New", command=addNew, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button7.pack(side=tk.LEFT, padx=10)
        button77 = tk.Button(button_frame1, text="Delete Selected", command=delete, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button77.pack(side=tk.LEFT, padx=10)
        
        scrollbar.config(command=listbox.yview)

        equip = SQL.getAllSomething("Equipment")
        listbox.insert(tk.END, "ItemID, Item Name, Item Category, Purchase Date, Condition, Room Location")
        # Insert items into the Listbox
        for item in equip:
            listbox.insert(tk.END, str(item))
        
        button1.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        button4.pack_forget()
        button5.pack(side=tk.LEFT, padx=10)

    def button3_click():
        global frame

        frame = tk.Frame(root)
        frame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)

        listbox = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        equip = SQL.getAllSomething("FitnessClass")
        listbox.insert(tk.END, "ClassID, Class Name, TrainerID, RoomID, ClassDate, SessionTime, Cost")
        # Insert items into the Listbox
        for item in equip:
            listbox.insert(tk.END, str(item).replace("datetime.date", ""))

        def filter():
            global x
            if(x == 0):   
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("FitnessClass ORDER BY ClassDate ASC;")
                listbox.insert(tk.END, "ClassID, Class Name, TrainerID, RoomID, ClassDate, SessionTime, Cost")
                for item in equip:
                    listbox.insert(tk.END, str(item).replace("datetime.date", ""))
                x=x+1
            else:
                reset()
                x=0
        def reset():
                listbox.delete(0, tk.END)
                equip = SQL.getAllSomething("FitnessClass")
                listbox.insert(tk.END, "ClassID, Class Name, TrainerID, RoomID, ClassDate, SessionTime, Cost")
                # Insert items into the Listbox
                for item in equip:
                    listbox.insert(tk.END, str(item).replace("datetime.date", ""))

        def addNew():
            login_label = tk.Label(frame, text="Enter Fitness Class Details", font=('Helvetica', '14'))
            login_label.pack()
            login_entry = tk.Entry(frame, font=('Helvetica', '14'), width=30)
            login_entry.pack(padx=40)
            def dingl():
                user_input = login_entry.get()
                SQL.addSomething("FitnessClass (ClassName, TrainerID, RoomID, ClassDate, SessionTime, Cost) VALUES ({});".format(user_input))
                reset()
                login_label.pack_forget()
                login_entry.pack_forget()
                button8.pack_forget()
                #removes text from textbox
                login_entry.delete(0, tk.END)
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#7A2727')
            button8.pack()

        def delete():
            index = listbox.curselection()
            selected_item = listbox.get(index)
            desired = selected_item.split(",")
            SQL.deleteSomething("FitnessClass Where lassID = {};".format(desired[0].replace("(", "")))
            reset()

        def update():
            login_label = tk.Label(frame, text="Enter Fitness Class Change", font=('Helvetica', '14'))
            login_label.pack()
            entries = []
            #Creates the fields to check
            info = {0:"ClassName", 1:"TrainerID", 2:"RoomID", 3:"ClassDate", 4:"SessionTime", 5:"Cost"}
            info2 = ["ClassName", "TrainerID", "RoomID", "ClassDate", "SessionTime", "Cost"]
            def dingl():
                newClass = []
                #gets the index from the box to be updated
                index = listbox.curselection()
                selected_item = listbox.get(index)
                desired = selected_item.split(",")
                #Checks the input boxes for changed values. If it finds it'll add to the newClass array
                for i in range(6):
                    if(entries[i].get() != info.get(i)):
                        print(entries[i].get())
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
            for i in range(6):
                string = str(info.get(i))
                entry = tk.Entry(frame, font=('Helvetica', '16'), width=16)
                entry.pack(pady=1)  
                entry.insert(0, string)  
                entries.append(entry)  
            button8 = tk.Button(frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#7A2727')
            button8.pack()
        

        global button_frame1
        button_frame1 = tk.Frame(root)
        button_frame1.pack(side=tk.BOTTOM, pady=30)
        button6 = tk.Button(button_frame1, text="Filter By Upcoming", command=filter, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button6.pack(side=tk.LEFT, padx=10)
        button7 = tk.Button(button_frame1, text="Add New", command=addNew, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button7.pack(side=tk.LEFT, padx=10)
        button77 = tk.Button(button_frame1, text="Delete Selected", command=delete, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button77.pack(side=tk.LEFT, padx=10)
        button777 = tk.Button(button_frame1, text="Update Selected", command=update, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
        button777.pack(side=tk.LEFT, padx=10)

        button1.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        button4.pack_forget()
        button5.pack(side=tk.LEFT, padx=10)

    def button4_click():
        print("button4")

    
    
    def returnButton():
        button1.pack(side=tk.LEFT, padx=10)
        button2.pack(side=tk.LEFT, padx=10)
        button3.pack(side=tk.LEFT, padx=10)
        button4.pack(side=tk.LEFT, padx=10)
        button5.pack_forget()
        frame.destroy()
        button_frame1.destroy()

    # Create the main window
    root = tk.Tk()
    root.title("Admin Controls")
    root.geometry("1400x600")  # Width x Height

    # Create and pack the buttons within the button frame
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=20)
    button1 = tk.Button(button_frame, text="Room Booking Mgmnt", command=button1_click, height=2, width=20, font=('Helvetica', '16'), bg='#89BAE5')
    button2 = tk.Button(button_frame, text="Equipment Maintenance Monitoring", command=button2_click, height=2, width=30, font=('Helvetica', '16'), bg='#E59989')
    button3 = tk.Button(button_frame, text="Class Schedule Updating", command=button3_click, height=2, width=20, font=('Helvetica', '16'), bg='#9389E5')
    button4 = tk.Button(button_frame, text="Billing and Payment Proccessing", command=button4_click, height=2, width=30, font=('Helvetica', '16'), bg='#7A2727')
    button5 = tk.Button(button_frame, text="Return", command=returnButton, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')

    button1.pack(side=tk.LEFT, padx=10)
    button2.pack(side=tk.LEFT, padx=10)
    button3.pack(side=tk.LEFT, padx=10)
    button4.pack(side=tk.LEFT, padx=10)

    # Start the Tkinter event loop
    root.mainloop()
