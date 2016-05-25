#!/home/macke/anaconda3/bin/python3.5
import sqlite3

db_name = "save.db"

def create_table():
    "create the save file with it contents"
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
    "takes the values and save them in the database"
    with sqlite3.connect("save.db") as db:
        cursor = db.cursor()
        sql = "INSERT INTO save (Name, Position, ReadNote, NoteStatus, NotePos, BanditConvOver) VALUES (?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def select_data(id):
    "selects all the data in a specific save"
    with sqlite3.connect("save.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Save WHERE SaveID=?",(id,))
        save = cursor.fetchall()
        return save


def select_name_and_id():
    "selects the name and saveId from a specific save"
    with sqlite3.connect("save.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT Name, SaveID FROM Save")
        data = cursor.fetchall()
        return data

def update_data(data):
    "overwrites the data of a specific save"
    with sqlite3.connect("save.db") as db:
        cursor = db.cursor()
        sql = "UPDATE Save SET Position=?, ReadNote=?, NoteStatus=?, NotePos=?, BanditConvOver=? WHERE SaveID=?"
        cursor.execute(sql,data)
        db.commit()

def delete_data(id):
    "deletes a specific save"
    with sqlite3.connect("save.db") as db:
        cursor = db.cursor()
        sql = "DELETE FROM Save WHERE SaveID=?"
        cursor.execute(sql,(id,))
        db.commit()
