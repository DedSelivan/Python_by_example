# Задача_051

# Выведите строки «There are [счетчик] green bottles hanging on the wall, [счетчик] green bottles hanging on the wall, 
# and if 1 green bottle should accidentally fall». 
# Затем выведите вопрос: «how many green bottles will be hanging on the wall?». 
# Если пользователь ответит правильно, выведите сообщение «There will be [счетчик] green bottles hanging on the wall». 
# Если пользователь ответит неправильно, выведите сообщение «No, try again», пока не будет дан правильный ответ. 
# Когда счетчик уменьшится до 0, выведите сообщение «There are no more green bottles hanging on the wall».

count = 10
while count > 0:
    print(f"""\n«There are {count} green bottles hanging on the wall, {count} green bottles hanging on the wall, 
and if 1 green bottle should accidentally fall»""")
    count -= 1
    quest = int(input(f'\n«how many green bottles will be hanging on the wall?» '))
    if quest == count:
        print(f'\n«There will be {count} green bottles hanging on the wall» ')
    else:
        while quest != count:
            quest = int(input('\n«No, try again» '))
print(f'\n«There are no more green bottles hanging on the wall»')
