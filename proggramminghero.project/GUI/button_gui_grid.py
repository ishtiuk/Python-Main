
from tkinter import *

root = Tk()

pyhon_button = Button(root, text="Pyhon", bd=3, bg='black', fg='aqua', font=('ds-digital', 30))
javascript_button = Button(root, text="Javascript", bd=3, bg='black', fg='aqua', font=('ds-digital', 30))
java_button = Button(root, text="Java", bd=3, bg='black', fg='aqua', font=('ds-digital', 30))
cpp_button = Button(root, text="C++", bd=3, bg='black', fg='aqua', font=('ds-digital', 30))

pyhon_button.grid(row=0, column=0)
javascript_button.grid(row=1, column=0)
cpp_button.grid(row=0, column=1)
java_button.grid(row=1, column=1)

root.mainloop()