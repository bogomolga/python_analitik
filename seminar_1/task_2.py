# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

my_list = []

max_num = -100000000
for i in range (5):
    num=int(input(f'Введите {i+1} число: '))
    my_list.append(num) # добавляем с конец списка число
    if num > max_num:
        max_num=num
print('Максимальное число: ', max_num)
print(my_list)