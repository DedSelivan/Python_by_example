# Задача_148(Пароли)

# Напишите программу, которая сохраняет идентификаторы пользователей и их пароли. Программа должна выводить следующее меню:
#        1) Create a new User ID
#        2) Change a password
#        3) Display all User IDs
#        4) Quit
#        Enter Selection:
# Если пользователь выбирает пункт 1, программа предлагает ввести идентификатор пользователя. 
# Она должна проверить, существует ли введенный идентификатор в списке. Если это так, программа выводит соответствующее 
# сообщение и предлагает выбрать другой идентификатор. После того как пользователь введет допустимый идентификатор, 
# программа запрашивает пароль. Паролю начисляется по одному баллу за соответствие перечисленным ниже условиям:

# пароль должен содержать не менее 8 символов; 
# пароль должен включать буквы верхнего регистра; 
# пароль должен включать буквы нижнего регистра;
# пароль должен включать цифры;
# пароль должен включать хотя бы один специальный символ: !, £, $, %, &, <, * или @.

# Если пароль получает всего 1 или 2 балла, он должен быть отклонен с формулировкой, что он является слабым. 
# Если у пароля 3 или 4 балла, выводится сообщение о том, что его можно улучшить. 
# Спросите пользователя, хочет ли он повторить попытку. Если пароль набрал 5 баллов, сообщите, что он является сильным. 
# В конец файла .csv должны добавляться только допустимые идентификаторы и пароли.

# Если пользователь выберет пункт 2, он должен будет ввести идентификатор пользователя. 
# Проверьте, существует ли идентификатор в списке. 
# Если это так, предложите пользователю изменить пароль и сохраните изменения в файле .csv. 
# Убедитесь в том, что программа только изменяет существующий пароль, а не создает новую запись.

# Если пользователь выберет пункт 3, выведите только идентификаторы пользователей без паролей.
# Наконец, при выборе пункта 4 программа должна завершиться.

import csv

# импортируем данные во временный список
def getList():
    file = list(csv.reader(open("password.csv")))
    temporary = []
    for row in file:
        temporary.append(row)
    return temporary

# Добавляем нового пользователя, с проверкой, что данного пользователя нету в списке
def createUserId(temporary):
    name = True
    while name == True:
        userID = input("Введите новый userID: ").lower()
        inList = False
        row = 0
        for x in temporary:
            if userID in temporary[row][0]:
                print(f'Данный userID занят')
                inList = True
            row += 1
        if inList == False:
            name = False
    return userID

def createPassword():
    symbol_list = ["!", "£", "$", "%", "^", "&", "*", "(",")", "?", "@", "#"]
    number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    tryAgain = True
    while tryAgain == True:
        score = 0
        uppList = False
        lowList = False
        symList = False
        numList = False
        password = input("Введите пароль: ")
        if len(password) >= 8:
            score += 1
        for row in password:
            if row.isupper():
                uppList = True
            if row.islower():
                lowList = True
            if row in symbol_list:
                symList = True
            if row in number_list:
                numList = True

        if uppList == True:
            score += 1
        if lowList == True:
            score += 1
        if symList == True:
            score += 1
        if numList == True:
            score += 1
        
        if score == 1 or score == 2:
            print(" Слабый пароль, его нужно улучшить!")
        if score == 3 or score == 4:
            print("Надёжный пароль, но его можно улучшить!")
            again = input("Улучшить пароль? (да/нет)").lower()
            if again == "нет":
                tryAgain = False
        else:
            return password
        


def findUser(temporary):
    nameAgain = True
    userID = ""
    while nameAgain == True:
        searchID = input("Введи ID пользователя для поиска: ").lower()
        inList = False
        row = 0
        for x in temporary:
            if searchID in temporary[row][0]:
                inList = True
            row += 1
        if inList == True:
            userID = searchID
            nameAgain = False
        else:
            print(f"{searchID} не в списке")
    return userID

def changePassword(userID, temporary):
    if userID != "":
        password = createPassword()
        user_id = userID.index(userID)
        temporary[user_id][1] = password
        myFile = open("password.csv", "w")
        x = 0
        for row in temporary:
            myFile.write(f"{temporary[x][0]}, {temporary[x][1]}\n")
            x += 1
        myFile.close()

def displayAllUser():
    temp = getList()
    x = 0
    for row in temp:
        print(temp[x][0])
        x += 1
    
def main():
    temp = getList()
    goAgain = True
    while goAgain == True:
        print("""
        1) Create a new User ID
        2) Change a password
        3) Display all User IDs
        4) Quit\n 
        """)
        select = int(input("Выберите действие: "))
        if select == 1:
            userID = createUserId(temp)
            password = createPassword()
            myFile = open("password.csv", "a")
            #newRecord = userID + ", "+ password + "\n"
            myFile.write(str(f"{userID},{password}\n"))
            myFile.close()
        elif select == 2:
            userID = findUser(temp)
            changePassword(userID, temp)
        elif select == 3:
            displayAllUser()
        elif select == 4:
            goAgain = False
        else:
            print("Некорректный ввод")
    

main()