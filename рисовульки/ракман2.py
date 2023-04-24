import tkinter as tk


def racaman_sequence(n):
    seq = [0]
    for i in range(1, n):
        prev = seq[i - 1]
        curr = prev - i
        if curr > 0 and curr not in seq:
            seq.append(curr)
        else:
            curr = prev + i
            seq.append(curr)
    return seq


def draw_arc(canvas, x1, y1, x2, y2, color):
    canvas.create_arc(x1, y1, x2, y2, start=-180, extent=180, fill=color)
    canvas.after(100)
    canvas.update()


def draw_arc1(canvas, x1, y1, x2, y2, color):
    canvas.create_arc(x1, y1, x2, y2, start=0, extent=180, fill=color)
    canvas.after(100)
    canvas.update()


def visualize_sequence(seq):
    max_val = max(seq)
    min_val = min(seq)
    range_val = max_val - min_val
    canvas_width = 1500
    canvas_height = 800
    x_scale = canvas_width / len(seq)
    y_scale = canvas_height / range_val
    root = tk.Tk()
    root.title('Visualization')
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()
    for i in range(len(seq)):
        size = 100 * (seq[i] - min_val) / range_val + 100
        if i % 2 == 0:
            color = 'grey'
        else:
            color = 'black'
        x1 = i * x_scale
        y1 = canvas_height / 2 - seq[i] * y_scale / 2
        x2 = x1 + size
        y2 = canvas_height / 2 + seq[i] * y_scale / 2
        draw_arc(canvas, x1, y1, x2, y2, color)
        draw_arc1(canvas, x1, y1, x2, y2, color)
    root.mainloop()


n = 20
racaman_seq = racaman_sequence(n)
visualize_sequence(racaman_seq)
