# Задача_066

# Нарисуйте восьмиугольник, все стороны которого окрашены в разные цвета 
# (случайно выбираемые из списка шести возможных цветов).

import random
import turtle

turtle.pensize(5)

for i in range(8):
    turtle.color(random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'brown']))
    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(45)
    turtle.end_fill()



turtle.hideturtle()
turtle.exitonclick()
    