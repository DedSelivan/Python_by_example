# Задача_012

# Предложите пользователю ввести два числа. Если первое число больше второго, сначала выведите второе число, а потом первое. 
# В противном случае выведите сначала первое число, а потом второе.

num_1,num_2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))

if num_1 > num_2:
    print(num_2)
    print(num_1)
elif num_1 == num_2:
    print('Числа равны')
else:
    print(num_1)
    print(num_2)