# Задача_056

# Выберите случайное целое число в диапазоне от 1 до 10. 
# Предложите пользователю ввести число и проверьте, совпадает ли оно с загаданным. 
# Продолжайте запрашивать числа до тех пор, пока пользователь не введет случайно выбранное число

import random
number = random.randint(1,10)

choise = int(input('Введите число в диапазоне от 1 до 10: '))
if choise > 0 and choise < 11:
    while choise != number:
        print('Число не совпадает с загаданным!!!')
        choise = int(input('Введите число в диапазоне от 1 до 10: '))
    print(f'Ура! Число совпало с загаданным')
else:
    print(f'Введённое число не соответсвует диапазону от 1 до 10')