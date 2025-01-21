import os

def append_notes_to_file(notes, filename):
    # Добавляет новые заметки в существующий файл в конец, не удаляя старые заметки.

    try:
        with open(filename, 'a', encoding='utf-8') as file:
            for note in notes:
                file.write(f"username: {note.get('username')}\n")
                file.write(f"title: {note.get('title')}\n")
                file.write(f"content: {note.get('content')}\n")
                file.write(f"status: {note.get('status')}\n")
                file.write(f"created_date: {note.get('created_date')}\n")
                file.write(f"issue_date: {note.get('issue_date')}\n")
                file.write("---\n")
        print(f"Заметки успешно добавлены в файл '{filename}'")
    except Exception as e:
        print(f"Критическая ошибка при добавлении заметок в файл '{filename}': {e}")

if __name__ == '__main__':
    filename = "notes.txt"

    # Пример списка заметок для добавления
    new_notes = [
        {
            'username': 'User3',
            'title': 'Note 3',
            'content': 'Content 3',
            'status': 'new',
            'created_date': '2024-12-03',
            'issue_date': '2024-12-12'
        },
        {
            'username': 'User4',
            'title': 'Note 4',
            'content': 'Content 4',
            'status': 'in progress',
            'created_date': '2024-12-04',
            'issue_date': '2024-12-13'
        }
    ]

    # Добавляем заметки в файл
    append_notes_to_file(new_notes, filename)

    # Проверка наличия файла и записи
    if os.path.exists(filename):
        print(f"\nФайл '{filename}' существует.")
    else:
        print(f"\nФайл '{filename}' не существует.")

    # Вывод содержимого файла для проверки
    with open(filename, "r", encoding="utf-8") as file:
        print(f"\nСодержимое файла '{filename}':")
        print(file.read())