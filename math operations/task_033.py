# Задача_033

# Предложите пользователю ввести два числа. 
# Используйте целочисленное деление, чтобы разделить первое число на второе; 
# вычислите остаток и выведите ответ в виде, удобном для пользователя 
# (например, если пользователь ввел 7 и 2, 
# выведите строку вида «если разделить 7 на 2, получится 3 с остатком 1»).

num1,num2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))

print(f'«Если разделить {num1} на {num2}, получится {num1 // num2} с остатком {num1 % num2}»')