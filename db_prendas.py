import sqlite3
DATABASE_NAME = "prendas.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS prendas(
                ID INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                talle REAL NOT NULL,
                precio REAL NOT NULL,
                material TEXT NOT NULL,
                color TEXT NOT NULL,
                descuento INTERGER
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)