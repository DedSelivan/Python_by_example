# Задача_124

# Создайте окно, которое предлагает пользователю ввести имя. 
# Когда пользователь нажимает кнопку, в окне должно выводиться сообщение «Hello [имя]» с изменением цвета фона и цвета шрифта 
# текстовой области.

# импортируем библиотеку Tkinter
from tkinter import *

def click():
    name = myBox_1.get()
    textBox['bg'] = 'green'
    textBox['fg'] = 'red'
    textBox['text'] = f'Hello {name}!'

# Создаем окно, которое используем для вывода, добавляем заголовок и задаём размеры окна
window = Tk()
window.title('Именное окно')
window.geometry("600x400")

# Добавляем текстовый элемент и задаём позицию
lbl_1 = Label(text = 'Введите ваше имя: ')
lbl_1.place(x=40, y=20)

# Создаём текстовое поле для ввода данных и задаём позицию и размеры
myBox_1 = Entry(text = '')
myBox_1.place(x=170, y=20, width=170, height=25)
# Задаем выравнивание в текстовом поле и задаём фокус
myBox_1['justify'] = 'left'
myBox_1.focus()

# Создаем кнопку , задаём выполнение функции при нажатии. Задаём размеры и позицию кнопки
btn_1 = Button(text='Нажми меня', command=click )
btn_1.place(x=170, y=50, width=170, height=25)

textBox = Message(text='')
textBox.place(x=170, y=75, width = 170, height = 45)
textBox['bg'] = 'yellow'
textBox['fg'] = 'purple'


window.mainloop()