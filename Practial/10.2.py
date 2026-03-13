from tkinter import *
root = Tk()
root.title("Login Form")
root.geometry("300x200")

Label(root, text="Username:").pack(pady=5)
username = Entry(root, width=30)
username.pack()

Label(root, text="Password:").pack(pady=5)
password = Entry(root, width=30, show="*")
password.pack()
def login():
    user = username.get()
    pwd = password.get()
    if user == "diskhit" and pwd == "1234":
        result_label.config(text="Login Successful!", fg="green")
    else:
        result_label.config(text="Invalid Credentials!", fg="red")
Button(root, text="Login", command=login).pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
