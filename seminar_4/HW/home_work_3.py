# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
# Генерация с целыми числами - [1.51, -7.1, -6, 7.4, 6.2, -8, 2.605, 0.9, -4.82, -1, -2.8, 2, -5.8, 4.487, -3.787, 9.872, -5.57, -1, -4.9, -3.97]

def generate_list(size: int):
    my_list = []
    for _ in range(size):
        amount = random.randint(0, 3)
        number = round(random.uniform(-10, 10), amount)
        if number == int(number):
            my_list.append(int(number))
        else:
            my_list.append(number)
    return my_list


def diff(item: float):
    m = str(item)
    list_num = m.split('.')
    return list_num


m_list = generate_list(int(input('Введите длину списка > 5 (желательно): ')))
print(m_list)
temp_list = []

for i in range(len(m_list)):
    number = diff(m_list[i])
    if len(number) > 1:  # Пропускаем целые числа мимо
        temp_list.append(int(number[1]))
print(temp_list)

max_num = temp_list[0]
min_num = temp_list[0]

for i in range(len(temp_list)):
    if temp_list[i] > max_num:
        max_num = temp_list[i]
    elif temp_list[i] < min_num:
        min_num = temp_list[i]

print('max= ', max_num)
print('min= ', min_num)
print('Разница между максимальным и минимальным значением: ', max_num - min_num)





    



