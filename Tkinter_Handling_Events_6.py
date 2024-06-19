from tkinter import *

def RS(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

root = Tk()
root.title("Learn Tkinter with RS - Events in Tkinter")
root.iconbitmap('rs1.ico')
root.geometry("644x334")

widget = Button(root, text='Click me please')
widget.pack()

widget.bind('<Button-1>', RS)
widget.bind('<Double-1>', quit)

root.mainloop()
