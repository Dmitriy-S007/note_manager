Промежуточный итог:

1. Задание 1: Основные переменные

Созданы базовые переменные для заметки: username, title, content, status, created_date, issue_date.
Вывод значений организован через print.

2. Задание 2: Изменение формата вывода даты

Реализовано преобразование формата отображения дат для пользователя, исключив год при выводе переменных created_date и issue_date.

3. Задание 3: Ввод данных через input

Переменные инициализируются через пользовательский ввод (input).
Реализованы подсказки для пользователя о том, как вводить данные, включая формат дат.

4. Задание 4: Добавление списка заголовков

Пользователь вводит три заголовка, которые сохраняются в список.
Введенные данные отображаются, включая список заголовков.

5. Задание 5: Использование словаря

Все данные организованы в словарь для заметки, включая:
Поля: username, content, status, created_date, issue_date.
Список заголовков как значение ключа titles.

Все данные выводятся на экран в структурированном виде.

Итог: В результате выполнения всех заданий вы получите функциональную базу для работы с заметками, где каждый шаг улучшал структуру и удобство обработки данных. Все файлы должны быть доступны в репозитории note_manager.


Содержание финального задания этап 2

1. add_titles_loop.py: Цикл для добавления заголовков

Функциональность:
Запрашивает у пользователя заголовки.
Позволяет завершить ввод пустым вводом.
Выводит итоговый список добавленных заголовков.

Пример работы:

Введите заголовок (или оставьте пустым для завершения): 1
Введите заголовок (или оставьте пустым для завершения): 2
Введите заголовок (или оставьте пустым для завершения):

Заголовки заметки:

- 1
- 2


2. update_status.py: Проверка и обновление статуса заметки

Функциональность:
Предлагает изменить статус на один из предложенных.
Обрабатывает некорректный ввод.
Показывает текущий статус заметки.

Пример работы:

Выберите новый статус заметки:

1. в процессе
2. выполнено
3. отложено

Ваш выбор: 1

Статус заметки успешно обновлён на: "в процессе"


Выберите новый статус заметки:
1. В процессе
2. Выполнено
3. Отложено
Ваш выбор: актив
Некорректный ввод. Пожалуйста, введите номер из списка.
Выберите новый статус заметки:
1. В процессе
2. Выполнено
3. Отложено
Ваш выбор: 3
Статус заметки успешно обновлен на: Отложено


3. check_deadline.py: Обработка дедлайнов

Функциональность:
Получает текущую дату из системы.
Запрашивает дату дедлайна и сравнивает её с текущей датой.
Сообщает, истёк ли дедлайн или сколько дней осталось (при статусе заметки "выполнено" о просроченном дедлайне не сообщает, просто выводит дату дедлайна).
Проверяет корректность формата ввода.

Пример работы:

Текущая дата: 12.01.2025
Введите дату дедлайна (в формате день-месяц-год): 10.01.2025
Внимание! Дедлайн истёк 2 дня назад.

Текущая дата: 12.01.2025
Введите дату дедлайна (в формате день-месяц-год): 12.01.2025
Внимание! Дедлайн сегодня.

Текущая дата: 12.01.2025
Введите дату дедлайна (в формате день-месяц-год): 14.01.2025
Внимание! До дедлайна осталось 2 дней.


4. multiple_notes.py: Работа с несколькими заметками

Функциональность:
Создаёт несколько заметок через ввод данных (имя, заголовки, описание, статус, дедлайн).
Хранит заметки в списке словарей.
Выводит список всех заметок.

Пример работы:

Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.
Введите имя пользователя: Дмитрий
Введите заголовок заметки: 1
Введите описание заметки: абв
Введите статус заметки (в процессе, выполнено, отложено): новая
Введите дедлайн (день-месяц-год): 12.01.2025

Хотите добавить ещё одну заметку? (да/нет): нет


Список заметок:

1. Имя пользователя: Дмитрий
   Заголовки: 1
   Описание: абв
   Статус: В процессе
   Дата создания: 12.01.2025
   Дедлайн: 12.01.2025
   Внимание! Дедлайн сегодня.


5. delete_note.py: Удаление заметок

Функциональность:
Удаляет заметки по имени пользователя или заголовку, как отдельно по названию, так и через запятую, есть команда на удаление всех заметок либо всех заметок данного пользователя.
Выводит сообщение, если заметка не найдена.
Обновляет список заметок.

Пример работы:

Текущие заметки:

1.
  Имя пользователя: Дмитрий
  Заголовки: 1
  Описание: абв
  Статус: В процессе
  Дата создания: 12.01
  Дедлайн: 12.01
  Внимание! Дедлайн сегодня.

2.
  Имя пользователя: Дмитрий
  Заголовки: 2
  Описание: где
  Статус: Отложено
  Дата создания: 12.01
  Дедлайн: 13.01
  До дедлайна осталось дней - 1.

