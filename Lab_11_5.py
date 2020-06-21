from tkinter import *

WIDTH = 800
HEIGHT = 500
SIZE = 30
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="cyan")
canvas.pack()
color = 'green'


class Ball:
    def __init__(self, speedx, speedy):
        self.shape = canvas.create_oval(WIDTH // 2,  HEIGHT // 2, WIDTH // 2 + SIZE, HEIGHT // 2 + SIZE, fill=color)
        self.speedx = speedx
        self.speedy = speedy
        self.active = True
        self.move_active()

    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self):
        if self.active:
            self.ball_update()
            tk.after(30, self.move_active)

ball1 = Ball(3, 5)

tk.mainloop()