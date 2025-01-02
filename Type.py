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
