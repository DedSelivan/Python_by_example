# Задача_043

# Спросите у пользователя, в каком направлении он хочет вести отсчет (в прямом или обратном). 
# Если выбран прямой отсчет, запросите число и проведите отсчет от 1 до введенного числа. 
# Если выбран обратный отсчет, запросите число меньше 20, а затем проведите обратный отсчет от 20 до заданного числа. 
# Если введено что-то другое, выведите сообщение «I don’t understand».

focus = input("""
Выберите в каком направлении вести отсчёт 1 или 2:
1) В прямом
2) В обратном
""")

if focus == '1':
    number = int(input('Введите число: '))
    for i in range(1, number+1):
        print(i)
elif focus == '2':
    number = int(input('Введите число меньше 20: '))
    if number < 20:
        for i in range(20, number-1, -1):
            print(i)
    else:
        print('Увы вы ввели число больше или равно 20...')
else:
    print('«I don\'t understand»')