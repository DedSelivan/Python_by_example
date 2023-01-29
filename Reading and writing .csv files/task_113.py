# Задача_113

# Используя файл Books.csv, спросите пользователя, сколько записей он хочет добавить в список,
# и предоставьте ему такую возможность. 
# После того как данные будут добавлены, запросите автора и выведите все книги указанного автора из списка. 
# Если в списке нет ни одной книги этого автора, выведите соответствующее сообщение.
import csv

numb = int(input('Сколько записей хотете добавить ?: '))
myFile = open('Books.csv', 'a')
for i in range(numb):
    book, name, year = input('Введите название: '), input('Введите автора: '), input('Введите год выпуска: ')
    myFile.write(f'{book}, {name}, {year}\n')
myFile.close()

author = input('Введите название автора: ')

myFile = open('Books.csv', 'r')
count = 0
for row in myFile:
    if author in row:
        count += 1
        print(row)
if count == 0:
    print(f'Автор не найден')    
myFile.close() 