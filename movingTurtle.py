import turtle as t
import random as rd
# forw=rd.randint(150,300)
# angle=rd.randint(0,1800)

def inside_window():
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    (x,y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside

def move():
    if inside_window():
        print("if")
        t.fillcolor("green")
        angle=rd.randint(0,180)
        t.right(angle)
        forw=rd.randint(150,300)
        t.forward(200)
        
        #   print("if")
        #     angle=rd.randint(0,180)
        #     t.right(angle)
        #     # forw=rd.randint(150,300)
        #     t.forward(200)

          

       
    else:
        print("else")
        t.fillcolor("white") 
        t.backward(200)  


t.shape("turtle")
t.fillcolor("green")
t.bgcolor("black")
t.speed(1)
t.pensize(2)


while True:
    move()

# t.Screen().exitonclick()