3.
  Имя пользователя: Ира
  Заголовки: 3
  Описание: жзи
  Статус: Выполнено
  Дата создания: 12.01
  Дедлайн: 10.01
Введите имя пользователя для удаления заметок (или 'все' для удаления всех): Дмитрий

Заметки пользователя:
1. Заголовок: 1, Описание: абв
2. Заголовок: 2, Описание: где

Введите заголовки заметок для удаления через запятую (или 'все' для удаления всех): 3
Заметки с такими заголовками не найдены. Попробуйте еще раз

Введите заголовки заметок для удаления через запятую (или 'все' для удаления всех): 1
Заметки успешно удалены.

Текущие заметки:

1.
  Имя пользователя: Дмитрий
  Заголовки: 2
  Описание: где
  Статус: Отложено
  Дата создания: 12.01
  Дедлайн: 13.01
  До дедлайна осталось дней - 1.

2.
  Имя пользователя: Ира
  Заголовки: 3
  Описание: жзи
  Статус: Выполнено
  Дата создания: 12.01
  Дедлайн: 10.01

Завершение этапа 3

1. create_note_function.py: Функция создания заметки

Функциональность:
Функция create_note() запрашивает данные у пользователя для создания заметки.
Формирует словарь с полями заметки, включая автоматическую генерацию текущей даты и автоматически подставляет дату дедлайна на неделю вперед при пустом вводе.
Проверяет корректность формата даты дедлайна.


2. update_note_function.py: Функция обновления заметки

Функциональность:
Функция update_note(note) принимает заметку (словарь) как аргумент.
Позволяет пользователю выбрать номер заметки, в которую необходимо внести изменения и выбрать поле для изменения.
Проверяет корректность ввода и обновляет выбранное поле.


3. display_notes_function.py: Функция отображения заметок

Функциональность:
Функция display_notes(notes) принимает список заметок.
Выводит каждую заметку в удобном формате.
Обрабатывает пустые списки заметок.


4. search_notes_function.py: Функция поиска заметок

Функциональность:
Функция search_notes(notes, keyword=None, status=None) ищет заметки по ключевым словам или статусу.
Возвращает список найденных заметок.
Выводит сообщение, если ничего не найдено.


5. menu.py: Меню действий

Функциональность:
Выводит интерактивное меню для выбора действий.
Обрабатывает выбор пользователя и вызывает соответствующую функцию.
Повторяет показ меню до тех пор, пока пользователь не выберет выход.
Добавлено визуальное разделение для улучшения читаемости, подтверждение при удалении заметки и цветное отображение меню и сообщений с помощью библиотеки colorama.

Доступные действия:
1: Создать новую заметку (create_note()).
2: Показать все заметки (display_notes()).
3: Обновить заметку (update_note()).
4: Удалить заметку (delete_note()).
5: Найти заметки (search_notes()).
6: Выйти из программы.


Завершение ЭТАП 4

1. Сохранение заметок в файл

Файл: save_notes_to_file.py

Описание задачи:

Создать функцию save_notes_to_file(notes, filename), которая:
Перезаписывает данные файла, записывая список заметок в текстовом формате.

Критерии:

Файл создаётся, если его не существует.
Все заметки записаны корректно.
Данные файла перезаписываются при каждом вызове функции.


2. Загрузка заметок из файла

Файл: load_notes_from_file.py

Описание задачи:

Создать функцию load_notes_from_file(filename), которая:
Читает заметки из текстового файла в формате YAML.
Преобразует данные в список словарей.

Критерии:

Возвращает список словарей.
Обрабатывает отсутствие файла: создаёт пустой файл и сообщает пользователю.
Работает корректно даже с пустым файлом.

3. Обработка ошибок при работе с файлами

Файл: File error handling.py

Описание задачи:

Добавить обработку ошибок в функции работы с файлами:

Если файл отсутствует:
Создать новый файл.
Вывести сообщение:

Файл filename не найден. Создан новый файл.

Если файл повреждён или данные некорректны:

Вывести сообщение:

Ошибка при чтении файла filename. Проверьте его содержимое.

Если возникают другие ошибки (например, отсутствие прав):
Вывести подробное сообщение об ошибке.
Корректно завершить выполнение программы.

4. Добавление данных в файл

Файл: append_notes_to_file.py

Описание задачи:
Создать функцию append_notes_to_file(notes, filename), которая:
Добавляет новые заметки в существующий файл, сохраняя старые данные.
Формат записи аналогичен save_notes_to_file, но файл открывается в режиме добавления.

Критерии:

Новые заметки добавляются в конец файла.
Старые данные остаются неизменными.
Файл создаётся автоматически, если он не существует.


5. Выбор формата файла

Файл: save_notes_json.py

Описание задачи:
Создать функцию save_notes_json(notes, filename), которая:
Сохраняет список заметок в формате JSON.
Записывает данные с отступами (indent=4) для удобства чтения.

Критерии:

Данные сохраняются в формате JSON.
Файл создаётся автоматически, если его не существует.
Форматирование сохраняется.
