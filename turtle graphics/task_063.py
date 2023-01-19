# Задача_063

# Нарисуйте в один ряд три квадрата, разделенных промежутками. 
# Заполните их тремя разными цветами.

import turtle

turtle.color("red", "purple")
turtle.begin_fill()
for i in range(4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("red", "green")
turtle.begin_fill()
for i in range(4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("red", "yellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.exitonclick()
