# Задача_099

# Измените программу из задачи 098. 
# Предложите пользователю выбрать строку и выведите только ее. 
# Предложите выбрать столбец из выведенной строки и выведите только хранящееся там значение. 
# Спросите, хочет ли пользователь изменить его. 
# Если ответ будет положительным, предложите ввести новое значение и измените данные. 
# Наконец, снова выведите измененную строку.

my_array = [[2,5,8], [3,7,4], [1,6,9], [4, 2, 0]]

line = int(input('Выберите строку: '))
print(my_array[line])

column = int(input('Выберите столбец: '))
print(my_array[line][column])

quest = input('Хотели бы вы изменить число (y/n): ')
if quest == 'y':
    my_array[line][column] = int(input('Введите число на которое хотите заменить: '))
print(my_array[line])