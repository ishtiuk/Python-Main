
from tkinter import *


root = Tk()

def output():
    out["text"] = 'Enrolled Successfully'

course = Label(root, text="Programming Course")
out = Label(root)


butto = Button(root, text="Enroll Now", command=output)

course.pack()
butto.pack()
out.pack()


root.mainloop()
