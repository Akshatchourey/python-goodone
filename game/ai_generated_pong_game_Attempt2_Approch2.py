import turtle

# Screen setup
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("white")
sc.setup(width=900, height=550)

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Ball
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Moving the paddles
def paddleaup():
    y = left_pad.ycor()
    y += 35
    left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    y -= 35
    left_pad.sety(y)

def paddlebup():
    y = right_pad.ycor()
    y += 35
    right_pad.sety(y)

def paddlebdown():
    y = right_pad.ycor()
    y -= 35
    right_pad.sety(y)

sc.listen()
sc.onkeypress(paddleaup, "c")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup, "n")
sc.onkeypress(paddlebdown, "m")

while True:
    sc.update()
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
