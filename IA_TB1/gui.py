from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35 , borderwidth=5)
e.pack()

def function(x):
    return pow(x, 2)

def myClick():
    current = int(e.get())
    t = function(current)
    u = str(t)
    myLabel = Label(root, text=u)
    myLabel.pack()


myButton = Button(root, text="Here to do the function", command=myClick)
myButton.pack()


root.mainloop()