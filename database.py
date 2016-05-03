import sqlite3

db_name = "save.db"

def create_table():
    sql = """CREATE TABLE save
            (Name, TEXT,
            Position INTEGER,
            ReadNote BOOLEAN,
            NoteStatus TEXT,
            NotePos INTEGER,
            BanitConvOver BOOLEAN,
            SaveID INTEGER,
            PRIMARY KEY(SaveID)"""
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT NAME FROM SQLITE_MASTER WHERE NAME=?",("save",))
        result = cursor.fetchall()
        if len(result) == 1:
            return

        cursor.execute(sql)
        db.commit()
