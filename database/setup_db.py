import sqlite3

conn = sqlite3.connect("precos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS precos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    preco TEXT,
    data_coleta TEXT NOT NULL
)
""")

print("Tabela criada")
conn.commit()
conn.close()