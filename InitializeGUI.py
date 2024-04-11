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
    def button1Click():
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
        userInput = loginEntry.get()
        messagebox.showinfo("Input Received", f"Logging in as: {userInput}")
        global loginMethod
        loginMethod += userInput
        loginMethod += ":"
        submit_callback(loginMethod)
            
    #if Trainer login was clicked
    def button2Click():
        enableLogin()
        messagebox.showinfo("Trainer Login", "You are now logging in as a Trainer")
        root.title("Trainer Login")
        button4.pack()
        #indicates the user chose the Trainer login (adds Trainer: to the return variable)
        global loginMethod
        loginMethod = 'Trainer:'

    #if admin login was clicked
    def button3Click():
        enableLogin()
        messagebox.showinfo("Admin Login", "You are now logging in as a Admin")
        root.title("Admin Login")
        button4.pack()
        #indicates the user chose the admin login (adds Admin: to the return variable)
        global loginMethod
        loginMethod = 'Admin:'

    #this is for new registrations
    def button4Click():
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
            loginLabel.pack_forget()
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
            SQL.addSomething("FitnessStuffs (MemberID, MeasurementDate, DistanceRunningGoal, FastestLapGoal, BenchPressGoal, SquatGoal, SwimmingDistanceGoal, CurrentRunDistance, CurrentFastestLap, CurrentBenchPress, CurrentSquat, CurrentSwimDistance) VALUES ({}, CURRENT_DATE, '0km', '0: 00 min/km', 0, 0, 0, '0km', '0:00 min/km', 0, 0, 0);".format(userID))
            SQL.addSomething("HealthStuffs (MemberID, MeasurementDate, Weight, BloodPressure, HeartRate, WeightGoal, HeartRateGoal, BloodPressureGoal) VALUES ({}, CURRENT_DATE, 00.00, '0/0', 0, 000.00, 0, '0/0');".format(userID))
            SQL.addSomething("Payment (MemberID, PaymentDate, AmountPayed, AmountOwed, PaymentMethod) VALUES ({}, CURRENT_DATE, 0, 80, 'Debit');".format(userID))
            messagebox.showinfo("Input Received", f"Log in as: {newClass[1] + ' ' + newClass[3]}")
            #return
            button1Click()

        loginLabel = tk.Label(loginFrame, text="Enter New Information", font=('Helvetica', '14'))
        loginLabel.pack()
        for i in range(6):
            string = str(info.get(i))
            entry = tk.Entry(loginFrame, font=('Helvetica', '15'), width=25)
            entry.pack(pady=0)  
            entry.insert(0, string)  
            entries.append(entry)  
        button8 = tk.Button(loginFrame, text="Submit", command=dingl, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')
        button8.pack()
        entries.append(button8)
        entries.append(loginLabel)
        global registration
        registration = True

    #returns to main menu and unpacks un-needed things
    def switchLogin():
        loginLabel.pack_forget()
        loginEntry.pack_forget()
        submitButton.pack_forget()
        root.title("Health Login")
        buttonFrame = tk.Frame(root)
        buttonFrame.pack(pady=20)
        packButtons()
        button4.pack_forget()
        global registration
        if registration == True:
            for item in entries:
                item.pack_forget()
    
    #enables the login by packing and deleteing the nesecary elements
    def enableLogin():
        loginLabel.pack()
        loginEntry.pack()
        loginEntry.delete(0, tk.END)
        print(loginEntry.get())
        submitButton.pack()
        forgetButtons()
    
    #create the window
    global root
    root = tk.Tk()
    root.title("HealthClub Login")
    root.geometry("800x400")

    loginFrame = tk.Frame(root)
    loginFrame.pack(pady=50)

    loginLabel = tk.Label(loginFrame, text="Enter First and Last Name", font=('Helvetica', '14'))
    loginLabel.pack()
    loginLabel.pack_forget()

    loginEntry = tk.Entry(loginFrame, font=('Helvetica', '14'), width=20)
    loginEntry.pack()
    loginEntry.pack_forget()

    submitButton = tk.Button(loginFrame, text="Submit", command=submitClick, font=('Helvetica', '14'), bg='#A4A4A4')
    submitButton.pack()
    submitButton.pack_forget()

    buttonFrame = tk.Frame(root)
    buttonFrame.pack(pady=20)

    button1 = tk.Button(buttonFrame, text="Member Login", command=button1Click, height=2, width=12, font=('Helvetica', '15'), bg='#89BAE5')
    button2 = tk.Button(buttonFrame, text="Trainer Login", command=button2Click, height=2, width=12, font=('Helvetica', '15'), bg='#E59989')
    button3 = tk.Button(buttonFrame, text="Admin Login", command=button3Click, height=2, width=12, font=('Helvetica', '15'), bg='#9389E5')
    button4 = tk.Button(buttonFrame, text="Switch Login", command=switchLogin, height=2, width=12, font=('Helvetica', '15'), bg='#7A2727')
    button5 = tk.Button(buttonFrame, text="Member Registration", command=button4Click, height=2, width=18, font=('Helvetica', '15'), bg='#E2EC70')
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