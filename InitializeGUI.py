import tkinter as tk
from tkinter import messagebox
import SQL
#Ryan

root = None
x=[]
entries = []
registration = False
loginMethod = ''

def Initialize(submit_callback):
    #if the user selected Member login
    def button1_click():
        enableLogin()
        messagebox.showinfo("Member Login", "You are now logging in as a Member")
        root.title("Member Login")
        button4.pack()
        #indicates the user chose the Member login (adds Member: to the return variable)
        global loginMethod
        loginMethod = 'Member:'
    
    #sends the login info back to the main.py file
    def submitClick():
        # Retrieve the input from the text box
        user_input = login_entry.get()
        messagebox.showinfo("Input Received", f"Logging in as: {user_input}")
        global loginMethod
        loginMethod += user_input
        loginMethod += ":"
        submit_callback(loginMethod)
            
    #if Trainer login was clicked
    def button2_click():
        enableLogin()
        messagebox.showinfo("Trainer Login", "You are now logging in as a Trainer")
        root.title("Trainer Login")
        button4.pack()
        #indicates the user chose the Trainer login (adds Trainer: to the return variable)
        global loginMethod
        loginMethod = 'Trainer:'

    #if admin login was clicked
    def button3_click():
        enableLogin()
        messagebox.showinfo("Admin Login", "You are now logging in as a Admin")
        root.title("Admin Login")
        button4.pack()
        #indicates the user chose the admin login (adds Admin: to the return variable)
        global loginMethod
        loginMethod = 'Admin:'

    #this is for new registrations
    def button4_click():
        forgetButtons()
        root.title("Member Registration Login")
        button4.pack()
        info = {0:"FirstName", 1:"LastName", 2:"Address", 3:"City", 4:"PhoneNumber", 5:"Email"}
        info2 = ["FirstName", "LastName", "Address", "City", "PhoneNumber", "Email"]
        #when submit is clicked, below happens
        def dingl():
            #we loop through all boxes and check for changed values
            newClass = []
            for i in range(6):
                if(entries[i].get() != info.get(i)):
                    newClass.append(info.get(i))
                    newClass.append(entries[i].get())
                entries[i].pack_forget()
            login_label.pack_forget()
            button8.pack_forget()
            print(newClass)
            x=False
            inserts = '('
            fields = '('
            #for each element that was changed, create the query
            for i in newClass:
                if(i in info2 or x == True):
                    if(x==True):
                        inserts += '&' +i + '&, '
                        x= False
                    else:
                        fields += i + ', '
                        x=True

            fields += ') VALUES'
            inserts += ');'
            finalQuery = fields + ' ' + inserts
            final = finalQuery.replace(', )', ')')
            #add the member to the DB
            SQL.addSomething('Members {}'.format(final.replace('&', '\'')))
            userID = SQL.getMemberNumber("'{}' AND LastName = '{}';".format(newClass[1], newClass[3]))
            userID = str(userID).replace("[(", "").replace(",)]", "")
            userID = int(userID)
            #adds default values to the mebers profile
            SQL.addSomething("FitnessStuffs (MemberID, DistanceRunningGoal, FastestLapGoal, BenchPressGoal, SquatGoal, SwimmingDistanceGoal, CurrentRunDistance, CurrentFastestLap, CurrentBenchPress, CurrentSquat, CurrentSwimDistance) VALUES ({}, '0km', '0: 00 min/km', 0, 0, 0, '0km', '0:00 min/km', 0, 0, 0);".format(userID))
            SQL.addSomething("HealthStuffs (MemberID, MeasurementDate, Weight, BloodPressure, HeartRate, WeightGoal, HeartRateGoal) VALUES ({}, CURRENT_DATE, 00.00, '0/0', 0, 000.00, 0);".format(userID))
            SQL.addSomething("Payment (MemberID, PaymentDate, AmountPayed, AmountOwed, PaymentMethod) VALUES ({}, CURRENT_DATE, 0, 80, 'Debit');".format(userID))
            messagebox.showinfo("Input Received", f"Log in as: {newClass[1] + ' ' + newClass[3]}")
            #return
            button1_click()

        login_label = tk.Label(login_frame, text="Enter New Information", font=('Helvetica', '14'))
        login_label.pack()
        for i in range(6):
            string = str(info.get(i))
            entry = tk.Entry(login_frame, font=('Helvetica', '16'), width=25)
            entry.pack(pady=0)  
            entry.insert(0, string)  
            entries.append(entry)  
        button8 = tk.Button(login_frame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
        button8.pack()
        entries.append(button8)
        entries.append(login_label)
        global registration
        registration = True

    #returns to main menu and unpacks un-needed things
    def switchLogin():
        login_label.pack_forget()
        login_entry.pack_forget()
        submit_button.pack_forget()
        root.title("Health Login")
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)
        packButtons()
        button4.pack_forget()
        global registration
        if registration == True:
            for item in entries:
                item.pack_forget()
    
    #enables the login by packing and deleteing the nesecary elements
    def enableLogin():
        login_label.pack()
        login_entry.pack()
        login_entry.delete(0, tk.END)
        print(login_entry.get())
        submit_button.pack()
        forgetButtons()
    
    #create the window
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

    submit_button = tk.Button(login_frame, text="Submit", command=submitClick, font=('Helvetica', '14'), bg='#A4A4A4')
    submit_button.pack()
    submit_button.pack_forget()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    button1 = tk.Button(button_frame, text="Member Login", command=button1_click, height=2, width=12, font=('Helvetica', '16'), bg='#89BAE5')
    button2 = tk.Button(button_frame, text="Trainer Login", command=button2_click, height=2, width=12, font=('Helvetica', '16'), bg='#E59989')
    button3 = tk.Button(button_frame, text="Admin Login", command=button3_click, height=2, width=12, font=('Helvetica', '16'), bg='#9389E5')
    button4 = tk.Button(button_frame, text="Switch Login", command=switchLogin, height=2, width=12, font=('Helvetica', '16'), bg='#7A2727')
    button5 = tk.Button(button_frame, text="Member Registration", command=button4_click, height=2, width=18, font=('Helvetica', '16'), bg='#E2EC70')
    #this is so we can delete the buttons later using pack and forget all buttons
    global x
    x = [button1, button2, button3, button5]
    #packs buttons
    packButtons()

    #starts the window
    root.mainloop()

#forgets all buttons
def forgetButtons():
    for item in x:
        item.pack_forget()

#packs all buttons
def packButtons():
    for item in x:
        item.pack(side=tk.LEFT, padx=10)

#destroys the GUi from outside the class
def closeGUI():
        global root
        if root:
            root.destroy()

#creates a way to indicate success from main. message is passed in and based on the boolean show success! or Error!
def broadcast(boolean, message):
    global root
    if(boolean):
      messagebox.showinfo("Success!", message)   
    else:
        messagebox.showinfo("Error!", message)