my_list = [7, 5, 3, 3, 2]
#new_num = int(input('Введите новое число: '))
new_num = 8
i = 1
while my_list[i] >= new_num:
    i += 1
else:
    my_list.insert( i, new_num )
print(my_list)





#for item in my_list:
  #  if item >= new_num:
   #     i += 1
    #else:
     #   my_list.insert( i, new_num )


#print(my_list)