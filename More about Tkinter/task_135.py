# Задача_135

# Напишите простую программу, которая выводит раскрывающийся список, 
# содержащий названия нескольких цветов, и кнопку Click Me.
# Когда пользователь выбирает цвет из списка и нажимает кнопку, 
# цвет фона окна заменяется выбранным цветом. 
# 
# Чтобы задача была более интересной, попробуйте обойтись без использования инструкции if.
from tkinter import *

def click():
    colour = myColour.get()
    app.configure(background=colour)


app = Tk()
app.title('Цвета')
app.geometry('300x300')


myColour = StringVar(app)
myColour.set('Green')

colourList = OptionMenu(app, myColour, 'Yellow', 'Blue', 'Red', 'Purple', 'Orange', 'Black', 'Pink')
colourList.place(x = 50, y = 30, width=100, height=30)

clickButton = Button(text='Нажми меня', command=click)
clickButton.place(x = 150, y = 31, width = 100, height = 26)

app.mainloop()