# 2. Сколько раз каждая цифра встречается в строке. Словари и Строки. Распарсить строку

my_dict = {}
num_str = '457394537956374657319759464064670685730453737403'

for dig in num_str:
    my_dict[dig] = my_dict.get(dig, 0) + 1

print(my_dict) # {'4': 8, '5': 7, '7': 9, '3': 8, '9': 4, '6': 6, '1': 1, '0': 4, '8': 1}



# 3. Найти корни квадратного уравнения. Коэффиценты А,В,С выдернуть из строки 'A*x**2 + B*x + C = 0', т.е. придумать универсальную формулу
# Проверку деления на 0 добавить
# in -> '32*x**2 + 4*x - 6 = 0' -> получить кортеж: (32, 4, -6)
import math
my_str = '-32*x**2 + 4*x - 6 = 0'

def conv(my_str):
    new_str = my_str.split('x')
    print(new_str)
    my_list = []
    for i in range(len(new_str)):
        my_list.append(new_str[i].replace(
            '**2', '').replace('*', '').replace(' ', '').replace('+', '').replace('=0', ''))
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    return my_list

my_list = []
my_list = conv(my_str)   
print(my_list)

# получаем [-32, 4, -6], далее это подставляем в формулу и вычисляем корни уравнения...


#from math import sqrt


def roots_equ(a,b,c):
    d = b ** 2 - 4 * a * c
    x1 = (-b + math.sqrt(d)) / a * 2
    x2 = (-b - math.sqrt(d)) / a * 2
    return d, x1, x2

print(roots_equ(my_list[0], my_list[1], my_list[2]))

#ValueError: math domain error