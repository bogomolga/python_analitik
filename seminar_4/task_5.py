# 5. Работа с плавающей точкой через строку
# Посчитать сумму цифр в вещественном числе

number = 'uhfwey945738573reuhye.wuery7547' # может быть просто 0.96
summa = 0

for char in number:
    if char.isdigit():
        summa += int(char)
print(summa)


# Задача из ДЗ: Сформировать список по формуле (1+1/n)**n и посчитать сумму элементов
# При n=4 список = 2, 2.25, 2.37, 2.44
# сумма = 9.06

num = int(input('Введите целое число: '))
my_list = []
for n  in range(1, num+1): # здесь будет деление на 0. чтоб избежать в range вместо range(number) пишем range(1, number+1), т.е. от 1
    num2 = round((1+1/n)**n, 2)
    my_list.append(num2 if num2 != int(num2) else int(num2)) # тернарный оператор !!!

print(f'При n={num} список = ', end='')
print(*my_list, sep=', ')
print(f'И его сумма = {sum(my_list)}')


import random

# Задача из ДЗ: Перемешивание списка
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 9, 0, 2, 3, 4, 5, 6, 7, 8] перемешивание есть, но хреновое :)

def create_list():
    new_list = []
    for i in range(10):
        new_list.append(i)
    return new_list

my_list2 = create_list()

def my_shuffle(my_list: list):
    ni = random.randint(0, (len(my_list) - 1))
    for i in range(len(my_list)):
        my_list[i], my_list[ni] = my_list[ni], my_list[i] # перемешивание есть, но хреновое :) см. на скриншоте еще один пример перемешивания
    return my_list

print(my_list2)
print(my_shuffle(my_list2))
