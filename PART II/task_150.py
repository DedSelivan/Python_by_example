# Задача_150(Картинная галерея)

# Программа должна предоставлять возможность добавления новых записей о художниках и картинах.
# После того как картина будет продана, данные о ней должны быть удалены из главной базы данных SQL и 
# сохранены в отдельном текстовом файле.
# Пользователь должен иметь возможность искать картины по имени художника, технике исполнения или цене.
import sqlite3
from tkinter import *

def addArtist():
    newNameArtist = artistNameBox.get()
    newAdress = adressBox.get()
    newTown = townBox.get()
    newCounty = countyBox.get()
    newPostCode = postcodeBox.get()
    cursor.execute("""INSERT INTO Artists(name, address, town, county, postcode)
    VALUES(?, ?, ?, ?, ?)""",(newNameArtist, newAdress, newTown, newCounty, newPostCode))
    db.commit()
    artistNameBox.delete(0, END)
    adressBox.delete(0, END)
    townBox.delete(0, END)
    countyBox.delete(0, END)
    postcodeBox.delete(0, END)
    artistNameBox.focus()

def clearArtist():
    artistNameBox.delete(0, END)
    adressBox.delete(0, END)
    townBox.delete(0, END)
    countyBox.delete(0, END)
    postcodeBox.delete(0, END)
    artistNameBox.focus()

def addArt():
    newArtName = artNameBox.get()
    newTitle = artTitleBox.get()
    newMedium = medium_one.get()
    newPrice = artPriceBox.get()
    cursor.execute("""INSERT INTO Art(artistid, title, medium, price)
    VALUES (?, ?, ?, ?)""",(newArtName, newTitle, newMedium, newPrice))
    medium_one.set("")
    db.commit()
    artNameBox.delete(0, END)
    artTitleBox.delete(0, END)
    artPriceBox.delete(0,END)
    artistNameBox.focus()

def clearArt():
    artNameBox.delete(0, END)
    artTitleBox.delete(0, END)
    artPriceBox.delete(0,END)
    artistNameBox.focus()
    
def clearWindow():
    outputWindow.delete(0, END)

def viewArtist():
    cursor.execute("SELECT * FROM Artists")
    for x in cursor.fetchall():
        newRecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", " + str(x[4]) + ", " + str(x[5]) + "\n"
        outputWindow.insert(END, newRecord)
    

def viewArt():
    cursor.execute("SELECT * FROM Art")
    for x in cursor.fetchall():
        newRecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", ₤" + str(x[4]) + "\n"
        outputWindow.insert(END, newRecord)


def searchArtistOutput():
    selectArtist = searchArtist.get()
    cursor.execute("SELECT name * FROM Artists WHERE artistid = ?", [selectArtist])
    for x in cursor.fetchall():
        outputWindow.insert(END, x)
        cursor.execute("SELECT name * FROM Art WHERE artistid = ?", [selectArtist])
        for x in cursor.fetchall():
            newRecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", ₤" + str(x[4]) + "'\n"
            outputWindow.insert(END, newRecord)
    searchArtist.delete(0, END)
    searchArtist.focus()


def searchMediumOutput():
    selectMedium = medium_two.get()
    cursor.execute("""SELECT Art.pieceid, Artists.name, Art.title, Art.medium, Art.price FROM Artists, Art WHERE Artists.artistid = Art.artistid AND Art.medium = ?""", [selectMedium])
    for x in cursor.fetchall():
        newRecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", ₤" + str(x[4]) + "\n"
        outputWindow.insert(END, newRecord)
    medium_two.set("")

def searchByPrice():
    minPrice = minBox.get()
    maxPrice = maxBox.get()
    cursor.execute("""SELECT Art.pieceid, Artists.name, Art.title, Art.medium, Art.price 
    FROM Artists, Art WHERE Artists.artistid = Art.artistid AND Art.price >= ? AND Art.price <= ?
    """, [minPrice, maxPrice])
    for x in cursor.fetchall():
        newRecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", ₤" + str(x[4]) + "\n"
        outputWindow.insert(END, newRecord)
    minBox.delete(0, END)
    maxBox.delete(0, END)
    minBox.focus()

def sold():
    myFile = open("Sold.txt", "a")
    selectPiece = soldBox.get()
    cursor.execute("""SELECT * FROM Art WHERE pieceid = ?""", [selectPiece])
    for x in cursor.fetchall():
        newRecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", " + str(x[4]) + "\n"
        myFile.write(newRecord)
    myFile.close()
    cursor.execute("DELETE FROM Art WHERE pieceid = ?", [selectPiece])
    db.commit()

# Подключаемся к нашей БД
with sqlite3.connect("Art.db") as db:
    cursor = db.cursor()

