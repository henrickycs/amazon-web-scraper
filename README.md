# Amazon Web Scraper

**Monitore preços da Amazon facilmente com scraping automatizado, banco SQLite, GUI e análise visual.**

---

## Funcionalidades

- Adicione links de produto diretamente pela interface (o nome é extraído automaticamente via scraping).  
- Colete preços e salve automaticamente no banco de dados SQLite.  
- Consulte o histórico completo via tabela dinâmica com scrollbar.  
- Gere gráficos de evolução do preço ao longo do tempo.  
- Exporte os dados para CSV.

---

## Estrutura do Projeto
```bash
amazon-web-scraper/
│── analysis/
│   ├── analyze_price.py       # Geração de gráficos
│   ├── export_data.py         # Exportação em CSV
│
│── database/
│   ├── setup_db.py            # Inicialização do SQLite
│   └── insert_price.py        # Função para salvar dados
│
│── gui/
│   ├── app.py                 # Interface completa
│   └── table.py               # Janela com tabela de histórico
│
│── scraping/
│   └── multiple_products.py   # Scraping (nome + preço → banco)
│
│── precos.db                  # SQLite database
│── requirements.txt           # Lista de dependências
```


---

## Tecnologias

- **Python 3.10+**  
- **Bibliotecas**:
  - `requests`, `beautifulsoup4` – scraping  
  - `sqlite3` – armazenamento local  
  - `pandas`, `matplotlib` – análise e gráficos  
  - `tkinter`, `ttk` – interface gráfica  

---

## Como Rodar

- Clone o repositório:  
```bash
   git clone https://github.com/seu-usuario/amazon-web-scraper.git
   cd amazon-web-scraper
```

- Instale as dependências:
```bash
pip install -r requirements.txt
```

- Execute a interface gráfica:
```bash
python gui/app.py
```

# Uso da GUI

 - `Adicionar Link` → insira o link da Amazon e clique em “Adicionar Link”.

- `Rodar Scraper` → coleta nome e preço dos links adicionados e salva no banco.

- `Ver Tabela` → abre uma janela com histórico de preços (scroll incluso).

- `Ver Análise` → gera gráficos de evolução do preço por produto.

- `Exportar Dados` → use analysis/export_data.py para salvar em CSV.

