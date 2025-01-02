
username = input('Введите Ваше имя: ')
title = input('Введите заголовок заметки: ')
title2 = input('Введите второй заголовок заметки: ')
title3 = input('Введите третий заголовок заметки: ')
info = [title, title2, title3]
content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания заметки, в формате dd.mm.yyyy: ')
issue_date = input('Введите дату истечения срока заметки, в формате dd.mm.yyyy: ')
note = [
    (f'Имя пользователя: {username}'),
    (f'Заголовок заметки: {info}'),
    (f'Описание заметки: {content}'),
    (f'Статус заметки: {status}'),
    (f'Дата создания: {created_date}'),
    (f'Дата изменения: {issue_date}')
]
print(note)
