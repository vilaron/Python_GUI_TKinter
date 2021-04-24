from tkinter import *
from Work_Break import *

root = Tk()
root.title("Separación de palabras")

root.geometry("1000x400")

e = Entry(root, width=35 , borderwidth=5)
e.pack()


dic = {'Jonathan', 'Villegas', 'Oscar', 'Burga', 'Marcelo', 'Martinez',
       'Inteligencia', 'Artificial', 'VillegasOscar', 'celoMar'}

def myClick():
    g = GeneticWordBreak(e.get(), dic).solve()
    myLabel = Label(root, text=g)
    myLabel.pack()


myButton = Button(root, text="Here to do the function")
myButton['command'] = myClick
myButton.pack()


root.mainloop()