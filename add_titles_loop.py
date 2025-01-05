note = []

username = input('Введите Ваше имя: ')
note.append(username)

titles = set()

while True:
    title = input("Введите заголовок (или оставьте пустым для завершения): ")

    if title:  # Проверяем, не пустой ли ввод
        if title in titles:
            print("Этот заголовок уже был добавлен. Пожалуйста, введите другой заголовок.")
        else:
            titles.add(title)
    else:
        break

note.append(title)

content = input('Введите описание заметки: ')
note.append(content)

status = input('Введите статус заметки: ')
note.append(status)

created_date = input('Введите дату создания заметки, в формате dd.mm.yyyy: ')
note.append(created_date)

issue_date = input('Введите дату истечения срока заметки, в формате dd.mm.yyyy: ')
note.append(issue_date)

print("Имя пользователя:", note[0])
print("Содержание заметки:", note[2])
print("Статус:", note[3])
print("Дата создания заметки:", note [4][:6])
print("Дата истечения заметки:", note [5][:6])
print("\nЗаголовки заметки:")
for title in titles:
    print(f"- {title}")
