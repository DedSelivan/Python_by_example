# Задача_063

# Нарисуйте круг

import turtle

window = turtle.Screen()
window.setup(500, 500)

for i in range(360):
    turtle.forward(1)
    turtle.right(1)
turtle.hideturtle()
turtle.exitonclick()