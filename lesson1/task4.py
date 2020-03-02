#n = input("Введите число: ")
n = 3739
if n < 10:
    print(n)
else:
    i = 0
    while n > 0:
        b = n % 10
        if i < b:
            i = b
        n /= 10
print(i)
