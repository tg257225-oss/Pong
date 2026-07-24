import turtle
import time
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

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("black")
pen1.penup()
pen1.hideturtle()


# box
btn1 = turtle.Turtle()
btn1.shape("square")
btn1.shapesize(stretch_wid=3, stretch_len=15)
btn1.penup()
btn1.speed(0)
btn1.color("white")

btn2 = turtle.Turtle()
btn2.shape("square")
btn2.shapesize(stretch_wid=3, stretch_len=15)
btn2.penup()
btn2.speed(0)
btn2.color("blue")

btn3 = turtle.Turtle()
btn3.shape("square")
btn3.shapesize(stretch_wid=3, stretch_len=15)
btn3.penup()
btn3.speed(0)
btn3.color("green")



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


def handle_click1(x, y):
    game_1_press()

def handle_click2(x, y):
    game_2_press()

game_state = "game1"

def draw_menu():
    window.bgcolor("#677087")
    global game_state
    game_state = "menu"
    pad_1.hideturtle()
    pad_2.hideturtle()
    ball.hideturtle()

    btn1.showturtle()
    btn2.showturtle()
    btn3.showturtle()

    pen.clear()
    pen1.clear()
    btn1.clearstamps()

    btn1.goto(0, 180)
    btn2.goto(0, 100)
    btn3.goto(0, 20)


    pen.goto(0,230)
    pen.write("PONG", align="center", font=("Lucida Sans", 30, "bold"))


    #pen1.goto(-200, 180)
    #pen1.write("Normal", align="center", font=("Lucida Sans", 20, "bold"))


    window.listen()
    window.onkeypress(game_1_press, "1")
    btn1.onclick(handle_click1)
    btn2.onclick(handle_click2)

def game_1_press():
    start_game_1()

def game_2_press():
    start_game_2()

def start_game_1():
    global game_state
    if game_state == "menu":
        game_state = "game1"
        pen.clear()
        pen1.clear()
        btn1.hideturtle()
        btn2.hideturtle()
        btn3.hideturtle()
        pad_1.showturtle()
        pad_2.showturtle()
        ball.showturtle()
        pen.goto(0, 230)
        pen.write("PLAYER 1: 0                                PLAYER 2: 0", align="center",
                  font=("Lucida Sans", 24, "bold"))
        pen.goto(0, 230)
        pen.write("Click 'E' to go back to the main menu.", align="center",
                  font=("Lucida Sans", 10, "normal"))


        window.listen()
        window.onkeypress(draw_menu, "e")

        window.onkeypress(press_w, "w")
        window.onkeyrelease(release_w, "w")

        window.onkeypress(press_s, "s")
        window.onkeyrelease(release_s, "s")

        window.onkeypress(press_up, "Up")
        window.onkeyrelease(release_up, "Up")

        window.onkeypress(press_down, "Down")
        window.onkeyrelease(release_down, "Down")

def start_game_2():
    global game_state
    if game_state == "menu":
        game_state = "game2"
        pen.clear()
        pen1.clear()
        btn1.hideturtle()
        btn2.hideturtle()
        btn3.hideturtle()
        pad_1.showturtle()
        pad_2.showturtle()
        ball.showturtle()
        pen.goto(0, 230)
        pen.write("PLAYER 1: 0                                PLAYER 2: 0", align="center",
                  font=("Lucida Sans", 24, "bold"))
        pen.goto(0, 230)
        pen.write("Click 'E' to go back to the main menu.", align="center",
                  font=("Lucida Sans", 10, "normal"))


        window.listen()
        window.onkeypress(draw_menu, "e")

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

draw_menu()
pad_move()

while True:
    time.sleep(1/240)
    window.update()
    if game_state == "game1":
        window.bgcolor("#b0afab")
        pad_1.shapesize(stretch_wid=5.5, stretch_len=1)
        pad_2.shapesize(stretch_wid=5.5, stretch_len=1)
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
            pen.write("Click 'E' to go back to the main menu.", align="center",
                      font=("Lucida Sans", 10, "normal"))

        if ball.xcor() < -435:
            ball.goto(0, 0)
            ball.dx *= -1
            scr_2 += 1
            pen.clear()
            ding.play()
            pen.write("PLAYER 1: {}                                PLAYER 2: {}".format(scr_1, scr_2), align="center",
                      font=("Lucida Sans", 24, "bold"))
            pen.write("Click 'E' to go back to the main menu.", align="center",
                      font=("Lucida Sans", 10, "normal"))

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

    if game_state == "game2":
        window.bgcolor("#46579e")
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        pad_2.shapesize(stretch_wid=8.5, stretch_len=1)
        pad_1.shapesize(stretch_wid=8.5, stretch_len=1)


        # check da border
        if ball.ycor() > 282:
            ball.sety(282)
            ball.dy *= -1.1
            sound.play()

        if ball.ycor() < -282:
            ball.sety(-282)
            ball.dy *= -1.1
            sound.play()

        if ball.xcor() > 435:
            ball.goto(0, 0)
            ball.dy = 1.2
            ball.dx = 1.2

            ball.dx *= -1
            scr_1 += 1
            pen.clear()
            ding.play()
            pen.write("PLAYER 1: {}                                PLAYER 2: {}".format(scr_1, scr_2), align="center",
                      font=("Lucida Sans", 24, "bold"))
            pen.write("Click 'E' to go back to the main menu.", align="center",
                      font=("Lucida Sans", 10, "normal"))

        if ball.xcor() < -435:
            ball.goto(0, 0)
            ball.dx = 1.2
            ball.dy = 1.2

            ball.dx *= -1
            scr_2 += 1
            pen.clear()
            ding.play()
            pen.write("PLAYER 1: {}                                PLAYER 2: {}".format(scr_1, scr_2), align="center",
                      font=("Lucida Sans", 24, "bold"))
            pen.write("Click 'E' to go back to the main menu.", align="center",
                      font=("Lucida Sans", 10, "normal"))

        if not pad_1.ycor() < 212:
            pad_1.sety(212)


        if not pad_1.ycor() > -212:
            pad_1.sety(-212)

        if not pad_2.ycor() < 212:
            pad_2.sety(212)

        if not pad_2.ycor() > -212:
            pad_2.sety(-212)

        # paddle ball collisions
        if (ball.xcor() > 390 and ball.xcor() < 400) and (
                ball.ycor() < pad_2.ycor() + 65 and ball.ycor() > pad_2.ycor() - 65):
            ball.setx(390)
            ball.dx *= -1.2
            sound.play()

        if (ball.xcor() < -390 and ball.xcor() > -400) and (
                ball.ycor() < pad_1.ycor() + 65 and ball.ycor() > pad_1.ycor() - 65):
            ball.setx(-390)
            ball.dx *= -1.2
            sound.play()

