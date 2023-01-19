# Нарисуйте квадрат.

import turtle

window = turtle.Screen()
window.setup(600, 400)

turtle.shape("turtle")

for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.hideturtle()
turtle.exitonclick()




