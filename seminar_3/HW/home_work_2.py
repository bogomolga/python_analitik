# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# [3, 8, 1, 4, 2, 5, 7, 9, 6] -> [18, 72, 7, 20, 4]
# [3, 8, 1, 4, 5, 7, 9, 6] -> [18, 72, 7, 20]

my_list = [3, 8, 1, 4, 2, 5, 7, 9, 6]
my_list_new = []
L = len(my_list) - 1
for i in range(L):
    if i != L-i and i < L-i:
        my_list_new.append(my_list[i] * my_list[L-i])
    elif i == L-i and i > L-i:
        my_list_new.append(my_list[i] * my_list[i])
        break
print(my_list)
print('Получили список c произведением пар чисел: ')
print(my_list_new)

