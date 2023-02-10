# Задача_126

# Напишите программу, которая предлагает пользователю ввести число в текстовом поле.
# Когда пользователь нажимает кнопку, это число прибавляется к накапливаемой сумме и выводится в другом поле. 
# Ввод может повторяться сколько угодно раз на усмотрение пользователя, при этом вводимые данные будут прибавляться к сумме.
# В окне должна присутствовать еще одна кнопка, которая обнуляет накапливаемую сумму и стирает содержимое исходного поля, 
# чтобы пользователь мог начать ввод заново.

from tkinter import *

def addition():
    number = int(myBox.get())
    answer = int(answBox['text'])
    answBox['text'] = number + answer
    

def zeroing_out():
    answBox['text'] = 0
    myBox.delete(0, END)
    myBox.focus()


# Создадём окно, задаём title и параметры окна
root = Tk()
root.title('')
root.geometry('400x200')

# добавляем текстовый элемент 
text_numb = Label(text='Введите число:')
text_numb.place(x=10, y=10)

# Создаём текстовое поле для ввода данных и задаём позицию и размеры
myBox = Entry(text=0)
myBox.place(x=120, y=10, width = 80, height = 25)
myBox['justify'] = 'center'
myBox['fg'] = 'green'
myBox.focus()

# Добавляем кнопку "Прибавления" и задаём расположение и параметры 
addButton = Button(text='Прибавить', command=addition)
addButton.place(x=200, y=10, width = 80, height = 25)

# Добавляем текстовый элемент
answer_text = Label(text='Сумма равна:')
answer_text.place(x=10, y=50)

# Добавляем поле вывода данных, задаём позицию и размеры
answBox = Message(text=0)
answBox.place(x=120, y=50, width = 80, height = 20)
answBox['bg'] = 'white'
answBox['fg'] = 'green'
answBox['relief'] = 'groove'

#
answButton = Button(text='Сбросить результат', command=zeroing_out)
answButton.place(x=200, y=50, width = 140, height = 25)

root.mainloop()