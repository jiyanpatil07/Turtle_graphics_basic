import turtle as t
import time as ti


def circle(a):
    while a<1000:
        t.speed(50)
        t.pencolor("red")
        
        t.circle(a)
        t.right(25)
        a=a+5
        circle(a)











t.bgcolor("black")
t.speed("fast")
t.pensize(4)
circle(50)

    # t.circle(5)
ti.sleep(2)





















t.exitonclick()