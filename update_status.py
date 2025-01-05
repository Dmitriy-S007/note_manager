note = []

username = input('Введите Ваше имя: ')
note.append(username)

titles = set()

while True:
    title = input("Введите заголовок (или оставьте пустым для завершения): ")

    if title:
        if title in titles:
            print("Этот заголовок уже был добавлен. Пожалуйста, введите другой заголовок.")
        else:
            titles.add(title)
    else:
        break
note.append(titles)

content = input('Введите описание заметки: ')
note.append(content)

available_statuses = ["В процессе", "Выполнено", "Отложено"]

while True:
    print("Выберите новый статус заметки:")
    for i, status in enumerate(available_statuses):
        print(f"{i + 1}. {status}")

    choice = input("Ваш выбор: ")

    if choice.isdigit() and 1 <= int(choice) <= len(available_statuses):
        selected_status = available_statuses[int(choice) - 1]
        note.append(selected_status) # Добавляем статус в note
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите номер из списка.")
print("\nСтатус заметки успешно обновлен на:", note[3])

created_date = input('Введите дату создания заметки, в формате dd.mm.yyyy: ')
note.append(created_date)

issue_date = input('Введите дату истечения срока заметки, в формате dd.mm.yyyy: ')
note.append(issue_date)

print("Имя пользователя:", note[0])
print("Содержание заметки:", note[2])
print("Статус:", note[3])
print("Дата создания заметки:", note [4][:5])
print("Дата истечения заметки:", note [5][:5])
print("\nЗаголовки заметки:")
for title in note[1]:
    print(f"- {title}")
