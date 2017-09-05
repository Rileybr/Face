# Smiley Face By Brandon Riley
# 8/31/17
# Draws a smiling face

import turtle


def draw_face():
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()


def draw_eye():
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.color("yellow")


def move_to_mouth():

    turtle.width(3)
    turtle.right(180)
    turtle.forward(110)
    turtle.left(90)
    turtle.pendown()


def draw_mouth():
    for x in range(45):
        turtle.color("black")
        turtle.forward(2)
        turtle.left(2)


def face_to_eye():
    turtle.penup()
    turtle.left(90)
    turtle.forward(140)
    turtle.left(90)
    turtle.forward(50)


def eye_to_eye():
    turtle.penup()
    turtle.right(180)
    turtle.forward(100)
    turtle.right(180)


def move_to_nose():
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(10)


def draw_nose():
    turtle.pendown()
    turtle.color("black")
    turtle.forward(20)
    turtle.width(3)
    turtle.right(90)
    turtle.forward(57.5)
    turtle.penup()

turtle.speed(100)

draw_face()

face_to_eye()

draw_eye()  # left eye

eye_to_eye()

draw_eye()  # right eye

move_to_nose()

draw_nose()

move_to_mouth()

draw_mouth()

turtle.exitonclick()
