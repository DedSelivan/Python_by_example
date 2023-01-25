# Задача_109

# Выведите следующее меню:
# 1) Create a new file
# 2) Display the file
# 3) Add a new item to the file
# Make a selection 1, 2 or 3:

# Предложите пользователю выбрать один из вариантов. Если пользователь введет что-либо, кроме 1, 2 и 3,
# программа должна вывести соответствующее сообщение об ошибке.
# Если пользователь выберет 1, предложите ему ввести название школьного предмета и 
# сохраните его в новом файле с именем Subject.txt. Существующий файл с таким именем должен быть заменен новым файлом.
# Если пользователь выберет 2, выводится содержимое файла Subject.txt.
# Если пользователь выберет 3, предложите пользователю ввести новый предмет, сохраните его в файле, а затем выведите все его 
# содержимое.
# Запустите программу несколько раз, чтобы протестировать разные команды.

print("""
1) Create a new file
2) Display the file
3) Add a new item to the file
Make a selection 1, 2 or 3:
""")

item = int(input('Выберите 1, 2 или 3: '))
print(item)

if item == 1:
    school_item = input('Введите название школьного предмета: ').title()
    file = open('Subject.txt', 'w')
    file.write(school_item + '\n')
    file.close()
elif item == 2:
    file = open('Subject.txt', 'r')
    print(file.read())
    file.close()
elif item == 3:
    item_new = input('Введите новый предмет: ').title()
    file = open('Subject.txt', 'a')
    file.write(item_new + '\n')
    file.close()
else:
    print('Ошибка ввода!!! Вы ввели значение отличное от 1, 2 или 3')