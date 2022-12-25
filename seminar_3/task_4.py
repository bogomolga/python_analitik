# 4. Генерация списка с вещественными числами
 
import random

my_list=[]

# Генерация с целыми числами - [1.51, -7.1, -6, 7.4, 6.2, -8, 2.605, 0.9, -4.82, -1, -2.8, 2, -5.8, 4.487, -3.787, 9.872, -5.57, -1, -4.9, -3.97]
for _ in range(20):
    amount = random.randint(0,3)
    number = round(random.uniform(-10, 10), amount)
    if number == int(number):
        my_list.append(int(number))
    else:
        my_list.append(number)

print(my_list)

# Генерация с нулями - [3.3, -0.0, -2.334, 4.125, 7.2, -0.0, 10.0, 7.488, 9.0, 0.737]
my_list2=[]
for _ in range(10):
    amount2 = random.randint(0,3)
    my_list2.append(round(random.uniform(-10, 10), amount2))
print(my_list2)