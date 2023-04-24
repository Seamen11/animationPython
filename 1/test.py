from math import cos
from tkinter import Tk, Canvas, BOTH

HEIGHT = 500
WIDTH = 500
STEP = 0.2
INTERVAL = 500

angle = 0
root = Tk()
root.geometry(str(HEIGHT) + "x" + str(WIDTH))
canvas = Canvas(root)
points = [0, HEIGHT, WIDTH / 2, 0, WIDTH, HEIGHT]
t = canvas.create_polygon(points, outline='#f11', fill='#1f1', width=2)
canvas.pack(fill=BOTH, expand=1)


def rotate(current_angle):
    angle = current_angle + STEP
    points[4] = 0.5 * WIDTH + 0.5 * WIDTH * cos(angle)
    points[0] = (WIDTH - (points[4] - 0.5 * WIDTH) * 2) / 2
    canvas.coords(t, points)
    root.after(INTERVAL, lambda: rotate(angle))


root.after(INTERVAL, lambda: rotate(angle))

root.mainloop()