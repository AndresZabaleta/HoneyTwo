import sqlite3

def create_table():
    conn = sqlite3.connect('apicultura.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS datos_apicultor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            numcol INTEGER NOT NULL,
            ubicacion TEXT NOT NULL,
            temperatura REAL NOT NULL,
            humedad REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
