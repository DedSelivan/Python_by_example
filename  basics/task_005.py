# Задача_005

# Предложите пользователю ввести три числа. Сложите первые два числа, затем умножьте сумму на третье число. 
# Выведите результат в виде 
# The answer is [результат].

number_1,number_2,number_3 = int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))
print(f'The answer is {(number_1+number_2) * number_3}')