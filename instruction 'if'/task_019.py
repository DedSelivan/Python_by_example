# Задача_019

# Предложите пользователю ввести значение 1, 2 или 3. 
# Если введено значение 1, выведите сообщение «Thank you»; 
# если 2 — сообщение «Well done»; 
# если 3 — сообщение «Correct». 
# Если введено любое другое значение, выведите сообщение «Error message».

number = int(input('Введите значение 1, 2 или 3: '))

if number == 1:
    print(f'«Thank you»')
elif number == 2:
    print(f'«Well done»')
elif number == 3:
    print(f'«Correct»')
else:
    print(f'«Error message»')