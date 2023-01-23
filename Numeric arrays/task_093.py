# Задача_093

# Предложите пользователю ввести пять чисел. 
# Отсортируйте их и выведите для пользователя. 
# Предложите выбрать одно из чисел. 
# Удалите выбранное число из исходного массива и сохраните его в новом.

from array import*

arr_1, arr_2 = array('i',[]), array('i',[])

while len(arr_1) < 5:
    item = int(input('Введите число: '))
    arr_1.append(item)

arr_1 = sorted(arr_1)
print(arr_1)

item = int(input('Выберите число для удаления: '))
if item in arr_1:
    arr_1.remove(item)
    arr_2.append(item)
else:
    print(f'Число {item} не в массиве ')
print(arr_1)
print(arr_2)