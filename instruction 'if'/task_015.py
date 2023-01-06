# Задача_015

# Предложите пользователю ввести любимый цвет. Если он введет «red», «RED» или «Red», выведите сообщение «I like red too».
# В противном случае выведите сообщение «I don’t like [colour], I prefer red».

colour = input('Введите любой цвет: ')

if colour == 'red' or colour == 'RED' or colour == 'Red':
    print(f'«I like red too»')
else:
    print(f"«I don't like {colour}, I prefer red»")