def add_user(conn, name, library_card_number):
    """
    Добавить нового пользователя в базу данных.
    """
    cursor = conn.cursor()
    cursor.execute("INSERT INTO readers (name, library_card_number) VALUES (%s, %s)", (name, library_card_number))
    conn.commit()
    cursor.close()

def delete_user(conn, name):
    """
    Удалить пользователя из базы данных по имени.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM readers WHERE name = %s", (name,))
    conn.commit()
    cursor.close()

def update_user(conn, name, new_name, new_library_card_number):
    """
    Обновить информацию о пользователе в базе данных.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE readers SET name = %s, library_card_number = %s WHERE name = %s", (new_name, new_library_card_number, name))
    conn.commit()
    cursor.close()