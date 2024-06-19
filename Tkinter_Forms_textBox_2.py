from tkinter import *
#from PIL import Image, ImageTk

root = Tk()

# To set title and image on top
root.title('Learn labels,text box entry,scrollbar Tkinter with RS')
root.iconbitmap('rs1.ico')

# set size of window
root.geometry('1000x1000')

def getval():
    print(f"The value of username is {userval.get()}")
    print(passval.get())
    
def concession_getval():
    print("Form Submitted")

    print(f"{nameval.get(),phoneval.get(),genderval.get(),concessionval.get()}")

    with open("records.txt","a") as f:
        f.write(f"{nameval.get(),phoneval.get(),genderval.get(),concessionval.get()}\n")


'''
frame = Frame(root,width=400, height=400, bg="yellow", colormap="new")
frame.pack(side=LEFT,fill="y")
'''

user=Label(root,text="Username")
password=Label(root,text="password")
user.grid(row=0)
password.grid(row=1)

userval=StringVar()
passval=StringVar()

userentry=Entry(root,textvariable=userval)
passentry=Entry(root,textvariable=passval)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getval,fg="red").grid()


Label(root,text="Welcome to Python - Grade12",font="comicsansms 15 bold",pady=10).grid(row=6,column=6)
# Text widgets for the filling Form
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")

# Packing texts
name.grid(row=8,column=2)
phone.grid(row=9,column=2)
gender.grid(row=10,column=2)

# Variables to store entries
nameval=StringVar()
phoneval=StringVar()
genderval=StringVar()
concessionval=IntVar()

#  Creating Entries/text boxes for the Form and then packing of all text boxes
nameentry=Entry(root,textvariable=nameval)
phoneentry=Entry(root,textvariable=phoneval)
genderentry=Entry(root,textvariable=genderval)
          
nameentry.grid(row=8 ,column=3)   #   Packing entries 
phoneentry.grid(row=9 ,column=3)   #   Packing entries 
genderentry.grid(row=10 ,column=3)   #   Packing entries 

# Creating Checkbox & packing it
concession=Checkbutton(text="Do you want concession", variable=concessionval)
concession.grid(row=11,column=3)

# Create Button & packing it and assigning it a command
Button(text="Submit Values",command=concession_getval,fg="blue").grid(row=12,column=3)
'''

f1=Frame(root,bg="red",borderwidth=6)
f1.pack(side=LEFT)
'''

'''
# To show image in other way

image=Image.open("pnguin.png")
photo=ImageTk.PhotoImage(image)
lbl=Label(root,image=photo)
lbl.pack()
'''

'''
img = ImageTk.PhotoImage(Image.open("pnguin.png"))
lbl = Label(root,image = img)
lbl.pack()
'''

root.mainloop()
