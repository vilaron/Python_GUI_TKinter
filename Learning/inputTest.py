from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your name: ")

def myClick():
    h = e.get()
    myLabel = Label(root, text=h)
    myLabel.pack()

myButton = Button(root, text="Enter your Name" , command=myClick)
myButton.pack()


root.mainloop()