import turtle
import time
import winsound
import pygame

pygame.mixer.init()
sound=pygame.mixer.Sound("Assets/sound.wav")
sound.set_volume(.04)
ding=pygame.mixer.Sound("Assets/ding.wav")
ding.set_volume(.04)


window = turtle.Screen()
window.title("Pong")
window.bgcolor("#677087")
window.setup(width=900, height=600)
window.cv._rootwindow.resizable(False, False)
window.tracer(0)

game_state = "game1"
# starting score
scr_1 = 0
scr_2 = 0


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


ball.dx = 1.2
ball.dy = 1.2
# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PLAYER 1: 0                                PLAYER 2: 0", align="center", font=("Lucida Sans", 24, "bold"))



# dict
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

# new paddle move function
def pad_move():
    if keys_pressed["w"]:
        y = pad_1.ycor()
        y += 6
        pad_1.sety(y)

    if keys_pressed["s"]:
        y = pad_1.ycor()
        y -= 6
        pad_1.sety(y)

    if keys_pressed["Up"]:
        y = pad_2.ycor()
        y += 6
        pad_2.sety(y)

    if keys_pressed["Down"]:
        y = pad_2.ycor()
        y -= 6
        pad_2.sety(y)

    window.ontimer(pad_move, 16)


pad_move()
while True:
    time.sleep(1/240)
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # check da border
    if ball.ycor() > 282:
        ball.sety(282)
        ball.dy *= -1
        sound.play()

    if ball.ycor() < -282:
        ball.sety(-282)
        ball.dy *= -1
        sound.play()

    if ball.xcor() > 435:
        ball.goto(0, 0)
        ball.dx *= -1
        scr_1 += 1
        pen.clear()
        ding.play()
        pen.write("PLAYER 1: {}                                PLAYER 2: {}".format(scr_1, scr_2), align="center",
                  font=("Lucida Sans", 24, "bold"))

    if ball.xcor() < -435:
        ball.goto(0, 0)
        ball.dx *= -1
        scr_2 += 1
        pen.clear()
        ding.play()
        pen.write("PLAYER 1: {}                                PLAYER 2: {}".format(scr_1, scr_2), align="center",
                  font=("Lucida Sans", 24, "bold"))

    if not pad_1.ycor() < 245:
        pad_1.sety(245)


    if not pad_1.ycor() > -245:
        pad_1.sety(-245)


    if not pad_2.ycor() < 245:
        pad_2.sety(245)


    if not pad_2.ycor() > -245:
        pad_2.sety(-245)


    # paddle ball collisions
    if (ball.xcor() > 390 and ball.xcor() < 400) and (ball.ycor() < pad_2.ycor()+ 65 and ball.ycor() > pad_2.ycor() - 65):
        ball.setx(390)
        ball.dx *=-1
        sound.play()

    if (ball.xcor() < -390 and ball.xcor() > -400) and (ball.ycor() < pad_1.ycor()+ 65 and ball.ycor() > pad_1.ycor() - 65):
        ball.setx(-390)
        ball.dx *=-1
        sound.play()

