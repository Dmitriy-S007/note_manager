username = input('Введите Ваше имя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания заметки, в формате dd.mm.yyyy: ')
issue_date = input('Введите дату истечения срока заметки, в формате dd.mm.yyyy: ')

print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print(f"Дата создания заметки: {created_date[:6]}")
print(f"Дата истечения заметки: {issue_date[:6]}")