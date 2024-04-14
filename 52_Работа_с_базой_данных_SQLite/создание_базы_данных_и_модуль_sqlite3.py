import sqlite3

DB_NAME = "52_Работа_с_базой_данных_SQLite/sqlite_db.db"

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite3)
#     print(sqlite3.version)

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS courses (
    id integer PRIMARY KEY,
    title text NOT NULL,
    students_qty integer,
    reviews_qty integer
    );"""
# PRIMATY KEY - это уникальный идентификатор для каждой записи в таблице базы данных. Он обеспечивает уникальность и быстрый доступ к данным.
# NOT NULL - это ограничение, указывающее, что столбец не может содержать значения NULL, то есть он должен всегда содержать какое-то значение.

sqlite_conn.execute(sql_request)
# execute() используется для выполнения SQL-запросов к базе данных.
