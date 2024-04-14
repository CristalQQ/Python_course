import sqlite3

DB_NAME = "52_Работа_с_базой_данных_SQLite/sqlite_db.db"

courses = [
    (351, "JavaScript", 415, 100),
    (614, "C++ course", 161, 10),
    (721, "Java full course", 100, 35)
]

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    for courses in courses:
        sqlite_conn.execute(sql_request, courses)
    sqlite_conn.commit()
# execute() - используется для выполнения SQL-запросов к базе данных.
# commit() - используется для подтверждения всех изменений, сделанных в базе данных с момента последнего вызова метода, для того, чтобы изменения стали постоянными и были записаны на диск.
