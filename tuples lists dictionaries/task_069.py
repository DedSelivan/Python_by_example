# Задача_069

# Создайте кортеж с названиями пяти стран. 
# Выведите все содержимое кортежа. 
# Предложите пользователю ввести название одной из этих стран и выведите индекс (то есть позицию в списке) 
# этого элемента кортежа.

country = ('Russia', 'India', 'Iran', 'Argentina', 'Mexico')
print(country)

question = (input('Введите название одной из стран: ')).title()
if question in country:
    print(f'индекс: {country.index(question)}')
else:
    print(f'Вы ввели другую страну :)')