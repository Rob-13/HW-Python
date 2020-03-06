''' Решение со списками. Если честно, мне не нравится, слишком много повторяющегося кода

#mon = int(input('Введите номер месяца: '))
mon = 5
lst1 = [1, 2, 12]
lst2 = [3, 4, 5]
lst3 = [6, 7, 8]
lst4 = [9, 10, 11]
if mon in lst1:
    print("Зима")
elif mon in lst2:
    print("Весна")
elif mon in lst3:
    print("Лено")
else:
    print("Осень")
'''

# Решение циклами
seasons = {'Winter':[1, 2, 12], 'Spring': [3, 4, 5], 'Summer':[6, 7, 8], 'Autumn': [9, 10, 11]}
#mon = int(input('Введите номер месяца: '))
mon = 12
for key, val in seasons.items():
    if mon in val:
        print(key)
