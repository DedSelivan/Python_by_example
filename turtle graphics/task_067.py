# Задача_067 

# Нарисуйте следующий узор:

import turtle

window = turtle.Screen()
window.setup(500, 500)

for j in range(10):
    for i in range(8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.hideturtle()
turtle.exitonclick()