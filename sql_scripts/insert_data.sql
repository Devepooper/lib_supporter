-- Добавляем авторов
INSERT INTO authors (name) VALUES ('Автор 1');
INSERT INTO authors (name) VALUES ('Автор 2');

-- Добавляем книги
INSERT INTO books (title, author_id, genre) VALUES ('Книга 1', 1, 'Жанр 1');
INSERT INTO books (title, author_id, genre) VALUES ('Книга 2', 2, 'Жанр 2');
