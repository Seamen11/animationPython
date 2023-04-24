import tkinter as tk

class Arc:
    def __init__(self, start, end, dir):
        self.start = start
        self.end = end
        self.dir = dir

    def show(self, canvas):
        diameter = abs(self.end - self.start)
        x = (self.end + self.start) / 2
        canvas.create_arc(x - diameter/2, -diameter/2, x + diameter/2, diameter/2, start=180*self.dir, extent=180, style="arc", width=2)

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



def visualize_sequence(seq):
    max_val = max(seq)
    min_val = min(seq)
    range_val = max_val - min_val
    canvas_width = 1500
    canvas_height = 300
    x_scale = canvas_width / len(seq)
    y_scale = canvas_height / range_val
    root = tk.Tk()
    root.title('Visualization')
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()
    numbers = [False] * (max_val+1)
    arcs = []
    biggest = 0
    index = 0
    count = 1
    numbers[index] = True
    for _ in range(len(seq)):
        next_index = index - count
        if next_index < 0 or numbers[next_index]:
            next_index = index + count
            numbers[next_index] = True
            a = Arc(index, next_index, count % 2)
            arcs.append(a)
            index = next_index
        if index > biggest:
            biggest = index
            count += 1
    for a in arcs:
        a.show(canvas)
    root.mainloop()

n = 20
racaman_seq = racaman_sequence(n)
visualize_sequence(racaman_seq)
