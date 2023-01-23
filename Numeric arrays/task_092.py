# Задача_092

# Создайте два массива: один будет содержать три числа, введенных пользователем, а другой — пять случайных чисел. 
# Объедините эти два массива в один большой. 
# Отсортируйте и выведите его, при этом каждое число должно выводиться в отдельной строке.

from array import*
import random

arr_1,arr_2 = array('i', []), array('i', [])

while len(arr_1) < 3:
    item = int(input('Введите число: '))
    arr_1.append(item)

while len(arr_2) < 5:
    item = random.randint(1, 100)
    arr_2.append(item)

arr_1.extend(arr_2)
arr_end = sorted(arr_1)
for i in arr_end:
    print(i)