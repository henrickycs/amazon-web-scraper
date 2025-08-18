import sqlite3

def salvar_preco(produto, preco, data):
    conn = sqlite3.connect("precos.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO precos (produto, preco, data_coleta)
        VALUES (?, ?, ?)
    """, (produto, preco, data))

    conn.commit()
    conn.close()