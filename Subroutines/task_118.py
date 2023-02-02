# Задача_118

# Определите подпрограмму, которая предлагает пользователю ввести число и сохраняет его в переменной num. 
# Определите другую подпрограмму, которая использует значение num и проводит отсчет от 1 до этого числа.

def get_numb():
    num = int(input('Введите число: '))
    return num

def count(num):
    number = 1
    while number <= num:
        print(number)
        number += 1
def my_main():
    num = get_numb()
    count(num)

my_main()

