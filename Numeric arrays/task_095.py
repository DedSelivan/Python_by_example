# Задача_095

# Создайте массив из пяти чисел от 10 до 100, каждое из которых содержит два знака в дробной части. 
# Предложите пользователю ввести целое число от 2 до 5. 
# Если пользователь введет значение, выходящее за границы диапазона, выведите сообщение об ошибке и предложите выбрать снова,
#  пока не будет введено допустимое значение. 
# Разделите каждое из чисел в массиве на число, введенное пользователем, и выведите ответы с точностью до двух знаков.

import math
from array import*

my_array = array('f', [68.75, 77.33, 99.99, 11.22, 43.00])

item = int(input('Введите число от 2 до 5: '))

stop = True

while stop == True:
    if item >= 2 and item <= 5:
        for i in my_array:
            i = i / item
            print(round(i, 2))
        stop = False
    else:
        print(f'Значение не соответствует параметрам')
        item = int(input('Введите число от 2 до 5: '))
        
