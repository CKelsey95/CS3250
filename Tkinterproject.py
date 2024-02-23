import tkinter as tk
from tkinter import *
import random

#creating root window
root = tk.Tk()
root.title("Welcome to my Demo")
root.geometry('350x200')
lbl = Label(root, text = "This is not a test of the emergency response system")
lbl.grid()

# function to display text when
# button is clicked
def clicked():
    lbl.configure(text = "I just got clicked")
 
# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)

#runs GUI
root.mainloop()