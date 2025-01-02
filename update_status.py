class Note:
    def __init__(self, status):
        self.status = status

    def check_status(self):
        return self.status

    def change_status(self, new_status):
        self.status = new_status


note = Note("новая")
print("Введите новый статус заметки: ", note.check_status())

new_status = input("Введите новый статус заметки: ")

note.change_status(new_status)
print("Статус заметки был изменен на: ", note.check_status())