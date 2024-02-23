import tkinter as tk
from tkinter import *
import random

#creating root window
root = tk.Tk()
root.title("Welcome to my Demo")
root.geometry('350x200')

# function to display text when
# button is clicked
def clicked1():
    lbl1.configure(text = "you rolled a (toadd)")
 
lbl1 = Label(root, text = "Six Sided Die")
lbl1.grid()

sixSidedImage = tk.PhotoImage(file="Images\six_sided_die.png")
btn1 = Button(root, image = sixSidedImage, command=clicked1)
btn1.grid(column=1, row=0)

#runs GUI
root.mainloop()