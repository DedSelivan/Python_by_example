# Задача_007

# Предложите пользователю ввести его имя и возраст. 
# Увеличьте возраст на 1 и выведите сообщение:
# [имя] next birthday you will be [новый возраст].

your_name = input('Введите ваше имя: ')
your_surname = int(input('Введите возраст: '))
print(f'{your_name} next birthday you will be {your_surname + 1}')