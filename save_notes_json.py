import json
import os

def save_notes_json(notes, filename):
    # Сохраняем заметки в формате json

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)
        print(f"Заметки успешно сохранены в файл '{filename}' в формате JSON")
    except Exception as e:
        print(f"Ошибка при сохранении заметок в файл '{filename}' в формате JSON: {e}")

if __name__ == '__main__':
    # Пример списка заметок
    example_notes = [
        {
            'username': 'Алексей',
            'title': 'Список покупок',
            'content': 'Купить продукты',
            'status': 'новая',
            'created_date': '27-11-2024',
            'issue_date': '30-11-2024'
        },
        {
            'username': 'Дмитрий',
            'title': 'Учеба',
            'content': 'решить домашнее задание',
            'status': 'в процессе',
            'created_date': '21.01.2025',
            'issue_date': '23.01.2025'
        }
    ]

    filename = "notes.json"

    # Сохраняем заметки в файл JSON
    save_notes_json(example_notes, filename)

    # Проверка создан ли файл и запись данных
    if os.path.exists(filename):
        print(f"\nФайл '{filename}' существует.")
    else:
        print(f"\nФайл '{filename}' не существует.")

    # Вывод содержимого файла для проверки
    with open(filename, 'r', encoding='utf-8') as file:
        print(f"\nСодержимое файла '{filename}':")
        print(file.read())