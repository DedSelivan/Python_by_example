# Задача_145

# Напишите программу, которая отображает следующий экран: 
# 
# При нажатии кнопки Add данные должны сохраняться в базе данных SQL с именем TestScores. 
# Кнопка Clear стирает текущее содержимое окна.

import sqlite3
from tkinter import *

def addList():
    name = nameBox.get()
    grade = gradeBox.get()
    cursor.execute("""INSERT INTO Scores(name, score)
    VALUES(?, ?)""", (name, grade))
    db.commit()



def clear():
    nameBox.delete(0, END)
    gradeBox.delete(0, END)
    nameBox.focus()

with sqlite3.connect("TestScore.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Scores(
    id integer PRIMARY KEY,
    name text,
    score integer); """)

app = Tk()
app.title("TestScores")
app.geometry("400x200")

nameText = Label(text="Enter student's name:")
nameText.place(x=30, y=30)
nameBox = Entry(text="")
nameBox.place(x=170, y=30, width=150, height=25)
nameBox.focus()

gradeText = Label(text="Enter student's grade:")
gradeText.place(x=30, y=80)
gradeBox = Entry(text="")
gradeBox.place(x=170, y=80, width=150, height=25)

addButton = Button(text="Add", command=addList)
addButton.place(x=170, y=120, width=50, height=25)

clearButton = Button(text="Clear", command=clear)
clearButton.place(x=240, y=120, width=75, height=25)

app.mainloop()
db.close()
