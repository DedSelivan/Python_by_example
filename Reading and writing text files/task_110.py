# Задача_110

# С помощью созданного ранее файла Names.txt выведите список имен в Python. 
# Попросите пользователя ввести одно из имен, 
# а затем сохраните все, кроме выбранного в новом файле, под названием Names2.txt.

file = open('Names.txt', 'r')
print(file.read())
file.close()

name = input('Введите имя которое исключить: ') + '\n'

file = open('Names.txt', 'r')
for i in file:
    if  i != name:
        file = open('Names2.txt', 'a')
        file.write(i)
        file.close()
file.close()

