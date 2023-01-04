# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

k = int(input('Введите целое число > 0: '))
my_list1 = []
my_list2 = []

for i in range(k+1):
    if i == 0:
        my_list1.append(i)
        my_list2.append(i+1)
        if k == 0:
            my_list2.pop(k)
    elif i == 1:
        my_list1.append(i)
        my_list2.append(i*-1)
        if k == 1:
            my_list2.pop(k)
    else:
        my_list1.append(my_list1[i-2] + my_list1[i-1])
        my_list2.append(abs(my_list2[i-2]) + abs(my_list2[i-1]))
        if i % 2 != 0:
            my_list2[i] = my_list2[i] * -1
        if i == k:
            my_list2.pop(k)

my_list2.reverse()
my_list2.extend(my_list1)
print(my_list2)


