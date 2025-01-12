
# Функция для создания заметки и возврата словаря.
import datetime


def create_note():
    """Запрашивает у пользователя данные для создания заметки и возвращает словарь."""
    note = {}

    note['username'] = input('Введите имя пользователя: ')

    while True:
        title = input("Введите заголовок заметки: ")
        if title:
            note['title'] = title
            break
        else:
            print("Заголовок не может быть пустым.")

    while True:
        content = input("Введите описание заметки: ")
        if content:
            note['content'] = content
            break
        else:
            print("Описание не может быть пустым.")

    available_statuses = ["новая", "в процессе", "выполнена"]
    while True:
        print("Введите статус заметки:")
        for i, status in enumerate(available_statuses):
            print(f"{i + 1}. {status}")
        choice = input("Ваш выбор: ")
        if choice.isdigit() and 1 <= int(choice) <= len(available_statuses):
            note['status'] = available_statuses[int(choice) - 1]
            break
        else:
            print("Неверный ввод. Пожалуйста, введите номер из списка.")

    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%d-%m-%Y")
    note['created_date'] = formatted_date

    while True:
        issue_date = input(
            'Введите дату истечения срока заметки, в формате dd.mm.yyyy (или оставьте пустым для установки на неделю вперед): ')
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
                print("Неверный формат даты. Пожалуйста, введите дату в формате dd.mm.yyyy.")

    return note


if __name__ == "__main__":
    note = create_note()
    print("Заметка создана:", note)
