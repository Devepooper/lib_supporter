-- Таблица для хранения информации об авторах книг
CREATE TABLE authors (
    author_id serial PRIMARY KEY, -- Уникальный идентификатор автора
    name VARCHAR(255) -- Имя автора
);

-- Таблица для хранения информации о книгах
CREATE TABLE books (
    book_id serial PRIMARY KEY, -- Уникальный идентификатор книги
    title VARCHAR(255), -- Название книги
    author_id INT, -- Идентификатор автора книги
    genre VARCHAR(255) -- Жанр книги
);

-- Таблица для хранения информации о читателях
CREATE TABLE readers (
    reader_id serial PRIMARY KEY, -- Уникальный идентификатор читателя
    name VARCHAR(255), -- Имя читателя
    library_card_number VARCHAR(10) -- Номер библиотечной карточки читателя
);

-- Таблица для хранения информации о фактах взятия/возврата книг
CREATE TABLE book_transactions (
    transaction_id serial PRIMARY KEY, -- Уникальный идентификатор транзакции
    book_id INT, -- Идентификатор книги
    reader_id INT, -- Идентификатор читателя
    transaction_type VARCHAR(10), -- Тип транзакции ('выдача' или 'возврат')
    transaction_date DATE -- Дата транзакции
);
