def division(x, y):
    if y == 0:
        print('Деление на 0 невозможно!')
    else:
        print(x / y)


a = int(input("Введите делимое: "))
b = int(input('Введите делитель: '))

division(a, b)
