# 2. В файле записаны N натуральных чисел(0 до N), упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# использовать map и list comprehensions и zip

from pathlib import Path

path = Path("C:\\", "Users", "Olga", "Documents", "!Обучение GB", "progs", "python_analitik", "seminar_5", "text_task2.txt") 
print(str(path))

try:
    my_abs_path = path.resolve(strict=True)
    
except FileNotFoundError:
    print('файла нет')  # doesn't exist
else:
    data = open(path,'r', encoding="utf8")
    text = data.read().split() #содержимое файла приводим к типу list с разбивкой по пробелам - split()
    print(text)
    text = list(map(int, text))
    print(text)
    digit = [text[x] - 1 for x in range(1, len(text)) if text[x] - 1 != text[x-1]]
    print(digit)

# >> [7]

# Вариант 2: с использованием zip. Найдет только одно пропущенное число
true_text = [x for x in range(1, len(text))] # вместо [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list(zip(text, true_text))
for item in new_list:
    if item[0] != item[1]:
        print(item[1])
        break

# >> 7

# Вариант 3: ошибку с путем выдает

path2 = r'data/text_task2.txt'  # r - сырая строка - означает, что берем текст как текст
with open(path2, 'r') as data2:
    s = data2.read().split()
s = list(map(int, s))
s = [s[x] - 1 for x in range(1, len(s)) if s[x] - 1 != s[x-1]]
print(s)

# >> [5]