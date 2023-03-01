# Задача_142

# Используя базу данных BookInfo из программы 141, выведите список авторов с датами рождения. 
# Предложите пользователю ввести место рождения, 
# а затем выведите название, дату издания и имя автора для всех книг авторов, родившихся в указанном месте.

import sqlite3

# Создаем файл с нашей базой данных
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# Выводим построчно список авторов
cursor.execute("SELECT * FROM Authors")
for author in cursor.fetchall():
    print(author)

print()
location = input("Введите место рождения автора: ").title()
print()

# Выводим построчно название книги , дату издания и имя автора
cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author
FROM Books,Authors WHERE Authors.Name = Books.Author AND Authors.PlaceofBirth = ?
""",[location])
for x in cursor.fetchall():
    print(x)

db.close()