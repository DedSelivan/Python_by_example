# Задача_139

# Создайте базу данных SQL с именем PhoneBook. 
# База данных должна содержать таблицу Names со следующими данными:


# Подключаем библиотеку SQL
import sqlite3

# Подключаемся к базе данны PhoneBook.db (если она не существует, то будет создана )
with sqlite3.connect("PhoneBook.db") as db:
    cursor =db.cursor()

# Создаем таблицу Names с полями (id, firstname, surname, phonenumber)
cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
ID integer PRIMARY KEY,
 FirstName text,
 Surname text,
 PhoneNumber text);""")

# Вставляем данные в таблицу Names. Команда db.commit - обновляет данные
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
VALUES("1", "Simon", "Howeis", "01223 349752")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
VALUES("2", "Karen", "Phillips", "01954 295773")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
VALUES("3", "Darren", "Smith", "01583 749012")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
VALUES("4", "Anne", "Jones", "01323 567322")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
VALUES("5", "Mark", "Smith", "01223 855534")""")
db.commit()

db.close()
