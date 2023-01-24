# Задача_101

# Используя программу из задачи 100, запросите у пользователя имя и регион. 
# Выведите соответствующие данные. 
# Запросите у пользователя имя и регион того значения, которое он хочет изменить, и позвольте скорректировать объем продаж. 
# Выведите объемы продаж по всем регионам для имени, выбранного пользователем.

my_database = {
    "John":{'N':3056, 'S':8463, 'E':8441, 'W':2694}, 
    "Tom":{'N':4832, 'S':6786, 'E':4737, 'W':3612},
    "Anna":{'N':5239, 'S':4802, 'E':5820, 'W':1859}, 
    "Fiona":{'N':3904, 'S':3645, 'E':8821, 'W':2451}
    }

name, region = input('Выберите имя: ').title(), input('Выберите регион: ').upper()
print(my_database[name][region])

name, region = input('Выберите имя изменяемого: ').title(), input('Выберите регион изменяемого: ').upper()
my_database[name][region] = int(input('Введите значение объема продаж: '))
print(my_database[name])