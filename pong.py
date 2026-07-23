import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("#677087")
window.setup(width=900, height=600)
window.tracer(0)


# paddle numero 1
pad_1 = turtle.Turtle()
pad_1.speed(0)
pad_1.shape("square")
pad_1.shapesize(stretch_wid=5.5, stretch_len=1)
pad_1.color("white")
pad_1.penup()
pad_1.goto(-400, 0)

# paddle numero 2
pad_2 = turtle.Turtle()
pad_2.speed(0)
pad_2.shape("square")
pad_2.shapesize(stretch_wid=5.5, stretch_len=1)
pad_2.color("white")
pad_2.penup()
pad_2.goto(400, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.color("white")
ball.penup()
ball.goto(0, 0)

# move da paddles
def pad_1_up():
    y = pad_1.ycor()
    y+=15
    pad_1.sety(y)

def pad_1_down():
    y = pad_1.ycor()
    y-=15
    pad_1.sety(y)

def pad_2_up():
    y = pad_2.ycor()
    y += 15
    pad_2.sety(y)

def pad_2_down():
    y = pad_2.ycor()
    y-=15
    pad_2.sety(y)

window.listen()
window.onkeypress(pad_1_up, "w")
window.onkeypress(pad_1_down, "s")
window.onkeypress(pad_2_up, "Up")
window.onkeypress(pad_2_down, "Down")









while True:
    window.update()