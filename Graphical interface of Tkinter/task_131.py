# Задача_131

# Создайте программу, которая предоставляет пользователю возможность создать новый файл .csv. 
# Программа предлагает ввести имя и возраст, а затем добавляет введенные данные в конец только что созданного файла.

from tkinter import *
import csv

def newCSV():
    newFile = open('NewFile_task131.csv', 'w')
    newFile.close()

def addCSV():
    myFile = open('NewFile_task131.csv', 'a')
    myFile.write(str(f'{nameBox.get()}, {ageBox.get()} \n'))
    myFile.close()
    nameBox.delete(0, END)
    ageBox.delete(0, END)
    nameBox.focus()

app = Tk()
app.title('Создание CSV')
app.geometry('300x100')

nameText = Label(text='Введите имя:')
nameText.place(x=10, y=10, width=100, height=25)

nameBox = Entry(text='')
nameBox.place(x=110, y=10, width=150, height=25)
nameBox.focus()

ageText = Label(text='Введите возраст:')
ageText.place(x=13, y=40, width=120, height=25)

ageBox = Entry(text='')
ageBox.place(x=130, y=40, width=80, height=25)

newButton = Button(text='New file', command=newCSV)
newButton.place(x=13, y=70, width=120, height=25)

addButton = Button(text='Add to file', command=addCSV)
addButton.place(x=130, y=70, width=120, height=25)

app.mainloop()