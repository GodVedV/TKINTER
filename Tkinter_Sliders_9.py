from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")

# To set title and image on top
root.title('LEARN Tkinter WITH RS- Sliders in Tkinter')
root.iconbitmap('rs1.ico')

def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credited!", f"We have credited {myslider2.get()} dollars to your bank account")

# myslider = Scale(root, from_=0, to=100)
# myslider.pack()
Label(root, text="How many dollars do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
# myslider2.set(34)
myslider2.pack()


Button(root, text="Get dollars!", pady=10, command=getdollar).pack()

root.mainloop()
