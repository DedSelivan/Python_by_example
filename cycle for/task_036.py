# Задача_036

# Измените программу из упражнения 35 так, чтобы она предлагала пользователю ввести имя и число,
#  а затем выводила имя заданное количество раз.

name = input('Введите имя: ')
n = int(input('Введите число: '))

for i in range(n):
    print(name)