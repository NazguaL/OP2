from random import random
import tkinter as tk


WIDTH, HEIGHT = 480, 480
x1, y1 = WIDTH // 2, HEIGHT // 2

def create_rectangle():
    rectangle = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill='green')
    return rectangle

def move_rectangle():
    rnd = random()
    x = 0
    y = 0
    pos = canvas.coords(rectangle)
    if rnd > 0 and rnd < 0.25 and pos[0] <= 440:
        x = 30
    elif rnd > 0.25 and rnd < 0.5 and pos[0] >= 30:
        x = -30
    elif rnd > 0.5 and rnd < 0.75  and pos[1] <= 440:
        y = 30
    elif rnd > 0.75 and rnd < 1 and pos[1] >= 30:
        y = -30
    canvas.move(rectangle, x, y)
    root.after(5, move_rectangle)


root = tk.Tk()
tk.Button(root, text='start', command=move_rectangle).pack()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="cyan")
canvas.pack()

rectangle = create_rectangle()
root.mainloop()