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
pad_1.shapesize(stretch_wid=5, stretch_len=1)
pad_1.color("white")
pad_1.penup()
pad_1.goto(-400, 0)


turtle.up()
turtle.goto(-200,-150)
turtle.color("blue")
turtle.down()
turtle.dot()
turtle.fd(400)
turtle.dot()
# paddle numero 2


# ball


while True:
    window.update()