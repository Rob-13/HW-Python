#a = int(input('Введите количество секунд: '))
a = 112390
h = a // 3600
m = (a % 3600) // 60
s = (a % 3600) % 60
print(f'{h:02d}:{m:02d}:{s:02d}')
