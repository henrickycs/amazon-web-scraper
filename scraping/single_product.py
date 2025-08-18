import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.amazon.com.br/PlayStation-DualSense-Controle-sem-fio/dp/B0CQKKHT5J/?_encoding=UTF8&pd_rd_w=bguwr&content-id=amzn1.sym.8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_p=8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_r=QC2C7FCV137BG5C8P4X0&pd_rd_wg=VlwNb&pd_rd_r=5760beb4-856f-4eee-b86e-3a668ea9ca00&ref_=pd_hp_d_btf_crs_zg_bs_7791985011&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

titulo = soup.find(id = "productTitle")
titulo = titulo.get_text().strip() if titulo else "Título não encontrado"

preco = soup.find("span", class_ ="a-offscreen")
preco = preco.get_text().strip() if preco else "Preço não encontrado"

print(f"Produto: {titulo}")
print(f"Preço: {preco}")
print(f"Data: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")