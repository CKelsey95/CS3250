import tkinter as tk
from tkinter import *
import random

#creating root window
root = tk.Tk()
root.title("Welcome to my diceroller")
root.geometry('500x500')


#configuration of Six Sided Die Roller
#command for 6 sided die
def clicked1():
    sixSidedRandom = str(random.randint(1,6))
    lbl1.configure(text = "you rolled a " + sixSidedRandom)
 
# label to describe 6 sided die and display number output 
lbl1 = Label(root, text = "Six Sided Die")
lbl1.grid(column=1, row=1)

#button for 6 sided die
sixSidedImage = tk.PhotoImage(file="Quiz 5\Images\six_sided_die.png")
btn1 = Button(root, image = sixSidedImage, height=100, width=100, command=clicked1)
btn1.grid(column=1, row=2)


#configuration of Ten Sided Die Roller
#command for 10 sided die roll
def clicked2():
    tenSidedRandom = str(random.randint(1,10))
    lbl2.configure(text = "you rolled a " + tenSidedRandom)

#label to describe 10 sided die and display number output
lbl2 = Label(root, text = "Ten Sided Die")
lbl2.grid(column=6, row=1)

# button for 10 sided die
tenSidedImage = tk.PhotoImage(file="Quiz 5\Images\Ten_sided_die.PNG")
btn2 = Button(root, image = tenSidedImage, height=100, width=100, command=clicked2)
btn2.grid(column=6, row=2)

# logic for user text input, controls which die is rolled
def display_text(entry_widget):
    input_text = entry_widget.get().lower()
    if input_text == "roll 6" or input_text == "roll six":
        clicked1()
    elif input_text == "roll 10" or input_text == "roll ten":
        clicked2()

#label to display user input
inputLabel = Label(root, text="valid argument: roll 6 or roll 10", font=("Courier 10 bold"))
inputLabel.grid(column=3,row=8)

#Entry widget
entry = Entry(root, width =40)
entry.focus_set()
entry.grid(column=3,row=10)

#Entry button
inputButton = Button(root, text = "Enter", width=10,command=lambda: display_text(entry))
inputButton.grid(column=3,row=11)

#allows user to hit Return key for input entry
entry.bind('<Return>', lambda event: display_text(entry))

#runs GUI
root.mainloop()