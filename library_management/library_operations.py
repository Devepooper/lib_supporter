def add_book(conn, title, author_id, genre):
    """
    Добавить новую книгу в базу данных.
    """
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author_id, genre) VALUES (%s, %s, %s)", (title, author_id, genre))
    conn.commit()
    cursor.close()

def delete_book(conn, book_id):
    """
    Удалить книгу из базы данных по её идентификатору.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
    conn.commit()
    cursor.close()

def update_book(conn, book_id, new_title, new_genre):
    """
    Обновить информацию о книге в базе данных.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = %s, genre = %s WHERE book_id = %s", (new_title, new_genre, book_id))
    conn.commit()
    cursor.close()

def add_transaction(conn, book_title, user_name, transaction_type):
    """
    Добавить информацию о транзакции (выдача или возврат книги).
    """
    cursor = conn.cursor()
    cursor.execute("SELECT book_id FROM books WHERE title = %s", (book_title,))
    book_id = cursor.fetchone()[0]
    cursor.execute("SELECT reader_id FROM readers WHERE name = %s", (user_name,))
    reader_id = cursor.fetchone()[0]

    if transaction_type == "выдача":
        cursor.execute("INSERT INTO book_transactions (book_id, reader_id, transaction_type, transaction_date) VALUES (%s, %s, 'выдача', current_date)", (book_id, reader_id))
    elif transaction_type == "возврат":
        cursor.execute("INSERT INTO book_transactions (book_id, reader_id, transaction_type, transaction_date) VALUES (%s, %s, 'возврат', current_date)", (book_id, reader_id))

    conn.commit()
    cursor.close()
