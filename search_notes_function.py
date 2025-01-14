# Функция поиска заметок
def search_notes(notes, keyword=None, status=None):
    if not notes:
        print("Список заметок пуст.")
        return []

    found_notes = []

    for note in notes:
        # Проверка по ключевому слову
        keyword_match = False
        if keyword:
            keyword_lower = keyword.lower()
            if (keyword_lower in note.get('title', '').lower() or
                    keyword_lower in note.get('content', '').lower() or
                    keyword_lower in note.get('username', '').lower()):
                keyword_match = True
        else:
            keyword_match = True  # Если ключевое слово не указано, считаем, что условие выполнено

        # Проверка по статусу
        status_match = False
        if status:
            if note.get('status', '').lower() == status.lower():
                status_match = True
        else:
            status_match = True  # Если статус не указан, считаем, что условие выполнено

        # Если оба условия выполнены, добавляем заметку в результат
        if keyword_match and status_match:
            found_notes.append(note)

    return found_notes


def display_search_results(found_notes):
    if not found_notes:
        print("Заметки, соответствующие запросу, не найдены.")
        return

    print("Найдены заметки:")
    print("------------------------------")

    for i, note in enumerate(found_notes, start=1):
        print(f"Заметка №{i}:")
        print(f"Имя пользователя: {note.get('username')}")
        print(f"Заголовок: {note.get('title')}")
        print(f"Описание: {note.get('content')}")
        print(f"Статус: {note.get('status')}")
        print("------------------------------")


# Пример использования функции
if __name__ == "__main__":
    # Тестовый список заметок
    notes = [
        {
            'username': 'Алексей',
            'title': 'Список покупок',
            'content': 'Купить продукты на неделю',
            'status': 'новая',
            'created_date': '27-11-2024',
            'issue_date': '30-11-2024'
        },
        {
            'username': 'Мария',
            'title': 'Учеба',
            'content': 'Подготовиться к экзамену',
            'status': 'в процессе',
            'created_date': '25-11-2024',
            'issue_date': '01-12-2024'
        },
        {
            'username': 'Иван',
            'title': 'План работы',
            'content': 'Завершить проект',
            'status': 'выполнено',
            'created_date': '20-11-2024',
            'issue_date': '26-11-2024'
        }
    ]

    # Пример 1: Поиск по ключевому слову
    print("Пример 1: Поиск по ключевому слову 'покупок'")
    found_notes = search_notes(notes, keyword='покупок')
    display_search_results(found_notes)

    # Пример 2: Поиск по статусу
    print("\nПример 2: Поиск по статусу 'в процессе'")
    found_notes = search_notes(notes, status='в процессе')
    display_search_results(found_notes)

    # Пример 3: Комбинированный поиск
    print("\nПример 3: Поиск по ключевому слову 'работы' и статусу 'выполнено'")
    found_notes = search_notes(notes, keyword='работы', status='выполнено')
    display_search_results(found_notes)

    # Пример 4: Поиск без результатов
    print("\nПример 4: Поиск по ключевому слову 'отпуск'")
    found_notes = search_notes(notes, keyword='отпуск')
    display_search_results(found_notes)
