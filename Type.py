# username - имя пользователя
# title - заголовок заметки
# content - описание заметки
# status - статус заметки
# created_date - дата создания заметки в формате "день-месяц-год", например "10-11-2024"
# issue_date - дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024"
'''Присвоите им соответствующие значения и напечатайте с помощью функции print в виде print("Описание переменной:", переменная),
например print("Имя пользователя:", username)
Это основные элементы нашей заметки, с которыми мы будем работать в будущем: изменять status, при выполнении заметки,
проверять issue_date, чтобы узнать, истекла ли дата выполнения, править content, если пользователь решил,
что описание недостаточно конкретное и т.д.'''

# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# print (f"Привет, {name} { surname}!")

# info = "а роза упала на лапу азора"
# print (info[2:7])
# print (info[::-1])
# print (info[::-3])
# print (info[11:6:-1])

# num1 = float(input('Введите первое чилсо: '))
# num2 = float(input('Введите второе чилсо: '))
# sum_result = num1 + num2
# print(f"Сумма чисел: {sum_result}")
# age = int(input('Введите Ваш возраст: '))
# if age >=18:
#     print('Доступ разрешён.')
# else:
#     print('Доступ запрещён.')

# first_name = input('Введите Ваше имя: ')
# last_name = input('Введите Вашу фамилию: ')
# age = int(input('Введите Ваш возраст: '))
# if age >=18:
#     print(f'Приятно познакомиться, {first_name} {last_name}! Доступ разрешён.')
# else:
#     print(f'Приятно познакомиться, {first_name} {last_name}! Доступ запрещён.')

# number = int(input('Введите число: '))
# if number == 10:
#     print('Вы ввели десять.')
# else:
#     print('Это не десять.')

# name = input('Введите Ваше имя: ')
# num1 = float(input('Введите Ваш возраст: '))
# sum_result = num1 + int (5)
# print (f'Через пять лет Вам будет: {sum_result}')

# username = input('Введите Ваше имя: ')
# print(f'Имя пользователя: {username}')
# title = input('Введите заголовок заметки: ')
# print(f'Заголовок заметки: {title}')
# content = input('Введите описание заметки: ')
# print(f'Описание заметки: {content}')
# status = input('Введите статус заметки: ')
# print(f'Статус заметки: {status}')
# created_date = input('Введите дату создания заметки, в формате dd.mm.yyyy: ')
# print(f'Дата создания: {created_date}')
# issue_date = input('Введите дату истечения срока заметки, в формате dd.mm.yyyy: ')
# print(f'Дата истечения заметки (дедлайн): {issue_date}')

# username = ('Дмитрий')
# print(f'Имя пользователя: {username}')
# title = ('Note_manager')
# print(f'Заголовок заметки: {title}')
# content = ('Блокнот для записей')
# print(f'Описание заметки: {content}')
# status = ('Активная')
# print(f'Статус заметки: {status}')
# created_date = ('28.12.2024')
# print(f'Дата создания: {created_date}')
# issue_date = ('28.01.2025')
# print(f'Дата истечения заметки (дедлайн): {issue_date}')

# info = [1, 2, 3]
# info2 = [1, 1.5, 'Строка', [4, 5, 'Cnhjrf2']]
# print (info)
# print (info2)

# names = [
#     'Misha', 'Vasya', 'Max',
#     'Galya', 'Kolya'
# ]
#
# names.sort()
# print(names)

# result = names.pop()
# print(result)
# print(names)

# names.append('ilya') - Добавляет в список

# print(names)
# print(names[1]) - Vasya
# print(names[::-1])

# result = names.count('Vasya')
# print(result) - кол-во

# from sys import getsizeof
# info = [1, 2, 3, 4, 5]
# info2 = (1, 2, 3, 4, 5)
# # 88 88 104
# # 64 72 80
# print(getsizeof(info))
# print(getsizeof(info2))

# text = "Привет, Python!"
# print(text.lower())  # привет, python!
# print(text.upper())  # ПРИВЕТ, PYTHON!
# print(text.capitalize())  # Привет, python!
# print(text.title())  # Привет, Python!
# print(text.swapcase())  # пРИВЕТ, pYTHON!

# text = "  Привет  "
# print(text.strip())  # "Привет" Удаление пробелов по краям
# print(text.lstrip())  # "Привет  " Удаление пробелов слева
# print(text.rstrip())  # "  Привет" Удаление пробелов справа

