import tkinter as tk
import SQL

testValue = 'Ryan Mastin'
testValue2 = 'Ryan Mastin'.split(" ")
frame = None
def MemberPortal(e):
    e = testValue

    def button1_click():
        forgetButtons()
        global frame
        frame = tk.Frame(root)
        frame.pack(padx=40, pady=40, fill=tk.BOTH, expand=True)
        listbox = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        listbox2 = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        listbox3 = tk.Listbox(frame, font=('Helvetica', '16'))
        listbox3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        listbox.insert(tk.END, "                           Personal Info")
        listbox2.insert(tk.END, "                          Fitness Goals")
        listbox3.insert(tk.END, "                          Health Metrics")
        
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
                    listbox2.selection_clear(0, tk.END)
                    listbox3.selection_clear(0, tk.END)
                    for index in previous_selection:
                        listbox.selection_set(index)
                        listbox2.selection_set(index)
                        listbox3.selection_set(index)
            else:
                # No item is selected; this block can be useful for additional logic if needed
                pass

        listbox.bind('<<ListboxSelect>>', on_select)
        listbox2.bind('<<ListboxSelect>>', on_select)
        listbox3.bind('<<ListboxSelect>>', on_select)  
    
    # Update the previous selection
        global previous_selection
        previous_selection = listbox.curselection()

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
        button1.pack(side=tk.LEFT, padx=10)
        button2.pack(side=tk.LEFT, padx=10)
        button3.pack(side=tk.LEFT, padx=10)
        button5.pack_forget()
        frame.destroy()

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=20)
    button1 = tk.Button(button_frame, text="Profile Management", command=button1_click, height=2, width=20, font=('Helvetica', '16'), bg='#89BAE5')
    button2 = tk.Button(button_frame, text="Dashboard Display", command=quit, height=2, width=30, font=('Helvetica', '16'), bg='#E59989')
    button3 = tk.Button(button_frame, text="Schedule Management", command=quit, height=2, width=20, font=('Helvetica', '16'), bg='#9389E5')
    button5 = tk.Button(button_frame, text="Return", command=returnButton, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')

    button1.pack(side=tk.LEFT, padx=10)
    button2.pack(side=tk.LEFT, padx=10)
    button3.pack(side=tk.LEFT, padx=10)


    # Start the Tkinter event loop
    root.mainloop()