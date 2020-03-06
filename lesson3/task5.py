
def sum_of_users_lst(lst):
    lst = lst.split()
    summ1 = 0
    for el in lst:
        if el.isdigit():
            el = int(el)
            summ1 += el
        else:
            continue
    return summ1


summ, stop = 0, 'stop'

# Цикл для зацикливания ввода
while True:
    numbers = input('Введите список чисел (если нужно остановиться напишите stop): ')
    summ += sum_of_users_lst(numbers)
    print(summ)
    if stop in numbers:
        break


