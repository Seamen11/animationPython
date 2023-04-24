from tkinter import *

window = Tk()
window.title('Работа с 5 заданием')

canvas = Canvas(window, width=600, height=600, bg="gray", cursor="pencil")
canvas.create_oval([400, 200], [400, 200], fill="pink")

canvas.pack()
window.mainloop()