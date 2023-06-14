import sqlite3 as sql

print("Подключение к MyDatabase.db, если не существует будет создана новая...\n")

sqliteConnection = sql.connect("MyDatabase.db")

sql_cursor = sqliteConnection.cursor()

print("Создание таблицы Users...\n")

sql_cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(255)
    );""")

print("Заполнение таблицы Users...\n")

sql_cursor.execute("""
INSERT INTO Users (name)
VALUES ('Иванов Иван'),
       ('Петрова Мария'),
       ('Грачев Алексей'),
       ('Сидорова Екатерина'),
       ('Иванов Алексей');

    """)

sqliteConnection.commit()

print("Создание таблицы TTStatus...\n")

sql_cursor.execute("""
CREATE TABLE IF NOT EXISTS TTStatus (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(255)
    );""")


print("Заполнение таблицы TTStatus...\n")

sql_cursor.execute("""
INSERT INTO TTStatus (name)
VALUES ('Открыта'),
       ('Ожидание'),
       ('Закрыта');
    """)

sqliteConnection.commit()

print("Создание таблицы TroubleTickets...\n")

sql_cursor.execute("""
CREATE TABLE IF NOT EXISTS TroubleTickets (
    tt_number INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    work_time TIMESTAMP,
    tt_status INTEGER,
    FOREIGN KEY(user_id) REFERENCES Users(id),
    FOREIGN KEY(tt_status) REFERENCES TTStatus(id)
    );""")

print("Сброс нумирации столбца tt_number таблицы TTStatus (нумирация начнется с 1000)...\n")

sql_cursor.executescript("""

UPDATE sqlite_sequence SET seq = 999 WHERE name = 'TroubleTickets';

INSERT INTO sqlite_sequence (name,seq) SELECT 'TroubleTickets', 999 WHERE NOT EXISTS
           (SELECT changes() AS change FROM sqlite_sequence WHERE change <> 0);
""")

sqliteConnection.commit()

print("Заполнение таблицы TroubleTickets...\n")

sql_cursor.execute("""
INSERT INTO TroubleTickets (user_id, work_time, tt_status)
VALUES (1, '2020-12-01 11:05:00', 1),
       (3, '2020-12-01 09:10:00', 3),
       (2, '2020-12-01 13:12:00', 2),
       (4, '2020-12-02 13:02:00', 2),
       (1, '2020-12-02 15:36:00', 1),
       (5, '2020-12-02 19:55:00', 2),
       (2, '2020-12-03 10:40:00', 1),
       (1, '2020-12-04 12:15:00', 2),
       (4, '2020-12-05 15:15:00', 1),
       (5, '2020-12-05 15:36:00', 3),
       (3, '2020-12-05 18:17:00', 1),
       (1, '2020-12-06 09:01:00', 2);
    """)

sqliteConnection.commit()

sqliteConnection.close()