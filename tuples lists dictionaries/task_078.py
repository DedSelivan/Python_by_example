# Задача_078

# Создайте список с названиями четырех телевизионных передач и выведите их на отдельных строках. 
# Предложите пользователю ввести название еще одной передачи и позицию, на которой она должна быть вставлена в список. 
# Снова выведите список, в котором все пять передач находятся на новых позициях.

tv_list = ['Вопрос ребром', 'Ушатайка', 'На ножах', 'Мой район']
for i in tv_list:
    print(i)
telecast = input('Введите название передачи для добавления: ').title()
cast_numb = int(input('Введите номер позиции на которой будет вставлена в список: '))
tv_list.insert(cast_numb, telecast)
for i in tv_list:
    print(i)