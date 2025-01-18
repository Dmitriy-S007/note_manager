def load_notes_from_file(filename):

    notes = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()  # Читаем всё содержимое файла

        # Если файл пуст, возвращаем пустой список
        if not content:
            print("Файл пуст.")
            return notes

        # Разделяем содержимое на отдельные заметки
        notes_raw = content.strip().split('---\n')

        # Обрабатываем каждую заметку
        for note_raw in notes_raw:
            note = {}
            lines = note_raw.strip().split('\n')  # Разделяем заметку на строки

            # Обрабатываем каждую строку
            for line in lines:
                if ': ' in line:  # Проверяем, что строка содержит разделитель
                    key, value = line.split(': ', 1)  # Разделяем строку на ключ и значение
                    # Преобразуем ключ в формат словаря
                    key = key.lower().replace(' ', '_')
                    note[key] = value

            if note:  # Добавляем заметку в список
                notes.append(note)

        print(f"Заметки успешно загружены из файла '{filename}'.")
        return notes

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return notes
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return notes

if __name__ == '__main__':
    filename = "notes.txt"

    loaded_notes = load_notes_from_file(filename)

    if loaded_notes:
        print("Заметки, загруженные из файла:")
        for note in loaded_notes:
            print(note)
    else:
        print("Файл не найден или пуст.")