# Создаем таблицу Artist (информация о художниках)
cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(
artistid integer PRIMARY KEY,
name text,
address text,
town text,
county text,
postcode text); """)

# Создаем таблицу Art (информация о картинах)
cursor.execute("""CREATE TABLE IF NOT EXISTS Art(
pieceid integer PRIMARY KEY,
artistid integer,
title text,
medium text,
price integer); """)

# Создаем окно, задаём title и задаем параметры
window = Tk()
window.title("Картинная галерея")
window.geometry("1200x700")

# Добавляем текстовый элемент 
newDataText = Label(text="Введите новые данные:")
newDataText.place(x=10, y=10)

# Добавляем текстовый элемент для ввода имени
artistNameText = Label(text="Введите имя:")
artistNameText.place(x=76, y=40)

# Добавляем элемент для ввода имени
artistNameBox = Entry(text="")
artistNameBox.place(x=164, y=40, width=80, height=25)
artistNameBox.focus()

# Добавляем текстовый элемент для ввода адреса
adressText = Label(text="Адрес:")
adressText.place(x=254, y=40)

# Добавляем элемент для ввода адреса
adressBox = Entry(text="")
adressBox.place(x=300, y=40, width=150, height=25)

# Добавляем текстовый элемент город
townText = Label(text="Город: ")
townText.place(x=460, y=40)

# Добавляем элемент ввода города
townBox = Entry(text="")
townBox.place(x=505, y=40, width=100, height=25)

# Добавляем текстовый элемент округа
countyText = Label(text="Округ:")
countyText.place(x=615, y=40)

# Добавляем элемент ввода округа
countyBox = Entry(text="")
countyBox.place(x=660, y=40, width=100, height=25)

# Добавляем текстовый элемент индекса
postcodeText = Label(text="Индекс:")
postcodeText.place(x=770, y=40)

# Добавляем элемент ввода индекса
postcodeBox = Entry(text="")
postcodeBox.place(x=825, y=40, width=100, height=25)

# Добавляем кнопку добавления данных
addButton = Button(text="Добавить художника", command=addArtist)
addButton.place(x=110, y=80)

# Добавляем кнопку очистки данных
clearButton = Button(text="Очистить данные", command=clearArtist)
clearButton.place(x=300, y=80)

artNameText = Label(text="ID художника:")
artNameText.place(x=76, y=120)

artNameBox = Entry(text="")
artNameBox.place(x=170, y=120, width=80, height=25)

artTitleText = Label(text="Заглавие:")
artTitleText.place(x=260, y=120)

artTitleBox = Entry(text="")
artTitleBox.place(x=325, y=120, width=100, height=25)

artMediumText = Label(text="Средство:")
artMediumText.place(x=435, y=120)

medium_one = StringVar(window)
artMedium = OptionMenu(window, medium_one, "Oil", "Watercolor", "Ink", "Acrylic")
artMedium.place(x=505, y=120, width=100, height=25)

artPriceText = Label(text="Цена:")
artPriceText.place(x=615, y=120)

artPriceBox = Entry(text="")
artPriceBox.place(x=655, y=120, width=100, height=25)

addArtButton = Button(text="Добавить картину", command=addArt)
addArtButton.place(x=120, y=160)

clearArtButton = Button(text="Очистить данные", command=clearArt)
clearArtButton.place(x=300, y=160)

outputWindow = Listbox()
outputWindow.place(x=76, y=200, width=1000, height=350)

clearOutputWindow = Button(text="Очистить данные", command=clearWindow)
clearOutputWindow.place(x=76, y=550)

viewAllButton = Button(text="Показать художников", command=viewArtist)
viewAllButton.place(x=230, y=550)

viewArtButton = Button(text="Показать картины", command=viewArt)
viewArtButton.place(x=410, y=550)

searchArtist = Entry(text="")
searchArtist.place(x=76, y=593, width=100, height=25)

searchArtistButton = Button(text="Поиск художника", command=searchArtistOutput)
searchArtistButton.place(x=176, y=590)

medium_two = StringVar(window)
searchMedium = OptionMenu(window, medium_two, "Oil", "Watercolor", "Ink", "Acrylic")
searchMedium.place(x=340, y=595, width=100, height=25)

searchMediumButton = Button(text="Поиск", command=searchMediumOutput)
searchMediumButton.place(x=450, y=590)

minText = Label(text="Минимум:")
minText.place(x=530, y=595)

minBox = Entry(text="")
minBox.place(x=600, y=595, width=50, height=25)

maxText = Label(text="Максимум:")
maxText.place(x=660, y=595)

maxBox = Entry(text="")
maxBox.place(x=735, y=595, width=50, height=25)

searchPriceButton = Button(text="Поиск по стоимости")
searchPriceButton.place(x=795, y=592)

soldText = Label(text="Продано:")
soldText.place(x=74, y=650)

soldBox = Entry(text="")
soldBox.place(x=140, y=650, width=120, height=25)

soldButton = Button(text="Продано", command=sold)
soldButton.place(x=270, y=648)

window.mainloop()
db.close()