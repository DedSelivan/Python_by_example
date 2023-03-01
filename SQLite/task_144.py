# Задача_144

# Используя базу данных BookInfo из программы 141, предложите пользователю ввести имя автора.
# Сохраните все книги этого автора в текстовом файле; 
# поля должны разделяться дефисами, так что выводимая информация должна выглядеть примерно так:

# 5 - Murder on the Orient Express - Agatha Christie - 1934
# 8 - The murder on the links - Agatha Christie - 1923
# 10 - The secret adversary - Agatha Christie - 1921
# 11 - The seven dials mystery - Agatha Christie - 1929
# 
# Откройте текстовый файл и убедитесь в том, что программа работает правильно.

import sqlite3

# Создали текстовый файл для записи
myFile = open('myBookList.txt', 'w')

# Подключаемся к нашей базе данных
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# Выводим список авторов
cursor.execute("SELECT Name FROM Authors")
for row in cursor.fetchall():
    print(row)

# Запрашиваем фамилию автора
print()
selectAuthor = input("Выберите автора: ")
print()

# Записываем данные в файл txt
cursor.execute("SELECT * FROM Books WHERE Author = ? ", [selectAuthor])
for row in cursor.fetchall():
    myFile.write(f"{str(row[0])}, {row[1]}, {row[2]}, {str(row[3])}\n")
myFile.close()

db.close()