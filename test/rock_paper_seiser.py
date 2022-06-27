import turtle
import random

print('ready to to loose \nleft is computer where right is human\nchose any one from the  three 1.stone, 2.paper and 3.seaser')
ch2 = int(input("enter your choice:"))
turtle.Screen().bgcolor("yellow")

# ch1=computer , b=computer
# ch2=human , a=human

def paper(w):
    f = w.forward
    r = w.right
    l = w.left
    b.color("black", 'white')
    w.begin_fill()
    l(90), f(25), r(90), f(25), l(90), f(25), r(90), f(25), l(90), f(25)
    r(90), f(50), l(90), f(25), r(90), f(25), l(90), f(25), r(90), f(50)
    l(90), f(25), r(90), f(25), l(90), f(25),r(90), f(50), r(90), f(25)
    l(90), f(25), r(90), f(25), l(90), f(25), r(90), f(25), l(90), f(25)
    r(90), f(25), l(90), f(25), r(90), f(25), l(90), f(25), r(90), f(25)
    r(90), f(25), l(90), f(25), r(90), f(25), l(90), f(25), r(90), f(25)
    l(90), f(25), r(90), f(50), l(90), f(25), r(90), f(25), l(90), f(25)
    r(90), f(50), l(90), f(25), r(90), f(50), r(90), f(25), l(90), f(25)
    r(90), f(25), l(90), f(25), r(90), f(25), l(90), f(25),
    r(90), f(25), l(90), f(25), r(90), f(25), l(90), f(25), r(90)
    w.end_fill()

def seiser(w):
    pass

def stone(w):
    f = w.forward
    r = w.right
    l = w.left
    w.color("black", 'gray')
    w.begin_fill()
    l(90), f(33), r(90), f(34), l(90), f(34), r(90), f(34), l(90), f(34), r(90), f(34), l(90), f(34), r(90), f(34), l(
        90), f(34), r(90), f(103)
    r(90), f(34), l(90), f(34), r(90), f(34), l(90), f(34), r(90), f(34), l(90), f(34), r(90), f(34), l(90), f(34), r(
        90), f(33)
    r(90), f(29), l(90), f(12), r(90), f(29), l(90), f(12), r(90), f(29), l(90), f(12), r(90), f(29), l(90), f(12)
    r(90), f(87), r(90), f(16), l(90), f(58), r(90), f(16), l(90), f(58), r(90), f(16), l(90), f(58)
    w.end_fill()

    w.penup(), r(180), f(290), b.pendown()
    w.color("black", 'black')
    w.begin_fill()
    r(110), f(10), r(30), f(5), r(100), f(10), r(120), f(15)
    w.end_fill()

    w.penup(), r(180), f(100), b.pendown()
    w.color("black", 'black')
    w.begin_fill()
    r(110), f(10), r(30), f(5), r(120), f(10), r(100), f(15)
    w.end_fill()

    w.penup(), r(90), f(130), b.pendown()
    w.color("black", 'black')
    w.begin_fill()
    r(110), f(10), r(120), f(5), r(30), f(10), r(100), f(15)
    w.end_fill()


a = turtle.Turtle()
a.color("black", 'white')
a.speed(70)
a.hideturtle()

b = turtle.Turtle()
b.speed(70)
b.penup()
b.back(380)
b.pendown()
b.hideturtle()

ch1 = random.randint(1, 3)

if ch2 == 1:
    if ch1 == 2:
        paper(a), seiser(b)
        print('loos')
    elif ch1 == 1:
        paper(a),paper(b)
        print('tie')
    else:
        paper(a),stone(b)
        print('win')
if ch2 == 2:
    if ch1 == 3:
        seiser(a),stone(b)
        print('loos')
    elif ch1 == 2:
        seiser(a),seiser(b)
        print('tie')
    else:
        seiser(a),paper(b)
        print('win')
if ch2 == 3:
    if ch1 == 1:
        stone(a),paper(b)
        print('loos')
    elif ch1 == 3:
        stone(a),stone(b)
        print('tie')
    else:
        stone(a),seiser(b)
        print('win')

turtle.done()
