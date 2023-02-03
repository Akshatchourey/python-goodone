import turtle
import random

print("Ready to to loose")
print("Left is computer where right is human")
print("This game is going to be conducted three parts and best of three will be chosen.")
print("chose any one from the three 1.stone, 2.paper and 3.seiser")
turtle.Screen().bgcolor("yellow")
    # ch1=computer, x=computer
    # ch2=human, y=human
y = turtle.Turtle()
x = turtle.Turtle()

def paper(w):
    f = w.forward
    r = w.right
    l = w.left
    x.color("black", 'white')
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
    f = w.forward
    r = w.right
    l = w.left
    x.color("black", 'white')
    l(45),f(340),r(90),f(24),r(90),f(80),r(45),f(15),l(45),f(249.3935),r(90),f(13.4)
    r(90),f(140),w.penup(),l(135),f(140),r(180),w.pendown(),f(340),l(90),f(24),l(90),f(80),l(45),f(15),r(45),f(249.3935),l(90),f(13.4)

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

    w.penup(), r(180), f(290), x.pendown()
    w.color("black", 'black')
    w.begin_fill()
    r(110), f(10), r(30), f(5), r(100), f(10), r(120), f(15)
    w.end_fill()

    w.penup(), r(180), f(100), x.pendown()
    w.color("black", 'black')
    w.begin_fill()
    r(110), f(10), r(30), f(5), r(120), f(10), r(100), f(15)
    w.end_fill()

    w.penup(), r(90), f(130), x.pendown()
    w.color("black", 'black')
    w.begin_fill()
    r(110), f(10), r(120), f(5), r(30), f(10), r(100), f(15)
    w.end_fill()

def reset():
    turtle.resetscreen()
    turtle.bgcolor("yellow")

    y.color("black", 'white')
    y.speed(70)
    y.hideturtle()

    x.speed(70)
    x.penup()
    x.back(380)
    x.pendown()
    x.hideturtle()


hum = com = 0
onPaper = {1:stone, 2:paper, 3:seiser}

for i in range(3):
    ch2 = int(input("enter your choice:"))  # y is human
    ch1 = random.randint(1, 3)   # x is computer
    reset()
    onPaper.get(ch2)(y)
    onPaper.get(ch1)(x)
    

    if ch1 == ch2:
        hum += 1
        com += 1
        print('tie')
    elif ch2 > ch1:
        if ch2-ch1 == 1:
            hum += 1
            print("win")
        else:
            com += 1
            print("loos")
    else:
        if ch1-ch2 == 1:
            com += 1
            print("loos")
        else:
            hum += 1
            print("win")

if hum == com:
    print("\nGame tied")
elif hum > com:
    print("\nYou finally won")
else:
    print("\nfinally Computer  wins")
turtle.done()
