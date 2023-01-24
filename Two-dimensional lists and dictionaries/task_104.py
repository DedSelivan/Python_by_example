# Задача_104

# После получения имени, возраста и размера обуви для четырех человек 
# запросите у пользователя имя человека для удаления из списка. 
# Удалите эту строку и выведите остальные данные с разбивкой по строкам.

list = {}


for i in range(4):
    name, age, shoe_size = input('Введите имя: ').title(), int(input('Введите возраст: ')), int(input('Введите размер обуви: '))
    list[name] = {'age':age, 'shoe_size':shoe_size}

name = input('Введите имя для удаления: ').title()

del list[name]
for name in list:
    print(name, list[name]['age'], list[name]['shoe_size'])
