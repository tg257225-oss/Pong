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
# paddle numero 2
pad_2 = turtle.Turtle()
pad_2.speed(0)
pad_2.shape("square")
pad_2.shapesize(stretch_wid=5, stretch_len=1)
pad_2.color("white")
pad_2.penup()
pad_2.goto(400, 0)


# ball


while True:
    window.update()