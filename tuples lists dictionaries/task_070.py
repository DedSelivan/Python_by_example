# Задача_070

# Доработайте программу 069 так, чтобы она предлагала пользователю ввести число и выводила название страны, 
# находящейся в заданной позиции.

country = ('Russia', 'India', 'Iran', 'Argentina', 'Mexico')
print(country)

question = (int(input('Введите число от 0 до 4: ')))
print(country[question])