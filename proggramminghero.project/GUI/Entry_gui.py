from tkinter import *

root_screen = Tk()


lbl = Label(root_screen, text="Name")

data = Entry(root_screen, bd=4)

lbl.grid(row=0, column=0)
data.grid(row=0, column=1)

root_screen.mainloop()
