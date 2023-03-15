# Задача_147

# Компьютер автоматически генерирует комбинацию из четырех цветов из списка возможных (предусмотрите возможность 
# компьютера многократно выбирать любой цвет).
# Например, компьютер может выбрать комбинацию «красный», «синий», «красный», «зеленый». 
# Эта последовательность остается скрытой от пользователя. 

# Пользователь вводит комбинацию из четырех цветов из списка, использованного компьютером. 
# Например, он может выбрать цвета «розовый», «синий», «желтый» и «красный».
# Программа сообщает, сколько цветов находятся в правильной позиции
# и сколько правильно угаданных цветов находятся в неправильных позициях.

import random

def select_colours():
    colors = ['зелёный', 'синий', 'оранжевый', 'белый', 'черный', 'фиолетовый', 'красный', 'жёлтый']
    c_one = random.choice(colors)
    c_two = random.choice(colors)
    c_three = random.choice(colors)
    c_four = random.choice(colors)
    puzzle = (c_one, c_two, c_three, c_four)
    return puzzle

def guessing(c_one, c_two, c_three, c_four):
    print("Цвета: зелёный, синий, оранжевый, белый, черный, фиолетовый, красный, жёлтый\n")
    guess = True
    while guess == True:
        colour_one = input('Выберите первый цвет:').lower()
        if colour_one != 'зелёный' and colour_one != 'синий' and colour_one != 'оранжевый' and colour_one != 'белый' and colour_one != 'черный' and colour_one != 'фиолетовый' and colour_one != 'красный' and colour_one != 'жёлтый':
            print("Некорректный цвет")
        else:
            guess = False
    guess = True
    while guess == True:
        colour_two = input('Выберите второй цвет:').lower()
        if colour_two != 'зелёный' and colour_two != 'синий' and colour_two != 'оранжевый' and colour_two != 'белый' and colour_two != 'черный' and colour_two != 'фиолетовый' and colour_two != 'красный' and colour_two != 'жёлтый':
            print("Некорректный цвет")
        else:
            guess = False
    guess = True
    while guess == True:
        colour_three = input('Выберите третий цвет:').lower()
        if colour_three != 'зелёный' and colour_three != 'синий' and colour_three != 'оранжевый' and colour_three != 'белый' and colour_three != 'черный' and colour_three != 'фиолетовый' and colour_three != 'красный' and colour_three != 'жёлтый':
            print("Некорректный цвет")
        else:
            guess = False
    guess = True
    while guess == True:
        colour_four = input('Выберите четвёртый цвет:').lower()
        if colour_four != 'зелёный' and colour_four != 'синий' and colour_four != 'оранжевый' and colour_four != 'белый' and colour_four != 'черный' and colour_four != 'фиолетовый' and colour_four != 'красный' and colour_four != 'жёлтый':
            print("Некорректный цвет")
        else:
            guess = False
    correct = 0
    inCorrect = 0
    c_No = 4
    if c_one == colour_one:
        correct += 1
    elif c_one == colour_two or c_one == colour_three or c_one == colour_four:
        inCorrect += 1
    if c_two == colour_two:
        correct += 1
    elif c_two == colour_one or c_two == colour_three or c_two == colour_four:
        inCorrect += 1
    if c_three == colour_three:
        correct += 1
    elif c_three == colour_one or c_three == colour_two or c_three == colour_four:
        inCorrect += 1
    if c_four == colour_four:
        correct += 1
    elif c_four == colour_one or c_four == colour_two or c_four == colour_three:
        inCorrect += 1
    print(f'Количество угаданных цветов в правильной позиции: {correct}')
    print(f'Количество угаданных цветов в неправильной позиции: {inCorrect}')
    print(f'Количество не верно угаданных цветов {c_No - correct - inCorrect}')
    print()
    result = [correct, inCorrect]
    return result

def myMain():
    c_one, c_two, c_three, c_four = select_colours()
    score = 0
    play = True
    while play == True:
        correct, inCorrect = guessing(c_one, c_two, c_three, c_four)
        score += 1
        if correct == 4:
            play = False
    print(f'Поздравляем !!! Вы победили!!!\n')
    print(f'Вам хватило {score} попыток')

myMain()