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

keys_pressed = {
    "w": False,
    "s": False,
    "Up": False,
    "Down": False
}

def press_w():
    keys_pressed["w"] = True
def release_w():
    keys_pressed["w"] = False

def press_s():
    keys_pressed["s"] = True
def release_s():
    keys_pressed["s"] = False

def press_up():
    keys_pressed["Up"] = True
def release_up():
    keys_pressed["Up"] = False

def press_down():
    keys_pressed["Down"] = True
def release_down():
    keys_pressed["Down"] = False

window.listen()
window.onkeypress(press_w, "w")
window.onkeyrelease(release_w, "w")

window.onkeypress(press_s, "s")
window.onkeyrelease(release_s, "s")

window.onkeypress(press_up, "Up")
window.onkeyrelease(release_up, "Up")

window.onkeypress(press_down, "Down")
window.onkeyrelease(release_down, "Down")

def pad_move():
    if keys_pressed["w"]:
        y = pad_1.ycor()
        y += 5
        pad_1.sety(y)

    if keys_pressed["s"]:
        y = pad_1.ycor()
        y -= 5
        pad_1.sety(y)




    window.ontimer(pad_move, 16)


pad_move()
while True:
    window.update()