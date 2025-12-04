import sqlite3

# Путь к SQL-файлу
sql_file_path = '.sql'  # скорректируйте путь при необходимости

# Создаем соединение с базой данных
conn = sqlite3.connect('school.db')

# Открываем и читаем SQL скрипт
with open(sql_file_path, 'r', encoding='utf-8') as f:
    sql_script = f.read()

# Выполняем весь SQL скрипт
try:
    conn.executescript(sql_script)
    print("База данных успешно создана и заполнена данными.")
except sqlite3.Error as e:
    print(f"Ошибка при выполнении скрипта: {e}")

# Закрываем соединение
conn.close()