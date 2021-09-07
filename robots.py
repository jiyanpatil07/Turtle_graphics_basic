import turtle as t


def ract(hor,ver,col):
    t.pendown()
    t.pensize()
    t.color(col)
    t.begin_fill()
    for i in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed(1000)
t.bgcolor("blue")
t.goto(-100,-150)
ract(50,20,"black")
t.goto(-30,-150)
ract(50,20,"black")
t.goto(-25,-50)
ract(15,100,"grey")
t.goto(-70,-50)
ract(15,100,"grey")
t.goto(-90,100)
ract(100,150,"red")
t.goto(-150,70)
ract(60,15,"grey")
t.goto(-150,110)
ract(15,40,"grey")
t.goto(10,70)
ract(60,15,"grey")
t.goto(55,100)
ract(15,40,"grey")
t.goto(-50,120)
ract(15,20,"grey")
t.goto(-85,170)
ract(80,50,"red")
t.goto(-60,160)
ract(30,10,"white")
t.goto(-55,155)
ract(5,5,"black")
t.goto(-40,155)
ract(5,5,"black")
t.goto(-65,140)
ract(40,5,"black")
t.hideturtle()















t.Screen().exitonclick()