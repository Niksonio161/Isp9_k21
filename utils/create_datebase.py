from loader import conn, cursor


async def create_database():
    # Создаем таблицу с полями ФИО, номер телефона, пароль, баланс и баллы
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     full_name TEXT,
                     phone_number TEXT,
                     user_name TEXT,
                     balance REAL,
                     points INTEGER,
                     is_admin BOOLEAN,
                     telegram_id INTEGER UNIQUE)''')

    # Создаем таблицу с полями логин и пароль
    cursor.execute('''CREATE TABLE IF NOT EXISTS logins
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT,
                     password TEXT)''')

    # Сохраняем изменения и закрываем соединение
    conn.commit()


