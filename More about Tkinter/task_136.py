# Задача_136

# Напишите программу, которая предлагает пользователю ввести имя, а затем выбрать пол человека из раскрывающегося списка. 
# При нажатии кнопки разделенные запятыми имя и пол добавляются в список.
from tkinter import *

def add_to_list():
    name = nameBox.get()
    nameBox.delete(0, END)
    checkGender = gender.get()
    gender.set('М/Ж')
    newList = f'{name}, {checkGender} \n'
    myList.insert(END, newList)
    nameBox.focus()

app = Tk()
app.title('Список людей')
app.geometry('350x250')

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

app.mainloop()