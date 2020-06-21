from tkinter import *

def on_move(event):
    component=event.widget
    locx, locy = component.winfo_x(), component.winfo_y()
    w , h =master.winfo_width(),master.winfo_height()
    xpos=(locx+event.x)
    ypos=(locy+event.y)
    if xpos>=0 and ypos>=0 and w-abs(xpos)>=0 and h-abs(ypos)>=0 and xpos<=w-125 and ypos<=h-43:
       component.place(x=xpos,y=ypos)


master = Tk()
master.geometry("%dx%d+0+0" % (500,500))
msg = Label(master, text = "Move Me")
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<B1-Motion>',on_move)
msg.place(x=0,y=0)


mainloop()