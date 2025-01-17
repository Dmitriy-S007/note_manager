def save_notes_to_file(notes, filename):

    file = open(filename, 'w', encoding='utf-8')

    for note in notes:

        file.write(f"Имя пользователя: {note.get('username')}\n")
        file.write(f"Заголовок: {note.get('title')}\n")
        file.write(f"Описание: {note.get('content')}\n")
        file.write(f"Статус: {note.get('status')}\n")
        file.write(f"Дата создания: {note.get('created_date')}\n")
        file.write(f"Дедлайн: {note.get('issue_date')}\n")
        file.write("---\n")

    file.close()
