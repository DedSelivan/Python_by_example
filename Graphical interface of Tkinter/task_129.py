# Здачада_129

# Создайте окно, которое предлагает пользователю ввести число в текстовом поле. 
# При нажатии кнопки используйте конструкцию varialble.isdigit() для проверки того, является ли число целым. 
# Если проверка дает положительный результат, оно добавляется в список; 
# в противном случае содержимое текстового поля стирается. 
# Создайте дополнительную кнопку для очистки списка.

from tkinter import *

def addNumb():
    number = numbBox.get()
    if number.isdigit():
        addList.insert(END, number)
        numbBox.delete(0, END)
        numbBox.focus()
    else:
        numbBox.delete(0, END)
        numbBox.focus()

def clearList():
    addList.delete(0, END)
    numbBox.focus()

# Добавим окно, зададим title и размеры
app = Tk()
app.title('Целое число')
app.geometry('300x300')

# Добавим текстовый элемент
addText = Label(text='Введите число:')
addText.place(x=10, y=10, width=100, heigh=25)

# Добавим поле для ввода чисел
numbBox = Entry(text=0)
numbBox.place(x=110, y=10, width=100, heigh=25)
numbBox.focus()

# Добавим кнопку проверки и добавления числа
addButton = Button(text='Проверить и добавить', command=addNumb)
addButton.place(x=10, y=40, width=150, heigh=25)

# Добавим кнопку очистить
clearButton = Button(text='Очистить список', command=clearList)
clearButton.place(x=170, y=40, width=120, heigh=25)

# Создадим список для добававления
addList = Listbox()
addList.place(x=10, y=80, width=280, heigh=160)


app.mainloop()