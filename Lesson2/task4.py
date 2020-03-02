#str1 = input("Введите свою строку: ")
str1 = 'Ну ничего себе я попал на курс программирования'
i = 1
for item in str1.split():
    print(f'{i} - {item[:10]}')
    i += 1

