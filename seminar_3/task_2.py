# 2. Напишите программу, которая определит позицию 2го вхождения строки в списке либо сообщит, что ее нет
# пример на скриншоте задача_2.png

my_list =['qwe', '123', 'qwe', 123, '0ytyty534qwe', '123']
print(my_list)
search = '123'
count=0
position=0

for item in my_list:
    if search==item:
        count+=1
    if count==2:
        break
    position+=1
else:
    print(f'Строка {search} НЕ входит в заданный список')
if count>=2:
    print(f'Строка {search} входит в заданный список на позиции {position}')
else:
    print('-1')
        
