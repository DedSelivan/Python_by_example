# Задача_115

# Используя файл Books.csv, выведите данные с нумерацией строк.

myFile = open('Books.csv', 'r')
count = 0
for row in myFile:
    print(f'Строка {count} - {row}')
    count += 1