# text = "Я люблю Python, потому что Python лучший!"
# print(text.find("Python"))  # 8 (первое вхождение)
# print(text.rfind("Python"))  # 27 (последнее вхождение)
# print(text.replace("Python", "программирование"))
# # Я люблю программирование, потому что программирование лучший!

# text = "Разделяем эту строку на слова"
# words = text.split()  # ['Разделяем', 'эту', 'строку', 'на', 'слова']
# print("|".join(words))  # Разделяем|эту|строку|на|слова

# text = "42"
# print(text.zfill(5))  # 00042
# print(text.rjust(5))  # '   42'
# print(text.ljust(5, '*'))  # '42***'

# def is_palindrome(text):
#     cleaned = text.lower().replace(" ", "")
#     return cleaned == cleaned[::-1]
# print(is_palindrome("А роза упала на лапу Азора")) - true

# def longest_word(sentence):
#     words = sentence.split()
#     return max(words, key=len)
# print(longest_word("Это пример строки для тестирования"))
# # тестирования

# text = "Привет, Python!"
# text.join()

# first = {1, 2, 3, 4, 5, 1, 3, 5, 123, 5634} #множество
# second = {1, 2, 5, 1, 3, 5634}
# result = first.difference(second) #показывает отсутствующие значения
# result2 = (second.issubset(first)) #подмножесвто фалс/тру
# print (result2)

# first = {'Один': 1, 'Два': 2, 'Три': [1,2,3]}
# print(first['Три'])
# print(first.get('Пять'))
# print(first.items())
# print(first.values())
# print(first.keys())
# first['Три'] = 3
# print(first)

# empty_list = []  # Пустой список
# fruits = ["яблоко", "банан", "вишня"]
# print(empty_list, fruits)

# empty_tuple = ()  # Пустой кортеж
# numbers = (1, 2, 3)
# no_parentheses = 1, 2, 3  # Также кортеж
# single_element = (42,)  # Обязательно с запятой
# print(no_parentheses)

# fruits = ["яблоко", "банан", "вишня"]
# print(fruits[0])  # Вывод: яблоко
# print(fruits[-1]) # Вывод: вишня (обратный индекс)

# numbers = [1, 2, 3, 4, 5]
# print(numbers[1:4])  # Вывод: [2, 3, 4]
# print(numbers[:3])   # Вывод: [1, 2, 3]
# print(numbers[::2])  # Вывод: [1, 3, 5] (с шагом 2)

# print(len([1, 2, 3]))  # Вывод: 3
# print(len(("a", "b", "c")))  # Вывод: 3

#Оператор "in" проверяет, содержится ли элемент в коллекции.
# print("яблоко" in ["яблоко", "банан"])  # Вывод: True
# print(3 in (1, 2, 4))  # Вывод: False

# list1 = (1, 2)
# list2 = (3, 4)
# result = list1 + list2 #()+() либо []+[] / ()+[] - не работает
# print(result)  # Вывод: [1, 2, 3, 4]

#append(): добавляет элемент в конец списка.
#insert(): вставляет элемент в указанную позицию.
# fruits = ["яблоко", "банан"]
# fruits.append("вишня")
# print(fruits)  # Вывод: ["яблоко", "банан", "вишня"]
# fruits.insert(1, "апельсин")
# print(fruits)  # Вывод: ["яблоко", "апельсин", "банан", "вишня"]

# remove(): удаляет первое вхождение элемента.
# pop(): удаляет элемент по индексу (по умолчанию — последний).
# clear(): очищает список.
# fruits = ["яблоко", "банан", "вишня"]
# fruits.remove("банан")
# print(fruits)  # Вывод: ["яблоко", "вишня"]
# last_fruit = fruits.pop()
# print(last_fruit)  # Вывод: вишня
# print(fruits)      # Вывод: ["яблоко"]
# fruits.clear()
# print(fruits)      # Вывод: []

# index(): возвращает индекс первого вхождения элемента.
# count(): возвращает количество вхождений элемента.
# sort(): сортирует список на месте.
# sorted(): возвращает новый отсортированный список.
# numbers = [4, 2, 8, 1]
# numbers.sort()
# print(numbers)  # Вывод: [1, 2, 4, 8]
# print(sorted([3, 1, 2]))  # Вывод: [1, 2, 3] - работает без самого списка

