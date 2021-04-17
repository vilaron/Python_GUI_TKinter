from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look ! I click a button!!", fg="white" , bg="Black" )
    myLabel.pack()

myButton = Button(root, text="Click Here" , command=myClick , fg="white" , bg="Black" )
myButton.pack()


root.mainloop()