# 2. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

my_list = []
n = int(input('Введите длину списка > 0: '))
if n < 0:
    print('Некорректный ввод')
else:
    sum = 0
    for i in range(1,n+1):
        num = (1+(1/i))**i
        my_list.append(round(num, 2))
        print('i= ',i)
        sum = sum + my_list[i-1]
    print('Получили список: ')
    print(my_list)
    print(sum)
