# Задача_086.py

# Предложите пользователю ввести пароль, а затем предложите ввести его повторно. 
# Если два пароля совпадут, выведите сообщение «Thank you». 
# Если буквы введены правильно, но различаются регистром, выведите сообщение «They must be in the same case»;
# в противном случае выводится сообщение «Incorrect».

password, double_pass = input('\nВведите пароль: '), input('Повторите пароль: ')

if password == double_pass:
    print(f'\n«Thank you»')
elif password.lower() == double_pass.lower():
    print(f'\n«They must be in the same case»')
else:
    print(f'\n«Incorrect»') 
