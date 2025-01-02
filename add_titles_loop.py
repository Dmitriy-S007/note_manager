titles = set()

while True:
    title = input("Введите заголовок (или оставьте пустым для завершения): ")

    if title:  # Проверяем, не пустой ли ввод
        if title in titles:
            print("Этот заголовок уже был добавлен. Пожалуйста, введите другой заголовок.")
        else:
            titles.add(title)
    else:
        break

print("\nЗаголовки заметки:")
for title in titles:
    print(f"- {title}")