# Задача_046

# Предложите пользователю ввести число. Продолжайте запрашивать число, пока введенное число не будет больше 5, 
# после чего выведите сообщение «The last number you entered was a [число]» и остановите программу.

count = 0

while count <= 5:
    numb = int(input('Введите число: '))
    count += numb
print(f'«The last number you entered was a {numb}»')    