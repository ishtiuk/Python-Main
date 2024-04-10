from tkinter import *
from tkinter import font

root = Tk()


# course = Label(root, text="Programming Course", font=("ds-digital", 80), bg='black', fg='green')
# course.pack()

# butto = Button(root, text="Enroll Now", font=('ds-digital', 10), bd=10, bg='red', fg='blue')
# butto.pack()

# lang_list = Label(root, text="Languages", bd= 10, fg="lightgreen", bg="black", font=('ds-digital', 20))
# lang_list.pack()


python_button = Button(root, text="Python", bd=5, bg='black', fg='aqua')
cpp_button = Button(root, text="C++", bd=5, bg='black', fg='aqua')
java_button = Button(root, text="Java", bd=5, bg='black', fg='aqua')
javascript_button = Button(root, text="Javascript", bd=5, bg='black', fg='aqua')


python_button.grid(row=0, column=0)
cpp_button.grid(row=0, column=1)
java_button.grid(row=1, column=0)
javascript_button.grid(row=1, column=1)


root.geometry("300x200")
root.mainloop()