# Задача_029

# Предложите пользователю ввести целое число больше 500. 
# Вычислите квадратный корень из этого числа и выведите его с точностью до двух знаков в дробной части.
import math

numb = int(input('Введите целое число больше 500: '))

if numb > 500:
    numb = math.sqrt(numb)
    print(round(numb, 2))
else:
    print(f'Число: {numb} меньше или равно 500')

