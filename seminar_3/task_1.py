# 1. Есть список строк. Надо выяснить есть в данном списке строк определенное заданное число
# Ищем первое вхождение

my_list =['dfgddfg44dfgd', 'ggf458fgfg12', 'ty579', '0ytyty534']
print(my_list)
search = input('Введите искомое число: ')

for item in my_list:
    if search in item:
        print(f'Число {search} входит в заданный список')
        break
else:
    print(f'Число {search} НЕ входит в заданный список') # этот else не отработает есть сработает break ! Либо, если цикл ничего не нашел









