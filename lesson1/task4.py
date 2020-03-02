n = input("Введите число: ")
if int(n) < 10:
    print(n)
else:
    i = 0
    while i < len(n):
        if int(n[i]) > int(n[i+1]):
            max = n[i]
            i += 1
        else:
            max = n[i+1]
            i += 1
    print(max)
