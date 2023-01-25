# Задача_108

# Откройте файл Names.txt. 
# Предложите пользователю ввести новое имя. 
# Добавьте его в конец файла и выведите все содержимое файла.

file = open('Names.txt', 'a')
names = input('Введите имя для добавления: ')
file.write(names + '\n')
file.close()

file = open('Names.txt', 'r')
print(file.read())
file.close()