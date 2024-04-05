import tkinter as tk
import datetime

import TrainerBackend as Backend
import Page

frame = None;

def detach(): #hide all widgets on this page
    if frame == None:
         return
    
    widgets = frame.winfo_children()

    for widget in widgets:
          widget.pack_forget();

def manageHours(trainerID, masterFrame):
    def refresh(): #refresh main listbox
            workingHours = Backend.getTrainerHours(trainerID)
            startTime = workingHours["startTime"]
            endTime = workingHours["endTime"]

            listbox.delete(0, tk.END)
            listbox.insert(tk.END, "CURRENT WORKING HOURS")
            listbox.insert(tk.END, "Starting time: " + startTime.strftime("%H:%M"))
            listbox.insert(tk.END, "Ending time: " + endTime.strftime("%H:%M"))
        
    def changeStartTime():
        def confirm():
            value = setStartTimePrompt.entry.get()
            timeArr = value.split(':') #returns array as [h, m]

            Backend.setTrainerStartTime(
                trainerID, 
                datetime.time(hour=timeArr[0], minute=timeArr[1]), 
            )

            setStartTimePrompt.label.pack_forget();
            setStartTimePrompt.entry.pack_forget();
            setStartTimePrompt.submit.pack_forget();

            refresh();
        
        setStartTimePrompt.label.pack();
        setStartTimePrompt.entry.pack(padx=40);
        setStartTimePrompt.submit.pack();

    def changeEndTime():
        def confirm():
            value = setEndTimePrompt.entry.get()
            timeArr = value.split(':')

            Backend.setTrainerEndTime(
                trainerID, 
                datetime.time(hour=timeArr[0], minute=timeArr[1]), 
            )

            setEndTimePrompt.label.pack_forget();
            setEndTimePrompt.entry.pack_forget();
            setEndTimePrompt.submit.pack_forget();

            refresh();
        
        setEndTimePrompt.label.pack();
        setEndTimePrompt.entry.pack(padx=40);
        setEndTimePrompt.submit.pack();
    
    global frame
    frame = tk.Frame(masterFrame)
    frame.pack(padx=0, pady=0, fill=tk.BOTH, expand=True)

    print("frame xy:", frame.winfo_x, frame.winfo_y)

    #generate listbox
    listbox = tk.Listbox(frame, font=('Helvetica', '16'))
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    refresh();

    setStartTimePrompt = Page.PromptEntry(frame, changeStartTime.confirm)
    setEndTimePrompt = Page.PromptEntry(frame, changeEndTime.confirm)

    changeStartTime_button = tk.Button(frame, text="Change Start Hours", command=changeStartTime, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
    changeEndTime_button = tk.Button(frame, text="Change End Hours", command=changeEndTime, height=2, width=20, font=('Helvetica', '16'), bg='#7A2727')
    changeStartTime_button.pack(side=tk.LEFT, padx=10)
    changeEndTime_button.pack(side=tk.LEFT, padx=10)