import tkinter as tk
from tkinter import messagebox

#Ryan

root = None
x=[]
def Initialize(submit_callback):
    def memberLogin_click():
        enable_login()
        messagebox.showinfo("Member Login", "You are now logging in as a Member")
        root.title("Member Login")
        switchLoginButton.pack()
    
    def submit_click():
        # Retrieve the input from the text box
        user_input = login_entry.get()
        messagebox.showinfo("Input Received", f"Logging in as: {user_input}")
        submit_callback(user_input)
            

    def trainerLogin_click():
        enable_login()
        messagebox.showinfo("Trainer Login", "You are now logging in as a Trainer")
        root.title("Trainer Login")
        switchLoginButton.pack()

    def adminLogin_click():
        enable_login()
        messagebox.showinfo("Admin Login", "You are now logging in as a Admin")
        root.title("Admin Login")
        switchLoginButton.pack()

    def Switch_login():
        login_label.pack_forget()
        login_entry.pack_forget()
        submit_button.pack_forget()
        root.title("Health Login")
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)
        packButtons()
        switchLoginButton.pack_forget()
    
    def enable_login():
        login_label.pack()
        login_entry.pack()
        submit_button.pack()
        forgetButtons()
    
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

    memberLoginButton = tk.Button(
        button_frame, 
        text="Member Login", 
        command=memberLogin_click, 
        height=2, width=12, font=('Helvetica', '16'), bg='#89BAE5')
    trainerLoginButton = tk.Button(
        button_frame, 
        text="Trainer Login", 
        command=trainerLogin_click, 
        height=2, width=12, font=('Helvetica', '16'), bg='#E59989')
    adminLoginButton = tk.Button(
        button_frame, 
        text="Admin Login", 
        command=adminLogin_click, 
        height=2, width=12, font=('Helvetica', '16'), bg='#9389E5')
    switchLoginButton = tk.Button(
        button_frame, 
        text="Switch Login", 
        command=Switch_login, 
        height=2, width=12, font=('Helvetica', '16'), bg='#7A2727')

    global x
    x = [memberLoginButton, trainerLoginButton, adminLoginButton]

    packButtons()

    root.mainloop()

def forgetButtons():
    for item in x:
        item.pack_forget()

def packButtons():
    for item in x:
        item.pack(side=tk.LEFT, padx=10)

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