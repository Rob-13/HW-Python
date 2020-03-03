#str1 = input("Введите свою строку: ")
str1 = 'Ну ничего себе я попал на курс программирования'
for item in enumerate(str1.split()):
    print(f'{item[0]} - {item[1][:10]}')
