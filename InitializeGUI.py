import tkinter as tk
from tkinter import messagebox

#Ryan

root = None
x=[]
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
        packButtons()
        button4.pack_forget()
    
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

    button1 = tk.Button(button_frame, text="Member Login", command=button1_click, height=2, width=12, font=('Helvetica', '16'), bg='#89BAE5')
    button2 = tk.Button(button_frame, text="Trainer Login", command=button2_click, height=2, width=12, font=('Helvetica', '16'), bg='#E59989')
    button3 = tk.Button(button_frame, text="Admin Login", command=button3_click, height=2, width=12, font=('Helvetica', '16'), bg='#9389E5')
    button4 = tk.Button(button_frame, text="Switch Login", command=Switch_login, height=2, width=12, font=('Helvetica', '16'), bg='#7A2727')

    global x
    x = [button1, button2, button3]

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