import turtle

turtle.speed(8)
turtle.penup()
turtle.goto(-400, 300)
turtle.pendown()

count = 6
while count > 0:
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.backward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    count -= 1

turtle.penup()
turtle.goto(-400,300)
turtle.right(90)
turtle.pendown()

count = 6
while count > 0:
    turtle.forward(500)
    turtle.penup()
    turtle.backward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    count -= 1

turtle.exitonclick()
