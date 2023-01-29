# Задача_117

# Создайте простую математическую игру, которая запрашивает у пользователя имя, а затем генерирует два случайных вопроса. 
# Сохраните имя, введенные вопросы, ответы пользователя и итоговый счет в файле .csv. 
# При каждом запуске программа должна добавлять информацию в файл .csv без перезаписи существующих данных.

import random
import csv

score = 0
player_name = input('Введите ваше имя: ')

number_one, number_two = random.randint(1, 100), random.randint(1, 100)
answer_one = int(input(f'{number_one} + {number_two} = '))
if answer_one == number_one + number_two:
    score += 1

numb_one, numb_two = random.randint(1, 100), random.randint(1, 100)
answer_two = int(input(f'{numb_one} + {numb_two} = '))
if answer_two == numb_one + numb_two:
    score += 1

myFile = open('Score.csv', 'a')
myFile.write(f'{player_name},{number_one} + {number_two} =,{answer_one},{numb_one} + {numb_two} =,{answer_two},{score}\n')
myFile.close()