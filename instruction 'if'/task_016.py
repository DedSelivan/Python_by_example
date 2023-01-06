# Задача_016

# Спросите пользователя, идет ли дождь. Преобразуйте его ответ к нижнему регистру. 
# Если пользователь ответит «yes», спросите, ветрено ли на улице. 
# Если пользователь ответит «yes» и на второй вопрос, 
# выведите сообщение «It is too windy for an umbrella»; 
# в противном случае выведите сообщение «Take an umbrella». 
# Если же пользователь не дал положительного ответа на первый вопрос, выведите сообщение «Enjoy your day».

question = input('Идёт ли дождь? ')
question = str.lower(question)

if question == 'yes':
    new_question = input('Ветрено ли на улице? ')
    new_question = str.lower(new_question)
    if new_question == 'yes':
        print(f'«It is too windy for an umbrella»')
    else:
        print(f'«Take an umbrella»')
else:
    print(f'«Enjoy your day»')