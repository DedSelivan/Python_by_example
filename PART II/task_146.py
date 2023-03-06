# Задача_146(Код сдвига)

# Код сдвига — один из самых простых кодов, который может использоваться для шифрования сообщений. 
# Каждая буква заменяется другой буквой, полученной сдвигом вперед по алфавиту на заданную величину. 
# Например, при сдвиге на один символ строка «abc» преобразуется в «bcd» (то есть каждая буква в алфавите 
# сдвигается вперед на одну позицию).

# Напишите программу, которая выводит следующее меню:
#      1) Make a code
#      2) Decode a message
#      3) Quit
#      Enter your selection:

# Если пользователь выбирает вариант 1, он получает возможность ввести сообщение (с пробелами), а затем число. 
# Python выводит закодированное сообщение, полученное с применением заданного сдвига.

# Если пользователь выбирает вариант 2, он вводит закодированное сообщение и правильное число, 
# а программа выводит декодированное сообщение (то есть смещается на нужное количество букв в обратном направлении по алфавиту).
# При выборе варианта 3 программа завершает работу.
# После того как пользователь закодирует или декодирует сообщение, меню выводится снова, 
# пока пользователь не завершит работу с программой.

alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
            'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
            'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

def getData():
    word = input('Введите сообщение: ').upper()
    number = int(input('Введите число от 1 до 33: '))
    if number == 0 or number > 33:
        while number == 0 or number > 33:
            number = int(input('Введите число от 1 до 33: '))
    data = (word, number)
    return data

def Make_a_code(word, number):
    newWord = ''
    for i in word:
        x = alphabet.index(i) + number
        if x > 33:
            x -= 34
        newWord += alphabet[x]
    print(newWord)
    print()

def decode_a_message(word, number):
    newWord = ''
    for i in word:
        x = alphabet.index(i) - number
        if x < 0:
            x += 34
        newWord += alphabet[x]
    print(newWord)
    print()

def main():
    repeat = True
    while repeat == True:
        print("""
        1) Make a code
        2) Decode a message
        3) Quit
        Enter your selection\n""")
        select = int(input('Выберите действие: '))
        if select == 1:
            word, number = getData()
            Make_a_code(word, number)
        elif select == 2:
            word, number = getData()
            decode_a_message(word, number)
        elif select == 3:
            repeat = False
        else:
            print('Некорректный выбор\n')

main()