import tkinter as tk

import TrainerBackend as Backend
import Page

frame = None;

def detach(): #hide all widgets on this page
    if frame == None:
         return
    
    widgets = frame.winfo_children()

    for widget in widgets:
          widget.pack_forget();

def searchMembers(masterFrame):
    def refresh():
        Backend.searchMemberByName(searchMembersPrompt.entry.get())

        
    searchMembersPrompt = Page.PromptEntry(
        masterFrame, 
        "Enter a member's name", 
        refresh
    )

    global frame
    frame = tk.Frame(masterFrame)
    frame.pack(padx=140, pady=60, fill=tk.BOTH, expand=True)

    #generate listbox
    listbox = tk.Listbox(frame, font=('Helvetica', '16'))
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    refresh();