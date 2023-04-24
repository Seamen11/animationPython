import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Функция, возвращающая координаты точек, описывающих сердце в полярных координатах
def heart(r, t):
    x = r * np.sin(t)
    y = r * np.cos(t)
    return (x ** 2 + y ** 2)**0.5 + np.sin(t * 5) * 0.2

# Определяем диапазон значений t и количество кадров
t = np.linspace(0, 2 * np.pi, 1000)
num_frames = 200

# Создаем фигуру и оси
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')
ax.set_ylim(0, 3)

# Определяем функцию анимации
def animate(i):
    ax.clear()
    ax.set_ylim(0, 3)
    ax.plot(t[:i], heart(1, t[:i]), 'r')
    ax.plot(t[:i], heart(-1, t[:i]), 'r')

# Создаем объект анимации
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Отображаем анимацию
plt.show()
