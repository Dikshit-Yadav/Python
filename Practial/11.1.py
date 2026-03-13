from tkinter import *

root = Tk()
root.title("Lab 11 - Tkinter Example")
root.geometry("300x200")

label = Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)

root.mainloop()
