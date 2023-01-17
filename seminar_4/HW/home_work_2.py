# 1. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. 

#### ПРИМЕР РЕШЕНИЯ:

# File 1:
# 77*x + 88 = 0
# 86*x^2 + 15*x + 17 = 0
# 29*x^3 + 46*x^2 + 0*x + 43 = 0

# File 2:
# 9*x + 81 = 0
# 44*x^2 + 31*x + 10 = 0
# 12*x^3 + 74*x^2 + 69*x + 93 = 0


# 8. Даны два файла, в каждом из которых находится запись многочлена. 

# Задача - сформировать файл, содержащий сумму многочленов.

num_1 = '83*x^2 + 43*x + 57 = 0'.replace(' ', '')
num_1 = num_1[:num_1.find('=')].split('+')
num_2 = '23*x^5 + 25*x^4 + 37*x^3 + 72*x^2 + 41*x + 52 = 0'.replace(' ', '')
num_2 = num_2[:num_2.find('=')].split('+')
num_all = num_1 + num_2

my_dict = {}

for elem in num_all:
    if 'x' not in elem:
        key = 0
    elif '^' not in elem:
        key = 1
    else:
        key = int(elem[elem.find('^') + 1:])
        
    if key > 0:
        if key in my_dict:
            my_dict[key] += int(elem[:elem.find('*')])
        else:
            my_dict[key] = int(elem[:elem.find('*')])
    else:
        if key in my_dict:
            my_dict[0] += int(elem)
        else:
            my_dict[0] = int(elem) 
    print(my_dict)

my_str = '' 
for key, value in sorted(my_dict.items(),reverse=True):
    if key == 0:
        my_str += str(value)
    elif key == 1:
        my_str += f'{value}*x + '
    else:
        my_str += f'{value}*x^{key} + '
    
my_str = my_str + ' = 0'





    



