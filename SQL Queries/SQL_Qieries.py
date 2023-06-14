import sqlite3 as sql

sqliteConnection = sql.connect("MyDatabase.db")

sql_cursor = sqliteConnection.cursor()


# Задание a

print("""\na. Написать запрос, который выдаст все заявки, которые были отработаны после '2020-12-02 12:00:00'. 
Формат вывода должен быть следующим: номер заявки, имя пользователя, время отработки, название статуса.
Данные должны быть отсортированы по возрастанию по дате отработки.\n""")

sql_cursor.execute("""
    SELECT tt_number, Users.name, TIME(work_time), DATE(work_time), TTStatus.name FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    WHERE work_time > '2020-12-02 12:00:00'
    ORDER BY DATE(work_time) ASC;
""")

query1_result = sql_cursor.fetchall()

print("Query 1 Result:")

for row_index, row in enumerate(query1_result):

    print(' | '.join(str(item) for item in row))


print("\nВсе заявки со статусом 'Закрыта' после '2020-12-02 12:00:00'\n")

sql_cursor.execute("""
    SELECT tt_number, Users.name, TIME(work_time), DATE(work_time), TTStatus.name status_name FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    WHERE work_time > '2020-12-02 12:00:00' AND status_name = "Закрыта"
    ORDER BY DATE(work_time) ASC;
""")

query11_result = sql_cursor.fetchall()

print("Query 1.1 Result:")

for row_index, row in enumerate(query11_result):

    print(' | '.join(str(item) for item in row))

# Задание b

print("""\nb. Написать запрос, который выдаст все заявки, отработанные 'Петровой Марией' со статусом 'ожидание'.
Формат вывода должен быть следующим: номер заявки, имя пользователя, время отработки, название статуса.\n""")

sql_cursor.execute("""
    SELECT tt_number, Users.name username, TIME(work_time), TTStatus.name ttstatusname FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    WHERE username = "Петрова Мария" AND ttstatusname = "Ожидание";
""")

query2_result = sql_cursor.fetchall()

print("Query 2 Result:")

for row_index, row in enumerate(query2_result):

    print(' | '.join(str(item) for item in row))

# Задание c

print("""\nc. Написать запрос, который выдаст все заявки, отработанные сотрудниками с фамилией 'Иванов' со статусом 'ожидание'.
Формат вывода должен быть следующим: номер заявки, имя пользователя, время отработки, название статуса.
Данные должны быть отсортированы по убыванию по дате отработки.\n""")

sql_cursor.execute("""
    SELECT tt_number, Users.name username, TIME(work_time), TTStatus.name ttstatusname FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    WHERE username LIKE "%Иванов%" AND ttstatusname = "Ожидание"
    ORDER BY DATE(work_time) DESC;
""")

query3_result = sql_cursor.fetchall()

print("Query 3 Result:")

for row_index, row in enumerate(query3_result):

    print(' | '.join(str(item) for item in row))

# Задание d

print("""\nd. Написать запрос, который выдаст количество отработанных заявок по дням 
со статусом 'открыта' и 'ожидание' за период '2020-12-02' по '2020-12-04'.
Формат вывода должен быть следующим: дата в формате день-месяц-год, название статуса, количество заявок.\n""")

sql_cursor.execute("""
    SELECT strftime("%d-%m-%Y", DATE(work_time)), TTStatus.name, COUNT(*) FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    WHERE TTStatus.name IN ("Открыта", "Ожидание") AND DATE(work_time) BETWEEN "2020-12-02" AND "2020-12-04"
    GROUP BY DATE(work_time)
    ORDER BY DATE(work_time);
""")

query4_result = sql_cursor.fetchall()

print("Query 4 Result:")

for row_index, row in enumerate(query4_result):

    print(' | '.join(str(item) for item in row))


print("\nПредыдущий запрос с разделением по названию статуса запроса\n")

sql_cursor.execute("""
    SELECT strftime("%d-%m-%Y", DATE(work_time)), TTStatus.name, COUNT(*) FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    WHERE TTStatus.name IN ("Открыта", "Ожидание") AND DATE(work_time) BETWEEN "2020-12-02" AND "2020-12-04"
    GROUP BY DATE(work_time), TTStatus.name
    ORDER BY DATE(work_time);
""")

query4_1_result = sql_cursor.fetchall()

print("Query 4.1 Result:")

for row_index, row in enumerate(query4_1_result):

    print(' | '.join(str(item) for item in row))

# Задание e

print("""\ne. Написать запрос, который выведет всех пользователей и количество их заявок со статусом 'открыта' 
с сортировкой по имени пользователя.\n""")

sql_cursor.execute("""
    SELECT Users.name username, COUNT(TTStatus.name) counted_tickets FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    WHERE TTStatus.name = "Открыта"
    GROUP BY Users.name
    ORDER BY Users.name;
""")

query5_result = sql_cursor.fetchall()

print("Query 5 Result:")

for row_index, row in enumerate(query5_result):
    print(' | '.join(str(item) for item in row))


print("\nСотрудник(и), которые не вошли в предыдущий запрос по условиям\n")

sql_cursor.execute("""
    SELECT Users.name, 0 FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    
    WHERE Users.name NOT IN (
    SELECT tb1.username FROM 
    (SELECT Users.name username, COUNT(TTStatus.name) counted_tickets FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    WHERE TTStatus.name = "Открыта"
    GROUP BY Users.name
    ORDER BY Users.name) tb1
    )
    GROUP BY Users.name
    ORDER BY Users.name;
    
""")

query5_1_result = sql_cursor.fetchall()

print("Query 5.1 Result:")

for row_index, row in enumerate(query5_1_result):

    print(' | '.join(str(item) for item in row))

print("\nЗапрос включающий в себя всех сотрудников, независимо от количества запросов\n")

sql_cursor.execute("""
    SELECT Users.name username, COUNT(TTStatus.name) counted_tickets FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    WHERE TTStatus.name = "Открыта"
    GROUP BY Users.name
    
    UNION
    
    SELECT Users.name, 0 FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status

    WHERE Users.name NOT IN (
    SELECT tb1.username FROM 
    (SELECT Users.name username, COUNT(TTStatus.name) counted_tickets FROM TroubleTickets
    JOIN Users ON Users.id = TroubleTickets.user_id
    JOIN TTStatus ON TTStatus.id = TroubleTickets.tt_status
    WHERE TTStatus.name = "Открыта"
    GROUP BY Users.name
    ORDER BY Users.name) tb1
    )
    GROUP BY Users.name
    ORDER BY Users.name;

""")

query5_2_result = sql_cursor.fetchall()

print("Query 5.2 Result:")

for row_index, row in enumerate(query5_2_result):
    print(' | '.join(str(item) for item in row))


sqliteConnection.close()

