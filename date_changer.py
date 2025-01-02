username = input('Введите Ваше имя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания заметки, в формате dd.mm.yyyy: ')
issue_date = input('Введите дату истечения срока заметки, в формате dd.mm.yyyy: ')

temp_created_date = created_date[:6] # Создаем временную переменную
temp_issue_date = issue_date[:6] # Создаем временную переменную

print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки:", temp_issue_date)
