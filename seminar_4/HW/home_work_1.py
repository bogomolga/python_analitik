# 1. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

def write_to_file(s):
    path = 'poly.txt'
    data = open(path, 'a', encoding="utf8") # 'a' - append, закрывает файл автоматически
    data.write(f"{s}\n")
    #data.close()

def ask_for_positiv_number(s):
    num = int(input(s))
    if num < 0:
        return -1
    else:
        return num

def create_mnogochlen(k):
    equation = {} # словарь
    for i in range(k, -1, -1): # от k до 0 с шагом -1 (по убыванию)
        equation[i] = random.randint(0,100) # для каждого ключа генерим рандомно значения
    #print(equation)
    eq_str = ''
    for k,v in equation.items():
        if k == 1:
            eq_str += f'{v}*x + '
        elif k == 0:
            eq_str += f'{v} + '
        else:
            eq_str += f'{v}*x^{k} + '
    else:
        eq_str = eq_str[:-3]
    eq_str += ' = 0'
    print("многочлен: ", eq_str)
    return eq_str

for i in range(3):
    k = ask_for_positiv_number('Введите максимальную степень > 0: ')
    if k == -1:
        print("Некорректные входные данные")
        break
    elif k == 0:
        print("многочлен: 0 = 0")
    else:
        write_to_file(create_mnogochlen(k))





    



