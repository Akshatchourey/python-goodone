import turtle

b = turtle.Turtle()

f = b.forward
r = b.right
l = b.left

b.speed(70)
b.penup()
b.back(380)
b.pendown()
b.hideturtle()

f(380),r(90),f(380)
penup(),r(180),f(760),pendown(),l(90),f(360),l(90),f(360)
turtle.done()
