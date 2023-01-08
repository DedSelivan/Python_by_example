# Задача_044.py

# Спросите у пользователя, скольких людей он хочет пригласить на вечеринку. 
# Если будет введено число меньше 10, запросите имена и после каждого имени выведите строку «[имя] has been invited». 
# Если введенное число больше или равно 10, выведите сообщение «Too many people».

quantity_of_people = int(input('Введите количество людей для пришлашения на вечеринку: '))

if quantity_of_people < 10 and quantity_of_people > 0:
    for i in range(quantity_of_people):
        name = input('Введите имя гостя: ')
        print(f'«{name} has been invited»')
else:
    print('«Too many people»')