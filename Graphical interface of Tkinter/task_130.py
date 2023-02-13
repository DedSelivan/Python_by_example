# Задача_130

# Измените программу 129, добавив третью кнопку для сохранения списка в файле .csv. 
# Команда tmp_list = num_list.get(0,END) может использоваться для сохранения содержимого списка в кортеже с именем tmp_list.
from tkinter import *
import csv

def addNumb():
    number = numbBox.get()
    if number.isdigit():
        addList.insert(END, number)
        numbBox.delete(0, END)
        numbBox.focus()
    else:
        numbBox.delete(0, END)
        numbBox.focus()

def save_csv():
    myFile = open('Task_130.csv', 'w')
    tmp_list = addList.get(0, END)
    x = 0
    for row in tmp_list:
        myFile.write(str(tmp_list[x] + '\n'))
        x += 1
    myFile.close()
    

def clearList():
    addList.delete(0, END)
    numbBox.focus()

# Добавим окно, зададим title и параметры
app = Tk()
app.title('Целое число (версия 2.0)')
app.geometry('400x400')

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

# Добавим кнопку сохранения csv
csvButton = Button(text='Сохранить в формате .CVS', command=save_csv)
csvButton.place(x=50, y=250, width=180, heigh=25)

app.mainloop()