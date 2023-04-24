from tkinter import *

root = Tk()
c = Canvas(root, width=600, height=600, bg="white")
c.pack()

point = c.create_oval(0, 50, 20, 70, fill='black')
oval = c.create_oval(200, 200, 400, 400, outline='black')

root.mainloop()
