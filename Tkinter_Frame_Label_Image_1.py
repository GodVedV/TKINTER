#Setting labels in Frames,Showing Image

from tkinter import *
from PIL import Image, ImageTk

root=Tk()

# To set title and image on top
root.title('LEARN Tkinter WITH RS- Setting labels in Frames: Tutorial 1')
root.iconbitmap('rs1.ico')


#set size of window - width x height
root.geometry("1366x968")

#width,height
#root.minsize(200,100)

root.maxsize(1800,1800)

def hello():
    print("Hello, How are you?")


# To add frames in Tkinter ***  Adding Frame1
#f1=Frame(root,width=300, height=800, bg="cyan",colormap="new")  OR
f1=Frame(root,bg="cyan",borderwidth=5,relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw",fill="y")

b1=Button(f1, fg="red",text="Print Now",command=hello)
b1.pack(side=LEFT,padx=2)

b2=Button(f1, fg="red",text="Submit")
b2.pack(side=LEFT,padx=2)

b3=Button(f1, fg="red",text="Download")
b3.pack(side=LEFT,padx=2)

l1=Label(f1,text="Project Tkinter")
l1.pack(side=TOP,pady=10)

# To add frames in Tkinter ***  Adding Frame2

f2=Frame(root,bg="deepskyblue",height=20,borderwidth=10,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l2=Label(f2,text="Welcome to Python", font="Helvetica 16 bold",fg="red",bg="olivedrab1",pady=10,borderwidth=10,relief=GROOVE)
l2.pack(pady=10,padx=20)

#Making label and packing label variable with pack()
# 2 ways to write font string and we can set relief=SUNKEN/RAISED/GROOVE/RIDGE
#important Pack options Anchor="nw"/"sw"/"ns"/"ne"  AND side=top/bottom/left/right

lbl2=Label(text=''' Now next step is label.\n
Now you will learn text and label.\n
''',bg="red",fg="white",font=("comicsansms",20,"bold"),borderwidth=5,relief=SUNKEN)
lbl2.pack(side=RIGHT,anchor='nw')

lbl3=Label(text="Write your Name",bg="pink",fg="black",font="comicsansms 15 bold",borderwidth=10,relief=RIDGE)
lbl3.pack(side=LEFT,anchor='ne')

lbl4=Label(text="Project Name",bg="pink",fg="black",font="comicsansms 15 bold",borderwidth=10,relief=RAISED)
lbl4.pack(side=BOTTOM,anchor='se')

#To show image and resizing it

'''
# To show image
photo=PhotoImage(file="pnguin.png")
lbl=Label(root,image= photo)
lbl.pack(side=RIGHT)
'''

'''
#To show image
disp = ImageTk.PhotoImage(Image.open("pnguin.png"))
lbl = Label(root,image = disp)
lbl.pack()
'''


img=Image.open("pnguin.png")    #Load the image
img1=img.resize((200,250))     #Resize the image : width and height
disp = ImageTk.PhotoImage(img1)  #Convert the image in Tkimage

#Display the image with Label
lbl = Label(root,image = disp)
lbl.pack(side=BOTTOM)


root.mainloop()
