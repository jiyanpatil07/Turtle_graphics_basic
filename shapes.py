import turtle as t
t.pendown()
t.penup()
t.goto(-250,250)
t.pendown()
# t.forward(100)
# t.pendown()
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.Screen().exitonclick()

# for i in range (1,5):
#     t.forward(200)
#     t.right(90)

t.penup()

t.goto(-100,100)
t.pendown()
t.color("red")
# t.circle(250)
# t.circle(260)
# t.circle(299)

t.color("blue")
t.speed(5)
# for i in range(10,200):
#     t.circle(i)
t.pensize(1)
t.speed(100)
# t.bgcolor("green")
t.fillcolor("green")
t.begin_fill()
for i in range(1,200):
    # t.f
    t.circle(i+90)
    t.left(150)

t.end_fill()

t.speed(1)
t.goto(200,200)

t.Screen().exitonclick()