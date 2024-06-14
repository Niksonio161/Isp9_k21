from loader import conn, cursor


async def create_database():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        uid INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        phone_number TEXT,
        user_name TEXT,
        balance INTEGER,
        hours INTEGER,
        points INTEGER,
        is_admin BOOLEAN,
        telegram_id INTEGER UNIQUE
    )
    ''')

    # Создаем таблицу computers
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS computers (
        number_pc INTEGER PRIMARY KEY AUTOINCREMENT,
        status BOOLEAN,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(uid)
    )
    ''')
    # try:
    #     cursor.execute(
    #         '''INSERT INTO users VALUES (1, 'Никита', '+79612872957', '@Niksonio161', 0, 0, 0, True, 2095407388)''')
    # except:
    #     pass
    # Сохраняем изменения и закрываем соединение
    conn.commit()
