import tkinter as tk
from tkinter import messagebox
from scraping.multiple_products import coletar_varios_produtos
from database.setup_db import inicializar_banco
from analysis.analyze_price import analisa_preco
from analysis.export_data import extrai_tabela
from gui.table import mostrar_tabela

# Inicializa o banco
inicializar_banco()

links = []  # lista temporária de links

def adicionar_link():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Aviso", "Informe um link!")
        return
    links.append(url)
    listbox_links.insert(tk.END, url)
    entry_url.delete(0, tk.END)

def rodar_scraper():
    if not links:
        messagebox.showwarning("Aviso", "Nenhum link adicionado!")
        return
    resultados = coletar_varios_produtos(links)
    msg = "\n".join([f"{r['nome']}: {r['preco']}" for r in resultados])
    messagebox.showinfo("Resultados", msg)

# GUI
root = tk.Tk()
root.title("Monitor de Preços - Amazon")

tk.Label(root, text="Link do Produto:").grid(row=0, column=0, padx=5, pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.grid(row=0, column=1, padx=5, pady=5)

btn_adicionar = tk.Button(root, text="Adicionar Link", command=adicionar_link)
btn_adicionar.grid(row=0, column=2, padx=5, pady=5)

listbox_links = tk.Listbox(root, width=70)
listbox_links.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

btn_scraper = tk.Button(root, text="Rodar Scraper", command=rodar_scraper)
btn_scraper.grid(row=2, column=0, columnspan=3, pady=10)

btn_analise = tk.Button(root, text="Ver Análise", command=analisa_preco)
btn_analise.grid(row=3, column=0, columnspan=1, pady=5)

btn_analise = tk.Button(root, text="Extrair", command=extrai_tabela)
btn_analise.grid(row=3, column=2, columnspan=3, pady=5)

btn_analise = tk.Button(root, text="Ver Tabela", command=mostrar_tabela)
btn_analise.grid(row=3, column=0, columnspan=5, pady=5)

root.mainloop()