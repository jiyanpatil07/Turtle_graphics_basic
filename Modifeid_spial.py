import turtle as t
import time as ti 
from itertools import cycle


colors= cycle(["red","blue","green","orange","pink","purple","grey"])


def circle(size,angel,forw,shape):
    # t.speed(100)
    t.pencolor(next(colors))    
    next_shape=" "    
    if shape=="circle":
        t.circle(size)
        next_shape="square"
    elif shape=="square":
        for i in range (4):
            t.forward(size * 2)
            t.left(90)
        next_shape="circle"
    t.right(angel) 
    t.forward(forw)  
    circle(size+5,angel+1,forw+1,next_shape)











t.bgcolor("black")
t.speed("fast")
t.pensize(4)
circle(30,0,1,"circle")

    # t.circle(5)
ti.sleep(2)

