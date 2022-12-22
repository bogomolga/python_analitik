# 2. Напишите программу, которая определит позицию 2го вхождения строки в списке либо сообщит, что ее нет
# пример на скриншоте задача_2.png
# Через функцию

my_list1 =['qwe', '123', 123, 'qwe', '0ytyty534qwe', '123'] # 'qwe' - ответ 3
my_list2 =['qwe', '123', 'qwe', 123, '0ytyty534qwe'] # '123' - ответ - нет
my_list3 =['qwe', '123', 'qwe', 123, '0ytyty534qwe', '123'] # '123' - ответ - 5
my_list4 =['qwe', '123', 'йцу', 123, '0ytyty534qwe', '123'] # 'йцу' - ответ - нет

def check(my_list: list, search: str):
    count=0
    for i in range(len(my_list)):
        if search == my_list[i]: # надо именно == а не in, т.к. ищем четкое совпадение, а не вхождение подстроки в строку !
            count+=1
            if count ==2:
                print(f'Второй индекс вхождения: {i}')
                break
    else:
        print('Второго вхождения нет')

check(my_list1, 'qwe')
check(my_list2, '123')
check(my_list3, '123')
check(my_list4, 'йцу')

print(my_list1.count('qwe')) # так можно посчить кол-во вхождений
print(my_list2.count('123'))
print(my_list3.count('123'))
print(my_list4.count('йцу'))