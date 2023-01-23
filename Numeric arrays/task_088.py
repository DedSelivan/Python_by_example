# Задача_088

# Предложите пользователю ввести пять целых чисел и сохраните их в массиве. 
# Отсортируйте список и выведите его содержимое в обратном порядке.

from array import *

new_array = array('i',[])
for i in range(5):
    new_array.append(int(input('Добавьте число в массив: ')))
new_array = sorted(new_array)
new_array.reverse()
print(new_array)

