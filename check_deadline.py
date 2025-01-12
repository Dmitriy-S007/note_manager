import datetime

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
        note.append(selected_status)
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите номер из списка.")
print("\nСтатус заметки успешно обновлен на:", note[3])

while True:
    created_date = input('Введите дату создания заметки, в формате dd.mm.yyyy: ')
    try:
      datetime.datetime.strptime(created_date, "%d.%m.%Y")
      break
    except ValueError:
      print('Неверный формат даты (dd.mm.yyyy)')
note.append(created_date)


while True:
    issue_date = input('Введите дату истечения срока заметки, в формате dd.mm.yyyy: ')
    try:
      datetime.datetime.strptime(issue_date, "%d.%m.%Y")
      break
    except ValueError:
      print('Неверный формат даты (dd.mm.yyyy)')
note.append(issue_date)


print("Имя пользователя:", note[0])
print("Содержание заметки:", note[2])
print("Статус:", note[3])
print("Дата создания заметки:", note [4][:5])
print("Дата истечения заметки:", note [5][:5])
print("\nЗаголовки заметки:")
for title in note[1]:
    print(f"- {title}")

# Функция для проверки дедлайна
def check_deadline(issue_date):
    """Проверяет, истёк ли дедлайн, и выводит соответствующее сообщение."""
    try:
        today = datetime.date.today()
        issue_date_obj = datetime.datetime.strptime(issue_date, "%d.%m.%Y").date()
        days_difference = (issue_date_obj - today).days

        if days_difference < 0:
            print(f"Внимание! Дедлайн истёк {-days_difference} дней назад.")
        elif days_difference == 0:
            print("Внимание! Дедлайн сегодня.")
        else:
            print(f"До дедлайна осталось дней - {days_difference}.")
    except ValueError:
        print("Неверный формат даты. Пожалуйста, введите дату в формате dd.mm.yyyy.")

# Вызов функции проверки дедлайна
check_deadline(note[5])