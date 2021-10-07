import turtle
import random
from math import *

def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(0, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_point(p, r, g, b):
    turtle.goto(p)
    turtle.dot(5, r, g, b)


def fidget_spinner():

    # circle
    for i in range(0, 100, 5):
        t = i * pi / 50
        # center
        x = cos(t) * 60
        y = sin(t) * 60
        draw_point((x, y), 1, 1, 0)
        x = cos(t) * 40
        y = sin(t) * 40
        draw_point((x, y), 1, 1, 0)
        # one
        x = cos(t) * 40 + 180
        y = sin(t) * 40
        draw_point((x, y), 0, 0, 1)
        x = cos(t) * 20 + 180
        y = sin(t) * 20
        draw_point((x, y), 0, 0, 1)
        # two
        x = cos(t) * 40 - 80
        y = sin(t) * 40 + 150
        draw_point((x, y), 0, 0, 1)
        x = cos(t) * 20 - 80
        y = sin(t) * 20 + 150
        draw_point((x, y), 0, 0, 1)
        # three
        x = cos(t) * 40 - 80
        y = sin(t) * 40 - 150
        draw_point((x, y), 0, 0, 1)
        x = cos(t) * 20 - 80
        y = sin(t) * 20 - 150
        draw_point((x, y), 0, 0, 1)

    # body
    for i in range(0, 100, 1):
        t = i * pi / 50
        x = (2 + 0.75*cos(3*t)) * cos(t) * 100
        y = (2 + 0.75*cos(3*t)) * sin(t) * 100
        draw_point((x, y), 1, 0, 0)


prepare_turtle_canvas()

fidget_spinner()

turtle.done()