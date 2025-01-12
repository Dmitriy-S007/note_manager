import datetime # Импортируем модуль Datetime, для работы с датами

notes = [] # Создаем список для будущих заметок

def create_note():
    # Создает новую заметку и возвращает ее в виде словаря.
    note = {}
    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    note['username'] = input('Введите Ваше имя: ')

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
    note['titles'] = titles

    note['content'] = input('Введите описание заметки: ')

    available_statuses = ["В процессе", "Выполнено", "Отложено"]
    while True:
        print("Выберите новый статус заметки:")
        for i, status in enumerate(available_statuses):
            print(f"{i + 1}. {status}")

        choice = input("Ваш выбор: ")
        if choice.isdigit() and 1 <= int(choice) <= len(available_statuses):
            note['status'] = available_statuses[int(choice) - 1]
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите номер из списка.")
    print("\nСтатус заметки успешно обновлен на:", note['status'])

    # Получаем текущую дату и форматируем ее
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%d.%m.%Y")
    note['created_date'] = formatted_date

    while True:
        issue_date = input('Введите дату истечения срока заметки, в формате dd.mm.yyyy: ')
        try:
            datetime.datetime.strptime(issue_date, "%d.%m.%Y")
            note['issue_date'] = issue_date
            break
        except ValueError:
            print('Неверный формат даты (dd.mm.yyyy)')
    return note


def display_notes(notes):
    # Выводит список всех заметок.
    if not notes:
        print("Список заметок пуст.")
        return
    print("\nТекущие заметки:")
    for i, note in enumerate(notes, 1):
        print(f"\n{i}.")
        print(f"  Имя пользователя: {note['username']}")
        print(f"  Заголовки: {', '.join(note['titles'])}")
        print(f"  Описание: {note['content']}")
        print(f"  Статус: {note['status']}")
        print(f"  Дата создания: {note['created_date'][:5]}")
        print(f"  Дедлайн: {note['issue_date'][:5]}")
        if note['status'] != 'Выполнено':
            check_deadline(note['issue_date'])


def check_deadline(issue_date):
    # Проверяет, истёк ли дедлайн, и выводит соответствующее сообщение.
    try:
        today = datetime.date.today()
        issue_date_obj = datetime.datetime.strptime(issue_date, "%d.%m.%Y").date()
        days_difference = (issue_date_obj - today).days

        if days_difference < 0:
            print(f"  Внимание! Дедлайн истёк {-days_difference} дней назад.")
        elif days_difference == 0:
            print("  Внимание! Дедлайн сегодня.")
        else:
            print(f"  До дедлайна осталось дней - {days_difference}.")
    except ValueError:
        print("Неверный формат даты. Пожалуйста, введите дату в формате dd.mm.yyyy.")


def delete_note(notes):
    # Удаляет выбранные заметки пользователя.
    if not notes:
        print("Список заметок пуст, удалять нечего.")
        return

    criterion = input("Введите имя пользователя для удаления заметок (или 'все' для удаления всех): ")

    if criterion.lower() == 'все':
        notes.clear()
        print("Все заметки успешно удалены.")
        return

    user_notes = [note for note in notes if note['username'] == criterion]

    if not user_notes:
        print("Заметок с таким именем пользователя не найдено.")
        return

    print("\nЗаметки пользователя:")
    for i, note in enumerate(user_notes, 1):
        print(f"{i}. Заголовок: {', '.join(note['titles'])}, Описание: {note['content']}")

    while True:
        titles_to_delete = input("Введите заголовки заметок для удаления через запятую (или 'все' для удаления всех): ")
        if titles_to_delete.lower() == 'все':
            for note in user_notes:
                notes.remove(note)
            print("Все заметки пользователя успешно удалены")
            display_notes(notes)
            return
        titles_to_delete = titles_to_delete.split(",")
        titles_to_delete = [title.strip() for title in titles_to_delete]
        notes_to_delete = []
        for note in user_notes:
            if any(title in note['titles'] for title in titles_to_delete):
                notes_to_delete.append(note)

        if not notes_to_delete:
            print("Заметки с такими заголовками не найдены. Попробуйте еще раз")
            continue

        for note in notes_to_delete:
            notes.remove(note)

        print("Заметки успешно удалены.")
        display_notes(notes)
        return


while True:
    note = create_note()
    notes.append(note)
    add_another = input("Хотите добавить ещё одну заметку? (да/нет/y): ").lower()
    if add_another != "да" and add_another != "y":
        break

display_notes(notes)
delete_note(notes)