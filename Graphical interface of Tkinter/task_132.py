# Задача_132

# Используя файл .csv, созданный для последней задачи, напишите программу,
# которая предлагает пользователю добавлять записи с именами и возрастом разных людей. 
# Создайте кнопку для вывода содержимого файла .csv посредством импортирования его данных в список.
from tkinter import *
import csv

def addCSV():
    myFile = open('NewFile_task131.csv', 'a')
    name = nameBox.get()
    age = ageBox.get()
    myFile.write(f'{name}, {age}\n')
    myFile.close()
    nameBox.delete(0, END)
    ageBox.delete(0, END)
    nameBox.focus()

def readCSV():
    readList.delete(0, END)
    myFile = list(csv.reader(open('NewFile_task131.csv')))
    myList = []
    for row in myFile:
        myList.append(row)
    x = 0
    for row in myList:
        data = myList[x]
        readList.insert(END, data)
        x += 1


app = Tk()
app.title('Работа с .CSV')
app.geometry('300x300')

nameText = Label(text='Введите имя:')
nameText.place(x=10, y=10, width=100, height=25)

nameBox = Entry(text='')
nameBox.place(x=110, y=10, width=150, height=25)
nameBox['justify'] = 'left'
nameBox.focus()

ageText = Label(text='Введите возраст:')
ageText.place(x=13, y=40, width=120, height=25)

ageBox = Entry(text='')
ageBox.place(x=130, y=40, width=60, height=25)

addButton = Button(text='Add to CSV', command=addCSV)
addButton.place(x=10, y=70, width=100, height=25)

readButton = Button(text='Read the CSV', command=readCSV)
readButton.place(x=110, y=70, width=100, height=25)

readList = Listbox()
readList.place(x=10, y=100, width=280, height=180)

app.mainloop()