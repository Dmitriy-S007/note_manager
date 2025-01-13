notes = [
    {
    'username': "Дмитрий",
    'title': "1",
    'content': "abc",
    'status': "новая",
    'created_date': "13.01.2025",
    'deadline': "20.01.2025"
    }
]

def display_notes(notes):
    if not notes:
        print("У Вас нет сохраненных заметок.")
        return

    print("Список заметок:")
    print("-----------------------------")

    for i, note in enumerate(notes, start=1):
        print(f"Заметка №{i}:")
        print(f"Имя пользователя: {note.get('username')}")
        print(f"Заголовок: {note.get('title')}")
        print(f"Описание: {note.get('content')}")
        print(f"Статус: {note.get('status')}")
        print(f"Дата создания: {note.get('created_date')[:5]}")
        print(f"Дедлайн: {note.get('deadline')[:5]}")
        print("------------------------------")

display_notes(notes)