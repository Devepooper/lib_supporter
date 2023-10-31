from db_connector import connect_to_db
from library_operations import (
    add_book,
    delete_book,
    update_book,
)
from reports import (
    report_library_summary,
    report_books_per_reader,
    report_overdue_books,
)
import click


def main():
    conn = connect_to_db()
    if conn:
        # Здесь можно взаимодействовать с базой данных
        add_book(conn, "Книга 3", 1, "Жанр 1")
        conn.close()

if __name__ == "__main__":
    main()


@click.group()
def library_cli():
    pass

@library_cli.command()
@click.argument("title")
@click.argument("author_id", type=int)
@click.argument("genre")
def add_book_command(title, author_id, genre):
    conn = connect_to_db()
    if conn:
        add_book(conn, title, author_id, genre)
        click.echo("Книга добавлена!")
        conn.close()

if __name__ == "__main__":
    library_cli()


@library_cli.command()
@click.argument("book_id", type=int)
def delete_book_command(book_id):
    conn = connect_to_db()
    if conn:
        delete_book(conn, book_id)
        click.echo("Книга удалена!")
        conn.close()


@library_cli.command()
@click.argument("book_id", type=int)
@click.argument("new_title")
@click.argument("new_genre")
def update_book_command(book_id, new_title, new_genre):
    conn = connect_to_db()
    if conn:
        update_book(conn, book_id, new_title, new_genre)
        click.echo("Данные книги обновлены!")
        conn.close()


@library_cli.command()
def report_summary_command():
    conn = connect_to_db()
    if conn:
        num_books, num_readers = report_library_summary(conn)
        click.echo(f"Количество книг в библиотеке: {num_books}")
        click.echo(f"Количество читателей: {num_readers}")
        conn.close()


@library_cli.command()
def report_books_per_reader_command():
    conn = connect_to_db()
    if conn:
        result = report_books_per_reader(conn)
        for reader, num_books in result:
            click.echo(f"{reader}: {num_books} книг")
        conn.close()


@library_cli.command()
def report_overdue_books_command():
    conn = connect_to_db()
    if conn:
        result = report_overdue_books(conn)
        for reader, num_books in result:
            click.echo(f"{reader}: {num_books} книг")
        conn.close()
