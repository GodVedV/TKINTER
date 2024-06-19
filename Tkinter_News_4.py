from tkinter import *
from PIL import  ImageTk, Image

def text_after_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text



root = Tk()
root.title("Learn Tkinter with RS- Articles")
root.iconbitmap('rs1.ico')
root.geometry("1200x1200")

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(text_after_100(text))

    image = Image.open(f"{i+1}.jpg")
#  *****   Resize these images   ******
    image = image.resize((130, 150))
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=100,bg="cyan",borderwidth=5,relief=SUNKEN)
Label(f0, text="News Articles", font="lucida 33 bold",bg="cyan").pack()
Label(f0, text="September 25, 2030", font="lucida 13 bold",bg="pink",padx=1200).pack()
f0.pack(fill="x")


f1 = Frame(root, width=900, height=200, pady=14,bg="yellow",borderwidth=5,relief=GROOVE)
Label(f1, text=texts[0], padx=25, pady=25).pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")


f2 = Frame(root, width=900, height=200, pady=14,bg="skyblue",borderwidth=5,relief=GROOVE)
Label(f2, text=texts[1], padx=40, pady=25).pack(side="right")
Label(f2, image=photos[1], anchor="e").pack()
f2.pack(anchor="w")


f3 = Frame(root, width=900, height=200, pady=14,bg="yellow",borderwidth=5,relief=GROOVE)
Label(f3, text=texts[2], padx=22, pady=25).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")


root.mainloop()
