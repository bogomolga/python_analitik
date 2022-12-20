# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

my_list = []
n = int(input('Введите длину списка > 0: '))
if n < 0:
    print('Некорректный ввод')
else:
    for i in range(n):
        my_list.append(i)
    print('Получили список: ')
    print(my_list)

    temp_list=my_list

    for i in range(len(my_list)):
        rnd = random.randint(0, n-1)
        #print('rnd= ', rnd)

        for j in range(len(my_list)):
            tmp_index=temp_list.index(rnd)
            tmp_item=temp_list[0]
            temp_list[0]=temp_list[tmp_index]
            temp_list[tmp_index]=tmp_item

    print('Получили список 2: ')
    print(temp_list)
