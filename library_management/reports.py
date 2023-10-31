def report_library_summary(conn):
    """
    Сгенерировать отчет о количестве книг и читателей в библиотеке.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    num_books = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM readers")
    num_readers = cursor.fetchone()[0]
    cursor.close()
    return num_books, num_readers

def report_books_per_reader(conn):
    """
    Сгенерировать отчет о количестве книг, взятых каждым читателем.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT readers.name, COUNT(book_transactions.book_id) "
                   "FROM readers "
                   "LEFT JOIN book_transactions ON readers.reader_id = book_transactions.reader_id "
                   "GROUP BY readers.name")
    result = cursor.fetchall()
    cursor.close()
    return result

def report_overdue_books(conn):
    """
    Сгенерировать отчет о количестве просроченных книг у каждого читателя.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT readers.name, COUNT(book_transactions.book_id) "
                   "FROM readers "
                   "LEFT JOIN book_transactions ON readers.reader_id = book_transactions.reader_id "
                   "WHERE book_transactions.transaction_type = 'выдача' "
                   "AND book_transactions.transaction_date < current_date - interval '30 days' "
                   "GROUP BY readers.name")
    result = cursor.fetchall()
    cursor.close()
    return result
