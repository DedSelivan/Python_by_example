# Задача_014

# Предложите пользователю ввести число от 10 до 20 (включительно). 
# Если будет введено число из этого диапазона, выведите сообщение «Thank you»; 
# в противном случае выведите сообщение «Incorrect answer».

number = int(input('Введите число в диапазоне от 10 до 20 (включительно): '))

if number >= 10 and number <= 20:
    print('«Thank you»')
else:
    print('«Incorrect answer»')