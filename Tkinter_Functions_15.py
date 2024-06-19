from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("Learn Tkinter with RS - Code of every GUI")
root.wm_iconbitmap("rs1.ico")
root.configure(background="skyblue")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command = root.destroy).pack()

root.mainloop()
