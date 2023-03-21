# Задача_149(Таблица умножения)

from tkinter import *

def showTable():
    number = int(numBox.get())
    for i in range(1,13):
        answer = number * i
        numbList.insert(END,(number, "x", i, "=", answer))
    numBox.delete(0, END)
    numBox.focus()


def clearList():
    numBox.delete(0, END)
    numbList.delete(0, END)
    numBox.focus()

app = Tk()
app.title('Таблица умножения')
app.geometry("400x300")

numbText = Label(text="Введите число:")
numbText.place(x = 20, y = 20, width = 100, height = 25)

numBox = Entry(text=0)
numBox.place(x = 120, y = 20, width = 100, height = 25)
numBox.focus()

viewButton = Button(text="Показать таблицу", command=showTable)
viewButton.place(x = 240, y = 20, width = 150, height = 25)

numbList = Listbox()
numbList.place(x = 120, y = 50, width = 100, height = 220)

clearButton = Button(text="Очистить таблицу", command=clearList)
clearButton.place(x = 240, y = 50, width = 150, height = 25)


app.mainloop()

