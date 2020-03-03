
summ = 0

def sum_of_users_lst(lst):
    lst = lst.split()
    summ1 = 0
    for el in lst:
        el = int(el)
        summ1 += el
    print(summ1)
    return summ1

sum_of_users_lst(input("dsf: "))