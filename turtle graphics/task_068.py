# Задача_068

# Нарисуйте узор, который меняется при каждом запуске программы. 
# Используйте функцию random для выбора количества линий, 
# длины каждой линии и каждого угла поворота.

import random
import turtle

for i in range(random.randint(5,30)):
    turtle.forward(random.randrange(40, 100, 5))
    turtle.right(random.randrange(5, 360, 5))

turtle.hideturtle()
turtle.exitonclick()