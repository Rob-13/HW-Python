item1 = (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'})
item2 = (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'})
item3 = (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
lst_keys = []
lst_val1 = []
for key1, val1 in item1[1].items():
    lst_keys.append(key1)
    lst_val1.append(val1)
lst_val2 = []
for key2, val2 in item2[1].items():
    lst_val2.append(val2)
lst_val3 = []
for key3, val3 in item3[1].items():
    lst_val3.append(val3)

vals1, vals2, vals3, vals4 = zip(lst_val1, lst_val2, lst_val3)

print(f'{lst_keys[0]}: {vals1}, \n{lst_keys[1]}: {vals2}, \n{lst_keys[2]}: {vals3},  \n{lst_keys[3]}: {set(vals4)}')