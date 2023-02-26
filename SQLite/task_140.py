# Задача_140

# Используя базу данных PhoneBook из программы 139, напишите программу, которая выводит следующее меню:

# Main Menu

# 1) View phone book
# 2) Add to phone book
# 3) Search for surname
# 4) Delete person from phone book
# 5) Quit

# Enter your selection: 
# 
# Если пользователь выбирает пункт 1, он сможет просмотреть всю телефонную книгу. 
# Если он выбирает пункт 2, он сможет добавить новую запись в телефонную книгу. 
# Если выбран пункт 3, программа предлагает ввести фамилию, а затем выводит записи всех людей с заданной фамилией. 
# При выборе пункта 4 программа предлагает ввести идентификатор и удаляет соответствующую запись из таблицы. 
# При выборе пункта 5 программа завершается. 
# Наконец, при вводе недопустимого числа должно выводиться соответствующее сообщение об ошибке. 
# После каждого действия пользователь должен возвращаться к меню, пока не будет выбран пункт 5.
import sqlite3

# Функция выводит телефонную книгу для просмотра
def view_phonebook():
    cursor.execute("SELECT * FROM Names")
    for row in cursor.fetchall():
        print(row)

# Функция для добавления новой записи в книгу
def add_to_phonebook():
    new_id = int(input("Введите ID: "))
    new_firstname = input("Введите имя: ")
    new_surname = input("Введите фамилию: ")
    new_phonenumber = input("Введите номер телефона: ")
    cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
    VALUES (?, ?, ?, ?)""", (new_id, new_firstname, new_surname, new_phonenumber))
    db.commit()

# Функция для поиска по фамилии
def search_for_name():
    select_surname = input("Введите фамилию: ")
    cursor.execute(" SELECT * FROM Names WHERE surname = ?", [select_surname])
    for row in cursor.fetchall():
        print(row)
    db.commit()

# Функция для удаления из книги
def delete_person_from_phonebook():
    select_id = int(input("Введите ID пользователя для удаления: "))
    cursor.execute(" DELETE FROM Names WHERE id = ?", [select_id])
    cursor.execute(" SELECT * FROM Names ")
    for row in cursor.fetchall():
        print(row)
    db.commit()


# Подключаемся к базе данны PhoneBook.db
with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

# 
def myMain():
    again = "y"
    while again == "y":
        print("""
        Main Menu

        1) View phone book
        2) Add to phone book
        3) Search for surname
        4) Delete person from phone book
        5) Quit

        Enter your selection:

        """)
        selection = int(input("Выберите действие: "))

        if selection == 1:
            view_phonebook()
        elif selection == 2:
            add_to_phonebook()
        elif selection == 3:
            search_for_name()
        elif selection == 4:
            delete_person_from_phonebook()
        elif selection == 5:
            again == "n"
        else:
            print("Введён некорректный запрос :)")
        
myMain()
db.close()
        










