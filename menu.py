import datetime
from colorama import Fore, Style, init

# Использование colorama
init(autoreset=True)

# Глобальный список для хранения заметок
notes = []


def create_note():
    # Функция для создания заметок
    note = {}
    print(Fore.CYAN + '\nДобро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    note['username'] = input(Fore.YELLOW + 'Введите имя пользователя: ')

    while True:
        title = input(Fore.YELLOW + "Введите заголовок заметки: ")
        if title:
            note['title'] = title
            break
        else:
            print(Fore.RED + "Заголовок не может быть пустым.")

    while True:
        content = input(Fore.YELLOW + "Введите описание заметки: ")
        if content:
            note['content'] = content
            break
        else:
            print(Fore.RED + "Описание не может быть пустым.")

    available_statuses = ["новая", "в процессе", "выполнена"]
    while True:
        print(Fore.YELLOW + "Введите статус заметки:")
        for i, status in enumerate(available_statuses):
            print(Fore.YELLOW + f"{i + 1}. {status}")
        choice = input(Fore.YELLOW + "Ваш выбор: ")
        if choice.isdigit() and 1 <= int(choice) <= len(available_statuses):
            note['status'] = available_statuses[int(choice) - 1]
            break
        else:
            print(Fore.RED + "Неверный ввод. Пожалуйста, введите номер из списка.")

    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%d.%m.%Y")
    note['created_date'] = formatted_date

    while True:
        issue_date = input(
            Fore.YELLOW + 'Введите дату истечения срока заметки, в формате dd.mm.yyyy (или оставьте пустым для установки на неделю вперед): ')
        if not issue_date:
            issue_date_obj = current_date + datetime.timedelta(days=7)
            note['issue_date'] = issue_date_obj.strftime("%d.%m.%Y")
            break
        else:
            try:
                datetime.datetime.strptime(issue_date, "%d.%m.%Y")
                note['issue_date'] = issue_date
                break
            except ValueError:
                print(Fore.RED + "Неверный формат даты. Пожалуйста, введите дату в формате dd.mm.yyyy.")

    notes.append(note)
    print(Fore.GREEN + "\nЗаметка успешно создана!")
    return note


def display_notes(notes):
    # Вывод всего списка заметок
    if not notes:
        print(Fore.RED + "\nУ вас нет сохранённых заметок.")
        return

    print(Fore.CYAN + "\nСписок заметок:")
    print(Fore.CYAN + "-" * 20)
    for i, note in enumerate(notes, start=1):
        print(Fore.CYAN + f"Заметка №{i}:")
        print(Fore.YELLOW + f"Имя пользователя: {note.get('username')}")
        print(Fore.YELLOW + f"Заголовок: {note.get('title')}")
        print(Fore.YELLOW + f"Описание: {note.get('content')}")
        print(Fore.YELLOW + f"Статус: {note.get('status')}")
        print(Fore.YELLOW + f"Дата создания: {note.get('created_date')}")
        print(Fore.YELLOW + f"Дедлайн: {note.get('issue_date')}")
        print(Fore.CYAN + "-" * 20)


def update_note():
    # Изменение данных в заметке
    if not notes:
        print(Fore.RED + "\nУ вас нет заметок для обновления.")
        return

    display_notes(notes)
    try:
        note_index = int(input(Fore.YELLOW + "\nВведите номер заметки для обновления: ")) - 1
        if 0 <= note_index < len(notes):
            note = notes[note_index]
            print(Fore.CYAN + "\nТекущие данные заметки:")
            print(Fore.YELLOW + str(note))

            field_to_update = input(
                Fore.YELLOW + "Какие данные вы хотите обновить? (username, title, content, status, issue_date): ").lower()
            if field_to_update in ["username", "title", "content", "status", "issue_date"]:
                if field_to_update == "issue_date":
                    while True:
                        new_value = input(Fore.YELLOW + f"Введите новое значение для {field_to_update} (день.месяц.год): ")
                        try:
                            datetime.datetime.strptime(new_value, "%d.%m.%Y")
                            note[field_to_update] = new_value
                            break
                        except ValueError:
                            print(Fore.RED + "Неверный формат даты. Пожалуйста, введите дату в формате день.месяц.год.")
                elif field_to_update == "status":
                    available_statuses = ["в процессе", "выполнена", "отложена"]
                    while True:
                        print(Fore.YELLOW + "Выберите новый статус заметки:")
                        for i, status in enumerate(available_statuses):
                            print(Fore.YELLOW + f"{i + 1}. {status}")
                        choice = input(Fore.YELLOW + "Ваш выбор: ")
                        if choice.isdigit() and 1 <= int(choice) <= len(available_statuses):
                            note[field_to_update] = available_statuses[int(choice) - 1]
                            break
                        else:
                            print(Fore.RED + "Некорректный ввод. Пожалуйста, введите номер из списка.")
                else:
                    new_value = input(Fore.YELLOW + f"Введите новое значение для {field_to_update}: ")
                    note[field_to_update] = new_value

                print(Fore.GREEN + "\nЗаметка успешно обновлена!")
            else:
                print(Fore.RED + "Неверное имя поля. Пожалуйста, выберите из списка: username, title, content, status, issue_date")
        else:
            print(Fore.RED + "Неверный номер заметки.")
    except ValueError:
        print(Fore.RED + "Неверный ввод. Пожалуйста, введите число.")


def delete_note():
    # Удаление заметок
    if not notes:
        print(Fore.RED + "\nУ вас нет заметок для удаления.")
        return

    display_notes(notes)
    try:
        note_index = int(input(Fore.YELLOW + "\nВведите номер заметки для удаления: ")) - 1
        if 0 <= note_index < len(notes):
            confirm = input(Fore.RED + "Вы уверены, что хотите удалить эту заметку? (да/нет): ").lower()
            if confirm in ["да", "y"]:
                deleted_note = notes.pop(note_index)
                print(Fore.GREEN + f"\nЗаметка '{deleted_note.get('title')}' успешно удалена!")
            else:
                print(Fore.RED + "\nУдаление отменено.")
        else:
            print(Fore.RED + "Неверный номер заметки.")
    except ValueError:
        print(Fore.RED + "Неверный ввод. Пожалуйста, введите число.")


def search_notes():
    # Поиск заметок
    if not notes:
        print(Fore.RED + "\nУ вас нет заметок для поиска.")
        return

    keyword = input(Fore.YELLOW + "Введите ключевое слово для поиска (или оставьте пустым): ").lower()
    status = input(Fore.YELLOW + "Введите статус для поиска (или оставьте пустым): ").lower()

    found_notes = []
    for note in notes:
        keyword_match = not keyword or (
                keyword in note.get('title', '').lower() or
                keyword in note.get('content', '').lower() or
                keyword in note.get('username', '').lower()
        )
        status_match = not status or note.get('status', '').lower() == status

        if keyword_match and status_match:
            found_notes.append(note)

    if found_notes:
        print(Fore.CYAN + "\nНайденные заметки:")
        display_notes(found_notes)
    else:
        print(Fore.RED + "\nЗаметки, соответствующие запросу, не найдены.")


def show_menu():
    # Меню
    print(Fore.CYAN + "\n" + "=" * 40)
    print(Fore.CYAN + "Добро пожаловать в менеджер заметок")
    print(Fore.CYAN + "=" * 40)
    print(Fore.GREEN + "1. Создать новую заметку")
    print(Fore.GREEN + "2. Показать все заметки")
    print(Fore.GREEN + "3. Обновить заметку")
    print(Fore.GREEN + "4. Удалить заметку")
    print(Fore.GREEN + "5. Найти заметки")
    print(Fore.GREEN + "6. Выйти из программы")
    print(Fore.CYAN + "=" * 40)


def main_menu():
    while True:
        show_menu()
        choice = input(Fore.YELLOW + "\nВаш выбор: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            display_notes(notes)
        elif choice == "3":
            update_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            search_notes()
        elif choice == "6":
            print(Fore.GREEN + "\nПрограмма завершена. Спасибо за использование!")
            break
        else:
            print(Fore.RED + "\nНеверный выбор. Пожалуйста, выберите действие от 1 до 6.")


if __name__ == "__main__":
    main_menu()


