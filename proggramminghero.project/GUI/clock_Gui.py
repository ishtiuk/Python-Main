from tkinter import *
from tkinter import font
from datetime import datetime
import time

root = Tk()


def time_update():
    tm = datetime.now().strftime("%I: %M: %S %p")
    timing.config(text=tm)
    timing.after(900, time_update)


timing = Label(root, font=("DS-digital", 80), bg='black', fg='aqua', width=203)
timing.pack(anchor='center')
timing.destroy()

# exit_button = Button(root, text="Exit", font=("DS-digital", 20), bg='green', bd=2, fg='yellow', command=root.destroy)
# exit_button.pack()


root.geometry("527x95")
time_update()
root.mainloop()
