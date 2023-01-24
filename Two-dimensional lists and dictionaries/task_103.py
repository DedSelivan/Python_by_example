# Задача_103

# Измените программу 102, чтобы она выводила имя и возраст для всех людей в списке, но не их размер обуви.

list = {}


for i in range(4):
    name, age, shoe_size = input('Введите имя: ').title(), int(input('Введите возраст: ')), int(input('Введите размер обуви: '))
    list[name] = {'age':age, 'shoe_size':shoe_size}

for name in list:
    print(name, list[name]['age'])
    

