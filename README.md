# Помощник библиотекаря

## Описание
Это приложение представляет собой систему управления библиотекой, которая позволяет библиотекарю вести учет книг, читателей и транзакций, а также генерировать различные отчеты.

## Требования
- Python 3.7+
- PostgreSQL (см. ниже по настройке базы данных)

## Установка и запуск
1. Установите необходимые библиотеки Python с помощью pip:

pip install -r requirements.txt

2. Настройте базу данных PostgreSQL:
- Создайте новую базу данных с именем "library".
- Используйте скрипт `create_tables.sql` для создания таблиц в базе данных.
- Запустите скрипт `insert_data.sql` для заполнения таблиц данными.
- В файле db_connector.py пропишите ваше имя пользователя и пароль 

3. Запустите основное приложение:

python main.py

## Использование
### Команды для библиотекаря
- `add_book_command`: Добавить книгу в базу данных.

python main.py add_book_command "Название книги" 1 "Жанр книги"

- `delete_book_command`: Удалить книгу из базы данных.

python main.py delete_book_command 1

- `update_book_command`: Изменить информацию о книге.

python main.py update_book_command 1 "Новое название" "Новый жанр"

- `report_summary_command`: Показать общую статистику библиотеки (количество книг и читателей).

python main.py report_summary_command

- `report_books_per_reader_command`: Показать, сколько книг взял каждый читатель.

python main.py report_books_per_reader_command

- `report_overdue_books_command`: Показать книги, не вернутые вовремя, и ожидаемую дату возврата.

python main.py report_overdue_books_command


## Автор
Степанов Дмитрий Игоревич 
