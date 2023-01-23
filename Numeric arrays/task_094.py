# Задача_094

# Выведите массив из пяти чисел. 
# Предложите пользователю выбрать одно из них. 
# После того как число будет выбрано, выведите его позицию в массиве. 
# Если пользователь введет значение, отсутствующее в массиве, предложите ему выбрать снова, 
# пока не будет выбрано допустимое значение.

from array import*
import random

arr = array('i', [])

for i in range(5):
    arr.append(random.randint(1, 100))
print(arr)

item = int(input('Выберите число из массива: '))

stop = True
while stop == True:
    if item in arr:
        print(arr.index(item))
        stop = False
    else:
        print('Число не из массива')
        item = int(input('Выберите число из массива: '))

