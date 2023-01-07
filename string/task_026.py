# Задача_026

# В шифре «поросячья латынь» начальная согласная буква слова перемещается в конец слова, и к ней добавляется суффикс «ay». 
# Если слово начинается с гласной, к нему просто добавляется суффикс «way».
# Например, pig превращается в igpay, banana — в ananabay,а aardvark — в aardvarkway. 
# Напишите программу, которая предлагает пользователю ввести слово и преобразует его в «поросячью латынь». 
# Проследите за тем, чтобы новое слово выводилось в нижнем регистре.

my_word = input('Введите слово: ').lower()

# Англоязычная версия (a, e, i, o, u, y):

if my_word[0] != 'a'  and my_word[0] != 'e' and my_word[0] != 'i' and my_word[0] != 'o' and my_word[0] != 'u' and my_word[0] != 'y':
    new_word = my_word[1:len(my_word)] + my_word[0] + 'ау'
else:
    new_word = my_word + 'way'

print(new_word)

# Русскоязычная версия (а, я, у, ю, о, е, ё, э, и, ы):

# if my_word[0] != 'а'  and my_word[0] != 'я' and my_word[0] != 'у' and my_word[0] != 'ю' and my_word[0] != 'о' and my_word[0] # != 'е' and my_word[0] != 'ё' and my_word[0] != 'э' and my_word[0] != 'и' and my_word[0] != 'ы':
#     new_word = my_word[1:len(my_word)] + my_word[0] + 'ау'
# else:
#     new_word = my_word + 'way'
# 
# print(new_word)