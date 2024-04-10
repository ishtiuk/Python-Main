
from tkinter import * 
from PIL import Image, ImageTk


root = Tk()

image_gogle = Image.open('google_PNG102344.png')
image_serch = Image.open('resizedImage (1).png')

img1 = ImageTk.PhotoImage(image_gogle)
img2 = ImageTk.PhotoImage(image_serch)

show = Label(root, image=img1)
show2 = Button(root, image=img2, height=20, width=50)
lbl = Label(root, text="serach bar:", font='calibri')
inp = Entry(root, bd=3, width=50)

show.grid(row=0, column=1)
lbl.grid(row=1, column=0)
inp.grid(row=1, column=1)
show2.grid(row=1, column=2)

root.mainloop()