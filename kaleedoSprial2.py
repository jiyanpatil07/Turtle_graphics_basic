import turtle as t
import time as ti 
from itertools import cycle


colors= cycle(["red","blue","green","orange","pink","purple","grey"])


def circle(size,angel,forw):
    # t.speed(100)
    t.pencolor(next(colors))        
    t.circle(size)
    t.right(angel) 
    t.forward(forw)  
    circle(size+5,angel+1,forw+1)











t.bgcolor("black")
t.speed("fast")
t.pensize(4)
circle(30,0,1)

    # t.circle(5)
ti.sleep(2)

