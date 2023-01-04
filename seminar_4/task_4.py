# 4. Найти корни квадратного уравнения. Коэффиценты А,В,С выдернуть из строки 'A*x**2 + B*x + C = 0', т.е. придумать универсальную формулу
# Рабочий вариант
# in -> '32*x**2 + 4*x - 6 = 0' -> получить кортеж: (32, 4, -6)

# in -> '32   *   x* *2 + 4  *x   - 6    = 0'
# out -> [32, 4, -6]
# in -> '32   *   x* *2 -  x   + 6    = 0'
# out -> [32, -1, 6]
# in -> ' x* *2 -  x   + 6    = 0'
# out -> [1, -1, 6]

import math

equation = '32   *   x* *2 + 4  *x   - 6    = 0'  # '32   *   x* *2 + 4  *x   - 6    = 0'

def create_koef(equation: str): # -> tuple:
    new_koef = []
    nq = equation.replace(' ','').replace('=0','').\
        replace('+',' ').replace('-',' -').split()
    for item in nq:
        if item.startswith('x'):
            new_koef.append(1)
        elif item.startswith('-x'):
            new_koef.append(-1)
        else:
            new_koef.append(int(item.split('*x')[0]))
    return new_koef
    print(new_koef)

create_koef(equation)

def solution(koef: list): # возвращает кортеж
    a, b, c = koef
    disc = b**2-4*a*c
    if disc>0:
        x1=(-b+math.sqrt(disc))/(2*a)
        x2=(-b-math.sqrt(disc))/(2*a)
        return round(x1,3), round(x2,3)  # кортеж. можно return 2, x1, x2 
    elif disc==0:
        x=-b/(2*a)
        return round(x, 3) # можно return 1, x, None
    else:
        return None # можно return 0, None, None

print(solution(create_koef(equation)))