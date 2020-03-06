#lst = input("Введите Ваш список: ")
lst = [1, 23, 42, 43, 47, 7776, 433, 334, 44, 56, 444, 'trrr']
i = 0
while i < len(lst) - 1:
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    i += 2
print(lst)
