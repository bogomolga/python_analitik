#Дана функция:
#        f(x) = 5*x**2 + 10*x - 30
#Определить корни
#Найти интервалы, на которых функция возрастает
#Найти интервалы, на которых функция убывает
#Построить график
#Вычислить вершину
#Определить промежутки, на котором f > 0
#Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy.plotting import plot

limit = 10
step = 0.01
a, b, c = 5, 10, -30
xs = np.arange(-limit, limit, step) #последовательность

def func(xs):
    return a*xs**2 + b*xs + c  # 5*x**2 + 10*x - 30

def take_roots(a, b, c):
    discr = b**2 - 4*a*c  #дискриминант
    if discr > 0:
        x1 = (-b + discr**0.5)/(2*a)
        x2 = (-b - discr**0.5)/(2*a)
        return x1, x2
    elif discr == 0:
        x0 = -b/(2*a)
        return x0, x0 #кортеж
    else:
        return None, None #кортеж
print("Корни уравнения: ", take_roots(5,10,-30))
print("Корни уравнения: ", np.roots([5,10,-30]))

roots = take_roots(a, b, c)

min_x, min_y = 0, 0
min_y = min(func(xs)) #минимальный Y = -35.0
min_x = take_roots(a, b, c - min_y)[0]  #(-1.0, -1.0)

x_down = np.arange(-limit, min_x, step)
x_up = np.arange(min_x, limit, step)

x_down_positiv = np.arange(-limit, min(roots), step)
x_down_negativ = np.arange(min(roots), min_x, step)
x_up_negativ = np.arange(min_x, max(roots), step)
x_up_positiv = np.arange(max(roots), limit, step)


plt.rcParams['lines.linestyle'] = '-'
plt.plot(x_down_positiv, func(x_down_positiv), 'r', label='Убывание выше 0') #red
plt.plot(x_up_positiv, func(x_up_positiv), 'b', label='Возрастание выше 0') 
plt.rcParams['lines.linestyle'] = '--'
plt.plot(x_down_negativ, func(x_down_negativ), 'r', label='Убывание ниже 0') #blue
plt.plot(x_up_negativ, func(x_up_negativ), 'b', label='Возрастание ниже 0') #blue

plt.plot(roots[0], func(roots[0]), 'go', label=f'Корни ({round(min(roots), 2)}, {round(max(roots), 2)})') #green o
plt.plot(roots[1], func(roots[1]), 'go')

plt.plot(min_x, min_y, 'cx', label=f'Экстремум ({min_x}, {min_y})') #cyan x

plt.grid()
plt.legend()