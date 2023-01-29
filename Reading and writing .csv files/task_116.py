# Задача_116

# Импортируйте данные из файла Books.csv в список. 
# Выведите список, предложите пользователю выбрать, какую строку он хочет исключить, и удалите ее. 
# Спросите пользователя, какие данные он хочет изменить, и предоставьте ему соответствующую возможность. 
# Запишите данные обратно в файл .csv с заменой существующих.

import csv
myFile = list(csv.reader(open('Books.csv')))
MyListBook = []
for row in myFile:
    MyListBook.append(row)

numb = 0
for row in MyListBook:
    print(f'{numb} - {row}')
    numb += 1

MyListBook.remove(MyListBook[int(input('Номер строки для удаления: '))])

numb = 0
for row in MyListBook:
    print(f'{numb} - {row}')
    numb += 1

numb = 0
numb_str = int(input('Введите номер строки для изменения: '))
for row in MyListBook[numb_str]:
    print(f'{numb} - {row}')
    numb += 1
part = int(input('Введите номер раздела для изменения: '))
MyListBook[numb_str][part] = input('Введите новые данные: ')
print(MyListBook[numb_str])


numb = 0
myFile = open('Books.csv', 'w')
for row in MyListBook:
    myFile.write(f'{MyListBook[numb][0]},{MyListBook[numb][1]},{MyListBook[numb][2]}\n')
    numb += 1
myFile.close()    