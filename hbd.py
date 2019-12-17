import random
import tkinter as tk
from tkinter import *

def CreateWidgets():
	root.happyLabel = Label(root, text = "Happy", bg = "snow4", font=("Helvetica", 100))
	root.happyLabel.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 5)

	root.hbdLabel = Label(root, text = "Birthday!", bg = "snow4", font=("Helvetica", 100))
	root.hbdLabel.grid(row = 1, column = 0, columnspan = 4)

def happyWish():
	x = format(random.randint(1,255), '02x')
	y = format(random.randint(1,255), '02x')
	z = format(random.randint(1,255), '02x')

	color = "#"+str(x)+str(y)+str(z)

	root.happyLabel.config(fg=color)
	root.happyLabel.after(105, happyWish)

def hbdWish():
	x = random.randint(1,255)
	y = random.randint(1,255)
	z = random.randint(1,255)

	color = "#%02x%02x%02x" % (x, y, z)

	root.hbdLabel.config(fg=color)
	root.hbdLabel.after(100, hbdWish)

root = tk.Tk()
root.title("HBD Greetings")
root.config(background="snow4")
root.geometry('550x350')

CreateWidgets()

root.mainloop()