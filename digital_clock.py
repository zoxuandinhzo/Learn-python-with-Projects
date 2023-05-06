from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")


def clock():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, clock)


label = Label(root, font=("digital-7", 80), background="black", foreground="cyan")
label.pack(anchor="center")
clock()
root.mainloop()
