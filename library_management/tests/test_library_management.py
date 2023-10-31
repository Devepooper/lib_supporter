import unittest
from library_operations import (
    add_book, delete_book, add_user, delete_user,
    add_transaction, report_library_summary, 
    report_books_per_reader, report_overdue_books,
)
from db_connector import connect_to_db


class TestLibraryManagement(unittest.TestCase):
    def setUp(self):
        self.conn = connect_to_db()
    
    def tearDown(self):
        self.conn.close()

    def test_add_book(self):
        initial_book_count = self.get_book_count()
        add_book(self.conn, "Новая книга", "Новый автор", "Жанр")
        updated_book_count = self.get_book_count()
        self.assertEqual(updated_book_count, initial_book_count + 1)

    def test_delete_book(self):
        # Предварительно добавьте книгу для удаления
        add_book(self.conn, "Книга для удаления", "Автор", "Жанр")
        initial_book_count = self.get_book_count()
        delete_book(self.conn, "Книга для удаления")
        updated_book_count = self.get_book_count()
        self.assertEqual(updated_book_count, initial_book_count - 1)

    def test_add_user(self):
        initial_user_count = self.get_user_count()
        add_user(self.conn, "Новый пользователь", "Карточка")
        updated_user_count = self.get_user_count()
        self.assertEqual(updated_user_count, initial_user_count + 1)

    def test_delete_user(self):
        # Предварительно добавьте пользователя для удаления
        add_user(self.conn, "Пользователь для удаления", "Карточка")
        initial_user_count = self.get_user_count()
        delete_user(self.conn, "Пользователь для удаления")
        updated_user_count = self.get_user_count()
        self.assertEqual(updated_user_count, initial_user_count - 1)

    def test_add_transaction(self):
        # Предварительно добавьте книгу и пользователя
        add_book(self.conn, "Книга", "Автор", "Жанр")
        add_user(self.conn, "Пользователь", "Карточка")
        initial_transaction_count = self.get_transaction_count()
        add_transaction(self.conn, "Книга", "Пользователь", "выдача")
        updated_transaction_count = self.get_transaction_count()
        self.assertEqual(updated_transaction_count, initial_transaction_count + 1)

    def test_report_library_summary(self):
        # Тест для генерации отчета о количестве книг и читателей в библиотеке
        report = report_library_summary(self.conn)
        self.assertTrue(report)  # Проверяем, что отчет существует

    def test_report_books_per_reader(self):
        # Тест для генерации отчета о количестве книг, взятых каждым читателем
        report = report_books_per_reader(self.conn)
        self.assertTrue(report)  # Проверяем, что отчет существует

    def test_report_overdue_books(self):
        # Тест для генерации отчета о количестве просроченных книг
        report = report_overdue_books(self.conn)
        self.assertTrue(report)  # Проверяем, что отчет существует

    def get_book_count(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM books")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    def get_user_count(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM readers")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    def get_transaction_count(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM book_transactions")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

if __name__ == "__main__":
    unittest.main()
