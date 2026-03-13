from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("300x400")

entry = Entry(root, width=20, font=('Arial', 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(num):
    entry.insert(END, num)

def clear():
    entry.delete(0, END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row, col = 1, 0
for b in buttons:
    if b == "C":
        Button(root, text=b, width=5, height=2, command=clear).grid(row=row, column=col)
    elif b == "=":
        Button(root, text=b, width=5, height=2, command=equal).grid(row=row, column=col)
    else:
        Button(root, text=b, width=5, height=2, command=lambda x=b: click(x)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
