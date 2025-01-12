# Создаем возможность менять данные заметки

import datetime

note = {
        'username': 'D',
        'title': '1',
        'content': 'A',
        'status': 'новая',
        'created_date': '12.01.2025',
        'issue_date': '19.01.2025'
    }


def update_note(note):
    """Позволяет пользователю обновить поле заметки."""
    print("\nТекущие данные заметки:")
    print(note)

    while True:
        field_to_update = input(
            "Какие данные вы хотите обновить? (username, title, content, status, issue_date): ").lower()
        if field_to_update in ["username", "title", "content", "status", "issue_date"]:
            break
        else:
            print("Неверное имя поля. Пожалуйста, выберите из списка: username, title, content, status, issue_date")

    if field_to_update == "issue_date":
        while True:
            new_value = input(f"Введите новое значение для {field_to_update} (день-месяц-год): ")
            try:
                datetime.datetime.strptime(new_value, "%d.%m.%Y")
                note[field_to_update] = new_value
                break
            except ValueError:
                print("Неверный формат даты. Пожалуйста, введите дату в формате день.месяц.год")
    elif field_to_update == "status":
        available_statuses = ["В процессе", "Выполнена", "Отложено"]
        while True:
            print("Выберите новый статус заметки:")
            for i, status in enumerate(available_statuses):
                print(f"{i + 1}. {status}")

            choice = input("Ваш выбор: ")
            if choice.isdigit() and 1 <= int(choice) <= len(available_statuses):
                new_value = available_statuses[int(choice) - 1]
                note[field_to_update] = new_value
                break
            else:
                print("Некорректный ввод. Пожалуйста, введите номер из списка.")
    else:
        new_value = input(f"Введите новое значение для {field_to_update}: ")
        note[field_to_update] = new_value

    print("\nЗаметка обновлена:")
    print(note)
    return note


if __name__ == "__main__":
    sample_note = dict(note)
    updated_note = update_note(sample_note)