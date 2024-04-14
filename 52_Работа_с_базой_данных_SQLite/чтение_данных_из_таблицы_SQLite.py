import sqlite3

DB_NAME = "52_Работа_с_базой_данных_SQLite/sqlite_db.db"

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty>=30"
    sql_cursor = sqlite_conn.execute(sql_request)
    # for record in sql_cursor:
    #     print(record[1])
    records = sql_cursor.fetchall()
    print(records)
