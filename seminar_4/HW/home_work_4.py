# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('Введите целое число > 0: '))
my_list = []
while n:    
    my_list.append(n % 2)
    n>>=1
my_list.reverse()
print(" ".join(map(str, my_list)).replace(" ", ""))
    

