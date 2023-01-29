# Задача_114

# Используя файл Books.csv, предложите пользователю ввести начальный и конечный год. 
# Выведите все книги, выпущенные в заданном промежутке времени.

import csv
start, finish = int(input('Введите начальный год: ')), int(input('Введите конечный год: '))


myFile = list(csv.reader(open('Books.csv', 'r')))
new_list = []
for row in myFile:
    new_list.append(row)

count = 0
for row in new_list:
    if int(new_list[count][2]) >= start and int(new_list[count][2]) <= finish:
        print(row)
    count += 1
