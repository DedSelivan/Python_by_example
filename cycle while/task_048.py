# Задача_048

# Предложите пользователю ввести имя человека, которого пользователь хочет пригласить на вечеринку. 
# После этого выведите сообщение «[имя] has been invited» и увеличьте счетчик на 1. 
# Спросите, хочет ли пользователь пригласить кого-то еще. 
# Продолжайте запрашивать имена, пока пользователь не ответит отрицательно, и выведите количество приглашенных.

count = 0
question = 'yes'

while question == 'yes':
    name = input('Введите имя гостя: ')
    print(f'«{name} has been invited»')
    count += 1
    question = input('Добавить ещё человека? yes/no: ')
print(f'Количество гостей приглашенных на вечеринку равно: {count}')