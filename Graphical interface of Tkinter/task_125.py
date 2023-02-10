# Задача_125

# Напишите программу, моделирующую бросок шестигранного кубика в настольной игре. 
# Когда пользователь нажимает кнопку, на экране должно выводиться случайное целое 
# число от 1 до 6 (включительно).

from tkinter import *
import random

def click():
    number = random.randint(1, 6)
    textBox['text'] = number

# Создаем окно, добавляем титульник и задаём размеры окна
root = Tk()
root.title('Моделирование броска шестигранного кубика')
root.geometry("150x150")

# Создаем область для вывода данных, задаём позицию и размеры
textBox = Message(text='')
textBox.place(x=60, y=10, width = 30, height = 25)
textBox['bg'] = 'gray'
textBox['fg'] = 'white'

# Добавляем кнопку, задаём позицию и размеры
myButton = Button(text='Нажми меня', command=click)
myButton.place(x=25, y=40, width = 100, height = 35)

root.mainloop()