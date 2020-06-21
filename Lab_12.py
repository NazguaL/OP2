import tkinter as tk

root = tk.Tk()

canvas_width, canvas_height = 500, 500
x1, y1 = canvas_width // 2, canvas_height // 2


canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()


rectangle = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill='green')


def move_left(event):
    pos = canvas.coords(rectangle)
    if pos[0] > 0:
        event.widget.move(rectangle, -10, 0)

def move_right(event):
    pos = canvas.coords(rectangle)
    if pos[0] < 490:
        event.widget.move(rectangle, 10, 0)

def move_up(event):
    pos = canvas.coords(rectangle)
    if pos[1] > 0:
        event.widget.move(rectangle, 0, -10)

def move_down(event):
    pos = canvas.coords(rectangle)
    if pos[1] < 490:
        event.widget.move(rectangle, 0, 10)


canvas.bind("<Left>", move_left)
canvas.bind("<Right>", move_right)
canvas.bind("<Up>", move_up)
canvas.bind("<Down>", move_down)
canvas.focus_set()

root.mainloop()