from tkinter import *
from tkinter import ttk

def hello():
    print('Hello world')
    print('Uncle Engineer')

#main    
GUI = Tk()

#title
GUI.title('Basic GUI')

#Setup paper
GUI.geometry('500x500')

#create butt
BT1 = ttk.Button(GUI, text = 'Hello' , command=hello)
BT1.place(x=250 , y=250)


GUI.mainloop()
 
