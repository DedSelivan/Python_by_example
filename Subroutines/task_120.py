# Задача_120

# Отобразите для пользователя следующее меню:
#  1) Addition
#  2) Subtraction
#  Enter 1 or 2:

# Если пользователь выбирает 1, запускается подпрограмма, генерирующая два случайных числа из диапазона между 5 и 20. 
# Предложите пользователю сложить их. 
# Рассчитайте правильный ответ и выведите его для пользователя вместе с его ответом.
# 
# Если он выбирает 2, должна запускаться подпрограмма, генерирующая случайное число между 25 и 50, 
# а затем еще одно между 1 и 25. 
# Попросите пользователя вычесть второе из первого: так ему не придется беспокоиться об отрицательных значениях. 
# Выведите правильный ответ вместе с ответом пользователя.

# Создайте еще одну подпрограмму, которая будет проверять совпадение ответа пользователя с правильным ответом. 
# Если ответы совпали, выведите сообщение «Correct»; 
# в противном случае выведите «Incorrect, the answer is» и правильный ответ.

# Если пользователь ввел некорректное значение в самом первом меню, выведите соответствующее сообщение.

import random

def addition():
    number_one, number_two = random.randint(5, 20), random.randint(5, 20)
    answer_user = int(input(f'{number_one} + {number_two} = '))
    answer_comp = number_one + number_two
    answ = (answer_user, answer_comp)
    return answ

def subtraction():
    number_one, number_two = random.randint(25, 50), random.randint(1, 25)
    answer_user = int(input(f'{number_one} - {number_two} = '))
    answer_comp = number_one - number_two
    answ = (answer_user, answer_comp)
    return answ

def comparison(answer_user, answer_comp):
    if answer_user == answer_comp:
        print(f'«Correct»')
    else:
        print(f'«Incorrect, the answer is»')
        print(f'Правильный ответ: {answer_comp}')

def my_main_function():
    print(""" 
    1) Addition
    2) Subtraction
    Enter 1 or 2:
    """)
    your_choice = int(input('Ваш выбор: '))
    if your_choice == 1:
        answer_user, answer_comp = addition()
        comparison(answer_user,answer_comp)
    elif your_choice == 2:
        answer_user, answer_comp = subtraction()
        comparison(answer_user, answer_comp)
    else:
        print(f'«Incorrect selection»')

my_main_function()