# Задача_074

# Введите список из десяти цветов. 
# Предложите пользователю ввести начальное число в диапазоне от 0 до 4 и 
# конечное число в диапазоне от 5 до 9. 
# Выведите список цветов из интервала, заданного начальным и конечным числом. 

colours = []

for i in range(10):
    colours.append(input('Введите название цвета: '))
start, end = int(input('Введите начальное число в диапазоне от 0 до 4: ')), int(input('Введите конечное число в диапазоне от 5 до 9: '))
print(colours[start:end+1])
