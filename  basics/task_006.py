# Задача_006

# Спросите, сколько кусков пиццы было у пользователя и сколько кусков он съел. 
# Вычислите, сколько кусков пиццы у него осталось, и выведите результат в форме, удобной для пользователя.

pizza_was = int(input('Сколько у пользователя было кусков пиццы: '))
pizza_ate = int(input('Сколько кусков пиццы съел пользователь: '))
print(f'{pizza_was - pizza_ate} куска(ов) пиццы осталось у пользователя')