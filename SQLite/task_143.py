# Задача_142

# Используя базу данных BookInfo из программы 141, предложите пользователю ввести год. 
# Выведите все книги, изданные после этого года; 
# список должен быть упорядочен по году издания.

import sqlite3

# Создаем файл с нашей базой данных
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# Предлагаем пользователю ввести год
select_year = int(input("Введите год: "))
print()

# Выводим построчно данные из таблицы Books
cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author
FROM Books WHERE DatePublished > ? ORDER BY DatePublished """, [select_year])
for i in cursor.fetchall():
    print(i)

db.close()