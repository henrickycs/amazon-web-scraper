import sqlite3

def inicializar_banco():
    conn = sqlite3.connect("precos.db")
    cursor = conn.cursor()

    # Tabela de preços
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            preco TEXT,
            data_coleta TEXT
        )
    """)

    conn.commit()
    conn.close()