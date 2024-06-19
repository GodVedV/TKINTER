'''
Python Tkinter-MessageBox module is used to display the message boxes in the python applications.
This module provides a number of functions that a user can use to display an appropriate message.
Some of these functions are showinfo, askquestion, showwarning, showerror, askokcancel, askyesno, and askretrycancel.
'''

from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("733x566")
# To set title and image on top
root.title('LEARN Tkinter WITH RS- Message Box')
root.iconbitmap('rs1.ico')

def myfunc():
    print("Learn Chapters-1 to 5 for Class Test tomorrow")

def help():
    print("I will help you")
    tmsg.showinfo("Help", "RS will help you with this gui")

def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience Good?", "You used this gui.. Was your experience Good?")
    if value == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)

def game():
    ans = tmsg.askretrycancel("Paly Games", "Sorry no Internet, You can't play")
    if ans:
        print("Don't Retry, It is better to study your books")

    else:
        print("Very Good, You pressed Cancel and saved your time")


mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)


m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label = "Help", command=help)
m3.add_command(label = "Rate us", command=rate)
m3.add_command(label = "Play Game", command=game)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)
root.mainloop()
