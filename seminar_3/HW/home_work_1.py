# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# [1, 2, 3, 4, 5, 6, 7, 8, 9] -> для нечетных 25

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

def sum_list(my_list: list, odd: bool): # odd=True = нечетные, False = четные
    sum = 0
    for i in range(len(my_list)):      
        if odd and i%2 == 0: 
            sum = sum + my_list[i]
        elif not odd and i%2 != 0:
            sum = sum + my_list[i]
    if odd:        
        print('Сумма нечетных элементов: ', sum)
    else:
        print('Сумма четных элементов: ', sum)

sum_list(my_list, True) # Считаем сумму нечетных элементов

