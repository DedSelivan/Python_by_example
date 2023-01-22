# Задача_085

# Предложите пользователю ввести имя, а затем сообщите, сколько в нем гласных букв.

name = input('Введите имя: ')
count = 0

for vowels in name:    
    if vowels.lower() == 'а' or vowels.lower() == 'я' or vowels.lower() == 'у' or vowels.lower() == 'ю' or vowels.lower() == 'о' or vowels.lower() == 'е' or vowels.lower() == 'ё' or vowels.lower() == 'э' or vowels.lower() == 'и' or vowels.lower() == 'ы':
       count += 1
print(f'Количество гласных букв в имени {name} равно {count}')