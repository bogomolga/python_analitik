# 1. Напишите программу, которая на вход принимает дробь и показывает первую цифру дробной части числа.
# 6,78 -> 7
# 5 -> Нет (выдает 0. надо дорабатывать)
# 0,34 -> 3

#====================================================================
# для корректной работы с плавающей точкой, чтоб не было погрешностей 
from decimal import Decimal
number=Decimal('0.56') 
#====================================================================

# вариант 1
n = float(input('Введите дробное (вещественное) число: '))
print(int(n*10%10))

# вариант 2
m=str(n)
list_num=m.split('.')
print(list_num)
if len(list_num) > 1: # проверяем число ли
    print(list_num[1][0]) # в строке символы тоже стоят на своих индексах, по split('.') мы делим на две подстроки и обращаемся ко второму числу [1]
else:                          # а в нем выбираем первое число [0]
    print('Число целое')                      # выдаст ошибку, если введут целое число

    







