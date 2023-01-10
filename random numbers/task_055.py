# Задача_055

# Выберите случайное число в диапазоне от 1 до 5. 
# Предложите пользователю выбрать число. Если он угадал, выведите сообщение «Well done»; 
# в противном случае сообщите, что его число больше или меньше вашего, и предложите выбрать другое число. 
# Если со второго раза пользователь угадал, выведите сообщение «Correct»,а если нет — сообщение «You lose».

import random

# Первый вариант

# number = random.randint(1, 5)
# count = 1
# 
# choise = int(input('Выберите число от 1 до 5: '))
# 
# if choise == number:
#     print(f'«Well done»')
# else:
#     while count > 0:
#         count -= 1
#         if choise > number:
#             print(f'Число больше загаданного')
#         else:
#             print(f'Число меньше загаданного')
#         choise = int(input('Выберите число от 1 до 5: '))
#     if choise == number:
#         print(f'«Correct»')
#     else:
#         print('«You lose»')
# print(f'\nЗагаданное число: {number}')



# Второй вариант решения через цикл for
number = random.randint(1, 5)
print(number)
choise = int(input('Выберите число от 1 до 5: '))

if choise >= 1 and choise <= 5:
    if choise == number:
        print('«Well done»')
    elif choise > number:
        print(f'Введённое число больше загаданного: ')
        choise = int(input('Выберите число от 1 до 5: '))
        if choise == number:
            print(f'«Correct»')
        else:
            print(f'«You lose»')
    elif choise < number:
        print(f'Введённое число меньше загаданного: ')
        choise = int(input('Выберите число от 1 до 5: '))
        if choise == number:
            print(f'«Correct»')
        else:
            print(f'«You lose»')
else:
    print(f'Введенное число не соответствует диапазону от 1 до 5:')