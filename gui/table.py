import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "precos.db"))

def mostrar_tabela():
    tabela_win = tk.Toplevel()
    tabela_win.title("Histórico de Preços")
    tabela_win.geometry("700x400")

    colunas = ("Produto", "Preço", "Data")

    frame = tk.Frame(tabela_win)
    frame.pack(fill="both", expand=True)

    #Scrollbar
    scrollbar_y = tk.Scrollbar(frame, orient="vertical")
    scrollbar_x = tk.Scrollbar(frame, orient="horizontal")

    tree = ttk.Treeview(
        frame,
        columns=colunas,
        show="headings",
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=200, anchor="center")

    scrollbar_y.config(command=tree.yview)
    scrollbar_y.pack(side="right", fill="y")

    scrollbar_x.config(command=tree.xview)
    scrollbar_x.pack(side="bottom", fill="x")

    tree.pack(fill="both", expand=True)

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT produto, preco, data_coleta FROM precos ORDER BY data_coleta DESC")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            tree.insert("", tk.END, values=row)

    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível carregar dados: {e}")