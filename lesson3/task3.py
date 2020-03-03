''' Решение по задаче

def remove_min_list(num1, num2, num3):
    lst = [num1, num2, num3]
    mini = 10000000000000
    for item in lst:
        if item <= mini:
            mini = item
    while mini in lst:
        lst.remove(mini)
    print(lst)


remove_min_list(23, 2, 423)
'''
# Решение со свободным числом аргументов

def remove_min_list(*args):
    lst = [*args]
    mini = 10000000000000
    for item in lst:
        if item <= mini:
            mini = item
    while mini in lst:
        lst.remove(mini)
    print(lst)


remove_min_list(23, 2, 423, 32, 4352, 3252550000, 324, 23, 1, 323, 234, 25235, 324)
