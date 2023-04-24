from tkinter import *
tk = Tk()
c = Canvas (tk, width= 2000, height=500)
c.pack()
c.create_rectangle(0,0,2000,100,fill='white')
c.create_rectangle(0,100,2000,200,fill='blue')
c.create_rectangle(0,200,2000,300,fill='red')
tk.mainloop()