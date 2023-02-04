#1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

my_string = 'Питон - сабвмый лучший в миреабв язык абв'
my_string2 = 'Питон - сабвмый лучший в миреабв язык абв'
my_string = my_string.split()
new_list = []
for word in my_string:
    if not 'абв' in word:
        new_list.append(word)

print(' '.join(new_list)) # join - объединяет список в одну строку (тип переменной должен быть string). Объединяющим элементом будет пробел


# Вариант 2: filter и lambda
new_list2 = list(filter(lambda word: not 'абв' in word, my_string))
print(' '.join(new_list2))


# Вариант 3: filter и lambda
new_list3 = list(filter(lambda word: not 'абв' in word, my_string2.split()))
print(' '.join(new_list3))


# Вариант 4: через list comprehensions
new_list4 = [x for x in my_string2.split() if not 'абв' in x]
print(' '.join(new_list4))


# результат работы одинаковый





