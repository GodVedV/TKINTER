#Drawing Lines,rectangle and oval using widgets
from tkinter import *
root=Tk()

# To set title and image on top
root.title('LEARN Tkinter WITH RS- Drawing Lines,rectangle and oval')
root.iconbitmap('rs1.ico')

canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()


# The line draws from the point x1,y1 to x2,y2
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="blue")

# To draw rectangle in widget, but it takes parameters like: co-ordinates of top left and bottom right
can_widget.create_rectangle(3,5,700,300,fill="yellow")
can_widget.create_text(200,200,text="RECTANGLE",font="lucida 12 bold",fill="RED")
can_widget.create_oval(344,233,244,455)


root.mainloop()
