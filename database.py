import sqlite3

db_name = "save.db"

def create_table():
    sql = """CREATE TABLE Save
            (Name TEXT,
            Position INTEGER,
            ReadNote BOOLEAN,
            NoteStatus TEXT,
            NotePos INTEGER,
            BanditConvOver BOOLEAN,
            SaveID INTEGER,
            PRIMARY KEY(SaveID))"""
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT NAME FROM SQLITE_MASTER WHERE NAME=?",("Save",))
        result = cursor.fetchall()
        if len(result) == 1:
            return
        cursor.execute(sql)
        db.commit()

def save_data(values):
    with sqlite3.connect("save.db") as db:
        cursor = db.cursor()
        sql = "INSERT INTO save (Name, Position, ReadNote, NoteStatus, NotePos, BanditConvOver) VALUES (?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def select_data(id):
    with sqlite3.connect("save.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Save WHERE SaveID=?",(id,))
        save = cursor.fetchall()
        return save


def select_name_and_id():
    with sqlite3.connect("save.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT Name, SaveID FROM Save")
        data = cursor.fetchall()
        return data

def update_data(data):
    with sqlite3.connect("save.db") as db:
        cursor = db.cursor()
        sql = "UPDATE Save SET Position=?, ReadNote=?, NoteStatus=?, NotePos=?, BanditConvOver=? WHERE SaveID=?"
        cursor.execute(sql,data)
        db.commit()
