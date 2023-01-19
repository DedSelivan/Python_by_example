import turtle

window = turtle.Screen()
window.setup(800, 600)

turtle.shape('turtle')


for i in range(3):
    turtle.fd(100)
    turtle.rt(-120)
turtle.hideturtle()
turtle.exitonclick()


