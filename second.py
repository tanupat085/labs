from tkinter import *
from tkinter import ttk

GUI = Tk()

GUI.title(' python GUI : aod shop ')

GUI.geometry('500x500')

#label และทางเข้า
LName = ttk.Label(GUI , text='Product Name')

LName.grid(row=0 , column=0)

#EName = tkk.Entry(GUI , textvariable=Name)

GUI.mainloop()