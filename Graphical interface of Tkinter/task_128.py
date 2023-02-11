# Задача_128

# 1 километр = 0,6214 мили, а 1 миля = 1,6093 километра. 
# Напишите программу, которая преобразует километры в мили и наоборот.
from tkinter import *


def convKM():
    km = int(valueBox.get())
    kmAnswer['text'] = round((km * 1.6093), 2)
    valueBox.delete(0, END)
    valueBox.focus()


def convML():
    ml = int(valueBox.get())
    mlAnswer['text'] = round((ml * 0.6214), 2)
    valueBox.delete(0, END)
    valueBox.focus()

# Добавим окно и зададим параметры
root = Tk()
root.title('Convertio')
root.geometry('400x200')

# Добавим текстовый элемент и задаём параметры
valueText = Label(text='Введите значение для преобразования: ')
valueText.place(x=10, y=10)

# Добавим поле для ввода данных, задаём позицию и параметры
valueBox = Entry(text = 0)
valueBox.place(x=270, y=10, width=100, height=24)
valueBox['justify'] = 'center'
valueBox.focus()

# Добавим кнопку конвертирования из миль в км, зададим позицию и параметры
kmButton = Button(text='Перевести в КМ', command=convKM)
kmButton.place(x=10, y=50, width=180, height=25)

# Добавим кнопку конвертирования из км в мили, зададим позицию и параметры
mlButton = Button(text='Перевести в МИЛИ', command=convML)
mlButton.place(x=210, y=50, width=180, height=25)

# Добавляем поле вывода данных, задаём позицию и параметры
kmAnswer = Message(text=0, font=8)
kmAnswer.place(x=35, y=90, width=140, height=35)
kmAnswer['bg'] = 'gray'


# # Добавляем второе поле вывода данных, задаём позицию и параметры
mlAnswer = Message(text=0, font=8)
mlAnswer.place(x=235, y=90, width=140, height=35)
mlAnswer['bg'] = 'gray'



root.mainloop()