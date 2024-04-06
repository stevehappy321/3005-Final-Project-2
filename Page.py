import tkinter as tk

import SQL
import Utility

class Page:
    def __init__(self, name, controls):
        self.name = name
        self.controlsArr = controls #dictonary of tkinter widgets belonging to this page
        self.childrenPages = [] #list of child pages

        self.isAttached = False

    def attach(self):
        for widget in self.controlsArr:
            widget.pack()

        self.isAttached = True

    def detach(self): #forget the controls

        for childPage in self.childrenPages: #detach child pages first
            childPage.detach()

        for widget in self.controlsArr:
            widget.pack_forget()

        self.isAttached = False

class PromptEntry:
    def __init__(self, masterFrame, prompt, callback):
        self.label = tk.Label(masterFrame, text=prompt, font=('Helvetica', '14'))
        self.entry = tk.Entry(masterFrame, font=('Helvetica', '14'), width=30)
        self.submit = tk.Button(masterFrame, text="Submit", command=callback, height=1, width=8, font=('Helvetica', '12'), bg='#9389E5')