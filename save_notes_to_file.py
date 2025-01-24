import os

def save_notes_to_file(notes, filename):

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for note in notes:
                file.write(f"Имя пользователя: {note.get('username')}\n")
                file.write(f"Заголовок: {note.get('title')}\n")
                file.write(f"Описание: {note.get('content')}\n")
                file.write(f"Статус: {note.get('status')}\n")
                file.write(f"Дата создания: {note.get('created_date')}\n")
                file.write(f"Дедлайн: {note.get('issue_date')}\n")
                file.write("---\n")
        print(f"Заметки успешно сохранены в файл '{filename}'")
    except Exception as e:
         print(f"Критическая ошибка при сохранении в файл '{filename}': {e}")

if __name__ == '__main__':
    example_notes = [
        {
            'username': 'D',
             'title': '1',
             'content': 'ASD',
             'status': 'новая',
             'created_date': '18.01.2025',
             'issue_date': '25.01.2025'
        },
        {
            'username': 'D',
             'title': '2',
             'content': 'ABC',
             'status': 'новая',
             'created_date': '18.01.2025',
             'issue_date': '25.01.2025'
        }
    ]

    filename = "notes.txt"

    # Сохраняем заметки в файл
    save_notes_to_file(example_notes, filename)

    # Проверяем, создался ли файл и записались ли данные
    if os.path.exists(filename):
        print(f"\nФайл '{filename}' существует.")
    else:
        print(f"\nФайл '{filename}' не существует.")

    # Выводим содержимое файла на экран для проверки:
    with open(filename, "r", encoding="utf-8") as file:
        print(f"\nСодержимое файла '{filename}':")
        print(file.read())