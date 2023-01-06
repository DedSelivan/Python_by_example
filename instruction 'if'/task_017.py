# Задача_017

# Предложите пользователю ввести его возраст. 
# Если введенное значение равно 18 и более, выведите сообщение «You can vote»; 
# если 17 — сообщение «You can learn to drive»; 
# если 16 — сообщение «You can buy a lottery ticket». 
# Если значение меньше 16, выведите сообщение «You can go Trick-or-Treating».

age = int(input('Введите возраст: '))

if age >= 18:
    print(f'«You can vote»')
elif age == 17:
    print(f'«You can learn to drive»')
elif age == 16:
    print(f'«You can buy a lottery ticket»')
else:
    print(f'«You can go Trick-or-Treating»')