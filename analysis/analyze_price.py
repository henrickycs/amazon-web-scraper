import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("precos.db")

df = pd.read_sql("SELECT * FROM precos", conn)

conn.close()

#converter para float
df["preco_num"] = (
    df["preco"]
    .str.replace("R$", "", regex=False)
    .str.replace(".", "", regex=False)  # remove separador de milhar
    .str.replace(",", ".", regex=False) # troca vírgula por ponto
    .astype(float)
)

#converter para datetime
df["data_coleta"] = pd.to_datetime(df["data_coleta"])

print(df[["produto", "preco", "preco_num", "data_coleta"]].head())


#grafico por produto
for produto, grupo in df.groupby("produto"):
    plt.figure(figsize=(8,4))
    plt.plot(grupo["data_coleta"], grupo["preco_num"], marker="o")
    plt.title(f"Evolução de preço - {produto}")
    plt.xlabel("Data")
    plt.ylabel("Preço (R$)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()