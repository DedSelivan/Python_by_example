# Задача_072

# Создайте список с названиями шести школьных предметов. 
# Спросите у пользователя, какие из этих предметов ему не нравятся. 
# Удалите выбранные предметы из списка и выведите его повторно.

my_list = ['алгебра', 'химия', 'физика', 'биология', 'экономика', 'география']
print(my_list)
numb = int(input('Сколько у вас нелюбимых предметов: '))

for i in range(numb):
    item = (input('Назовите нелюбимый предмет: ')).lower()
    my_list.remove(item)
print(sorted(my_list))
