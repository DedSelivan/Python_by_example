# Задача_122

#  Создайте следующее меню:

# 1) Add to file
# 2) View all records
# 3) Quit program
# 
# Enter the number of your selection:
# 
# Если пользователь выбрал вариант 1, данные должны добавляться в файл Salaries.csv, содержащий имена и зарплаты. 
# Если пользователь выбрал вариант 2, программа выводит все записи из файла Salaries.csv. 
# Если пользователь выбрал вариант 3, программа завершается. 
# Если выбран несуществующий вариант, выводится сообщение об ошибке. 
# Пользователь снова и снова возвращается к меню, пока не будет выбран вариант 3.


def add_to_file():
    my_file = open('Salaries.csv', 'a')
    name, salary = input('Введите имя сотрудника: '), int(input('Введите зарплату: '))
    my_file.write(f'{name}, {salary}\n')
    my_file.close()

def view_all_records():
    my_file = open('Salaries.csv', 'r')
    for row in my_file:
        print(row)
    my_file.close()

repeat = True
while repeat == True:
    print("""
    1) Add to file
    2) View all records
    3) Quit program
    
    Enter the number of your selection:
    """)
    select = int(input('Выберите действие: '))

    if select == 1:
        add_to_file()
    elif select == 2:
        view_all_records()
    elif select == 3:
        print('Вы успешно вышли из программы')
        repeat = False
    else:
        print('Введён некорректный запрос')