import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            database="library",
            user="your_user",  # Здесь укажите ваше имя пользователя
            password="your_password",  # Здесь укажите ваш пароль
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None