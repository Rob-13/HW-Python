# Решение для одног ослова

def int_func(word):
    lst = list(word)
    lst[0] = chr(ord(lst[0]) - 32)
    return ''.join(lst)


#word = input('Введите слово: ')
w = 'world'
print(int_func(w))

# Решение для предложения
#string = input('Type your text, please: ')
string = 'hello world it is a great day'
lst = string.split(' ')
lst1 =[]
for el in lst:
    lst1.append(int_func(el))
print(' '.join(lst1))
