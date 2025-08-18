import sqlite3
import pandas as pd

conn = sqlite3.connect("precos.db")
df = pd.read_sql("SELECT * FROM precos", conn)
conn.close()

df["preco_num"] = (
    df["preco"]
    .str.replace("R$", "", regex=False)
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

df["data_coleta"] = pd.to_datetime(df["data_coleta"])

df.to_csv("relatorio_precos.csv", index = False, encoding="UTF-8")
