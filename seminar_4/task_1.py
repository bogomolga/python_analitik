# 1. Методы строк. Распарсить строку

my_string = '  \tПитон самый лучший в мире язык\n'

my_list = ['21', '34', '444', 'dsfsddf']
add = '-'

#new_string = my_string.split() #делит строку по определенному символу. не изменяет оригинал! надо присваивать значение новой переменной
                                # по-умолчанию делит строку по пробелу - split(' ')

#new_string = my_string.replace('и', '$') # заменить одно на другое значение
#new_string = my_string.replace(' ', '').replace('и', '!!!')  # множественные replace, можно много добавить

new_string = my_string.strip() # очищает строку в начале и в конце от ненужных символов. Уберет \t \n пробелы вначале строки. Полезно при чтении из файла
#new_string = my_string.lstrip() # чистит слева
#new_string = my_string.rstrip() # чистит справа

if new_string.lower().startswith('пит'):  # выдаст True
    print('Да, всё верно')

print(add.join(my_list)) # join - склеивает строки (тип переменной должен быть string)

print(my_string)
print(new_string)










