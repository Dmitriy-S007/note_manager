import os

def save_notes_to_file(notes, filename):

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for note in notes:
                file.write(f"username: {note.get('username')}\n")
                file.write(f"title: {note.get('title')}\n")
                file.write(f"content: {note.get('content')}\n")
                file.write(f"status: {note.get('status')}\n")
                file.write(f"created_date: {note.get('created_date')}\n")
                file.write(f"issue_date: {note.get('issue_date')}\n")
                file.write("---\n")
        print(f"Заметки успешно сохранены в файл '{filename}'")
    except Exception as e:
        print(f"Критическая ошибка при сохранении в файл '{filename}': {e}")


def load_notes_from_file(filename):

    notes = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        if not content:
            print("Файл пуст.")
            return notes

        notes_raw = content.strip().split('---\n')

        for note_raw in notes_raw:
            note = {}
            lines = note_raw.strip().split('\n')

            for line in lines:
                if ': ' in line:
                    try:
                        key, value = line.split(': ', 1)
                        key = key.lower().replace(' ', '_')
                        note[key] = value.strip()
                    except ValueError:
                        print(
                            f"Ошибка при чтении файла '{filename}'. Проверьте его содержимое. Некорректная строка: {line}")
                        return []
            if note:
                if not all(key in note for key in
                           ["username", "title", "content", "status", "created_date", "issue_date"]):
                    print(
                        f"Ошибка при чтении файла '{filename}'. Проверьте его содержимое. Не все обязательные поля найдены в заметке: {note}")
                    return []
                notes.append(note)

        print(f"Заметки успешно загружены из файла '{filename}'.")
        return notes

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Создан новый файл.")
        open(filename, 'w').close()
        return []
    except Exception as e:
        print(f"Критическая ошибка при чтении файла '{filename}': {e}")
        return []


if __name__ == "__main__":
    filename = "notes.txt"

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

    # Пример загрузки
    loaded_notes = load_notes_from_file(filename)
    if loaded_notes:
        print("Загруженные заметки:", loaded_notes)