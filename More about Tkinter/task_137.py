# Задача_137

# Измените программу 136, чтобы новые значения имени и пола, добавляемые в список,
# так же записывались в текстовый файл. 
# Добавьте еще одну кнопку, которая будет выводить весь текстовый файл в главном окне командной оболочки Python.
from tkinter import *

def add_to_list():
    name = nameBox.get()
    nameBox.delete(0, END)
    checkGender = gender.get()
    gender.set('М/Ж')
    newList = f'{name}, {checkGender} \n'
    myList.insert(END, newList)
    nameBox.focus()
    myFile = open('MyNameList.txt', 'a')
    myFile.write(newList)

def readList():
    myFile = open('MyNameList.txt', 'r')
    print(myFile.read())

app = Tk()
app.title('Список людей')
app.geometry('400x440')

nameText = Label(text='Введите имя:')
nameText.place(x=20, y=20, width=100, height=30)

nameBox = Entry(text='')
nameBox.place(x=120, y=20, width=150, height=30)
nameBox.focus()

gendText = Label(text='Выберите пол')
gendText.place(x=20, y=80)
gender = StringVar(app)
gender.set('М/Ж')
gendermenu = OptionMenu(app, gender, 'М', 'Ж')
gendermenu.place(x=120, y=80)

myList = Listbox()
myList.place(x=20, y=120, width=300, height=100)

addButton = Button(text='Добавить', command=add_to_list)
addButton.place(x=220, y=80, width=100, height=25)

add_csvButton = Button(text='PRINT', command=readList)
add_csvButton.place(x=220, y=250, width=100, height=25)

app.mainloop()