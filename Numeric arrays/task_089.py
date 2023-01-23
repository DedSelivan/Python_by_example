# Задача_089

# Создайте массив для хранения целых чисел. 
# Сгенерируйте пять случайных чисел и сохраните их в массиве. 
# Выведите массив (каждый элемент должен выводиться в отдельной строке).
from array import *
import random

arr = array('i',[])
for i in range(5):
    item = random.randint(1, 100)
    arr.append(item)
for j in arr:
    print(j)