# Задача_123

# В языке Python невозможно напрямую удалить запись из файла .csv. Вместо этого приходится сохранять файл во временном списке,
# вносить в него изменения, а затем заменять исходный файл временным списком. 

# Измените предыдущую программу, чтобы она предоставляла такую возможность. Меню должно выглядеть так:
# 1) Add to file
# 2) View all records
# 3) Delete a record
# 4) Quit program

# Enter the number of your selection:

import csv

def add_to_file():
    myFile = open('Salaries.csv', 'a')
    name, salary = input('Введите имя сотрудника: '), int(input('Введите зарплату: '))
    myFile.write(f'{name}, {salary}\n')
    myFile.close

def view_all_records():
    myFile = open('Salaries.csv', 'r')
    for row in myFile:
        print(row)
    myFile.close()

def delete_a_record():
    myFile = open('Salaries.csv', 'r')
    my_list = []
    for row in myFile:
        my_list.append(row)
    
    
    numb = 0
    for row in my_list:
        print(f'{numb}.{row}')
        numb += 1

    strDel = int(input('Введите номер строки для удаления: '))
    del my_list[strDel]

    myFile = open('Salaries.csv', 'w')
    
    for row in my_list:
        myFile.write(row)
        
    myFile.close()

repeat = True
while repeat == True:
    print("""
    1) Add to file
    2) View all records
    3) Delete a record
    4) Quit program
    
    Enter the number of your selection:
    """)
    select = int(input('Выберите действие: '))

    if select == 1:
        add_to_file()
    elif select == 2:
        view_all_records()
    elif select == 3:
        delete_a_record()
    elif select == 4:
        print('Вы успешно вышли из программы')
        repeat = False
    else:
        print('Введён некорректный запрос')

