# Задача_112

# Используя файл Books.csv из программы 111, предложите пользователю ввести новую запись и добавьте ее в конец файла. 
# Выведите каждую строку файла .csv в отдельной строке.
import csv

myFile = open('Books.csv', 'r')
print(myFile.read())
myFile.close()

book, name, year = input('Введите название: '), input('Введите автора: '), input('Введите год выпуска: ')

myFile = open('Books.csv', 'a')
myFile.write(f'{book}, {name}, {year}\n')
myFile.close()

myFile = open('Books.csv', 'r')
for row in myFile:
    print(row)
myFile.close()
