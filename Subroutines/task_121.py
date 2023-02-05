# Задача_121

# Напишите программу, которая помогает пользователю легко управлять списком имен. 
# Программа должна выводить меню, дающее возможность добавлять, изменять и удалять имена из списка, а также отображать их все.
# Кроме того, в меню должна присутствовать команда для завершения работы программы. 
# Если пользователь выбрал несуществующую команду, программа выводит соответствующее сообщение. 
# После того как пользователь выбрал команду добавления, изменения или удаления имени или просмотра всех имен, 
# меню должно выводиться снова без необходимости перезапуска программы. 
# Программа должна быть по возможности простой и удобной в использовании.

def adding():
    listName.append(input('Введите имя для добавления: '))
    return listName

def change():
    numb = 0
    for name in listName:
        print(f'{numb}.{name}')
        numb += 1
    change_numb = int(input('Введите номер из списка для изменения: '))
    listName[change_numb] = input('Введите имя: ')
    return listName

def delete():
    numb = 0
    for name in listName:
        print(f'{numb}.{name}')
        numb += 1
    del listName[int(input('Введите номер для удаления: '))]
    return listName

def show_name():
    x = 0
    for name in listName:
        print(f'{x}.{name}')
        x += 1

def main():
    do = 'yes'
    while do == 'yes':
        print("""
            Выберите действие:

            1. Для добавления в список введите: add
            2. Для изменения списка введите: change
            3. Для удаления из списка введите: del
            4. Для вывода списка введите: show
            5. Для выхода нажмите: exit
        """)
        select = input('Выберите действие: ').lower()

        if select == 'add':
            listName = adding()
        elif select == 'change':
            listName = change()
        elif select == 'del':
            listName = delete()
        elif select == 'show':
            listName = show_name()
        elif select == 'exit':
            do = 'no'
            print(f'Работа программы завершена')
        else:
            print(f'Вы ввели некорректное значение') 

listName = []
main()