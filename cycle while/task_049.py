# Задача_049

# Создайте переменную с именем compnum и присвойте ей значение 50. 
# Предложите пользователю ввести число. 
# Пока предположение не совпадает со значением compnum, сообщите, больше оно или меньше compnum, 
# и предложите ввести другое число. 
# Если введенное значение совпадет с compnum, выведите сообщение «Well done, you took [попытки] attempts».

compnum = 50
number = int(input('Введите число: '))
count = 1

while number != compnum:
    if number < compnum:
        print(f'Введённое число меньше compnum')
    elif number > compnum:
        print('Введенное число больше compnum')
    count += 1
    number = int(input('Введите число: '))
print(f'«Well done, you took {count} attempts»')