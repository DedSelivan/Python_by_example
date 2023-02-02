# Задача_119

# Определите подпрограмму, которая предлагает пользователю выбрать большое и маленькое число, 
# а затем генерирует случайное число из этого диапазона и сохраняет его в переменной с именем comp_num. 
# 
# Определите другую подпрограмму, которая выводит сообщение «I am thinking of a number...», 
# после чего предлагает пользователю угадать загаданное число.
# 
# Определите третью подпрограмму, которая проверяет, совпадает ли comp_num с предположением пользователя. 
# Если совпадает, то подпрограмма выводит сообщение «Correct, you win»;
# в противном случае цикл продолжается, а подпрограмма сообщает, больше или меньше их предположение загаданного числа,
#  и предлагает сделать новую попытку до тех пор, пока пользователь его не угадает.
import random

def numb():
    numb_1, numb_2 = int(input('Введите начальное число:')), int(input('Введите конечное число:'))
    comp_num = random.randint(numb_1,numb_2)
    return comp_num

def guess_the_number():
    print('I am thinking of a number...\n')
    number = int(input('Что это за число: '))
    return number

def verification():
    quest = numb()
    answ = guess_the_number()
    while quest != answ:
        if quest > answ:
            print('Твоё число меньше заданого')
            answ = int(input('Что это за число: '))
        elif quest < answ:
            print('Твоё число больше заданого')
            answ = int(input('Что это за число: '))
    print('«Correct, you win»')

verification()