# copy(): создаёт копию списка.
# original = [1, 2, 3]
# copy = original.copy()
# copy.append(4)
# print(original)  # Вывод original: [1, 2, 3]
# print(copy)  # Вывод copy: [1, 2, 3, 4]

# # extend(): добавляет элементы из другой коллекции.
# numbers = [1, 2, 3]
# numbers.extend([4, 5]) #при этом другая колекция нигде не прописана
# print(numbers)  # Вывод: [1, 2, 3, 4, 5]

# count(): возвращает количество вхождений элемента.
# index(): возвращает индекс первого вхождения элемента.
# colors = ("красный", "зелёный", "синий", "красный")
# print(colors.count("красный"))  # Вывод: 2
# print(colors.index("зелёный"))  # Вывод: 1

# numbers = [10, 20, 30]
# total = sum(numbers)
# print(total)  # Вывод суммы чисел из списка: 60

# duplicates = [1, 2, 2, 3, 4, 4] #удаление дубликатов
# unique = list(set(duplicates))
# print(unique)  # Вывод: [1, 2, 3, 4]

# #Используйте кортеж для хранения географических координат.
# coordinates = (55.7558, 37.6173)  # Москва
# print(f"Широта: {coordinates[0]}, Долгота: {coordinates[1]}")

#Оставьте в списке только чётные числа, вопрос как вывести нечетные.
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = [num for num in numbers if num % 2 == 0] #оставляет числа кратные 2
# print(even_numbers)  # Вывод: [2, 4, 6]

# #Создайте два списка: имена и оценки, затем объедините их в пары.
# names = ["Анна", "Борис", "Виктор", "Надя"]
# scores = [85, 90, 78]
# students = list(zip(names, scores))
# print(students)  # Вывод: [("Анна", 85), ("Борис", 90), ("Виктор", 78)] - Надя в список не вошла

# phone_book = {'Dima': 12345, 'Ira': 32154, 'Max': 54123}
# print(phone_book) #{'Dima': 12345, 'Ira': 32154, 'Max': 54123}
# print(phone_book['Dima']) #12345
# phone_book['Ira'] = 96325
# phone_book['Anton'] = 54321
# print(phone_book) #{'Dima': 12345, 'Ira': 96325, 'Max': 54123, 'Anton': 54321}
# del phone_book['Max']
# print(phone_book) #{'Dima': 12345, 'Ira': 96325, 'Anton': 54321}
# phone_book.update({'Sasha': 12378,
#                   'Alex': 87654})
# print(phone_book) #{'Dima': 12345, 'Ira': 96325, 'Anton': 54321, 'Sasha': 12378, 'Alex': 87654}
# print(phone_book.get('Kamila', 'Такого ключа нет')) #Такого ключа нет
# print(phone_book.get('Dima', 'Такого ключа нет')) #12345
# a = phone_book.pop('Alex')
# print(phone_book) #{'Dima': 12345, 'Ira': 96325, 'Anton': 54321, 'Sasha': 12378}
# print(a) #87654
# print(phone_book.keys()) #dict_keys(['Dima', 'Ira', 'Anton', 'Sasha'])
# print(phone_book.values()) #dict_values([12345, 96325, 54321, 12378])
# print(phone_book.items()) #dict_items([('Dima', 12345), ('Ira', 96325), ('Anton', 54321), ('Sasha', 12378)])
# phone_book['Ira'] = [96325, 32154]
# print(phone_book) #{'Dima': 12345, 'Ira': [96325, 32154], 'Anton': 54321, 'Sasha': 12378}

#set_ = {1, 2, 3, 4, 5, 4, 3, 2, 1,}
#print(set_) #{1, 2, 3, 4, 5}
# set_ = {1, 2, 3, 4, 5, 4, 3, 2, 1, 'String', True, (3,2,1)}
# print(set_) #{1, 2, 3, 4, 5, (3, 2, 1), 'String'}
# list = [1,1,3,1,2,3,2,3,4,5]
# print(set(list)) #{1, 2, 3, 4, 5}
# list = set(list)
# print(list) #{1, 2, 3, 4, 5}
# print(list.discard(2)) #None (discard - не выдает ошибку, если элемент не найден во множестве)
# print(list) #{1, 3, 4, 5}
# print(list.remove(4)) #None
# print(list) #{1, 3, 5}
# print(list.add(7))
# print(list) #{1, 3, 5, 7}
#list.pop('3') - команда .pop - не фурычит, хотя в лекции и написано, что можно...
#TypeError: set.pop() takes no arguments (1 given)
























