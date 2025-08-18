import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

from database.insert_price import salvar_preco

urls = {
    "DualSense Branco":"https://www.amazon.com.br/PlayStation-DualSense-Controle-sem-fio/dp/B0CQKLS4RP/?_encoding=UTF8&pd_rd_w=7f3us&content-id=amzn1.sym.8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_p=8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_r=CJQN0Q9D6ZWXSD51E082&pd_rd_wg=oCv2M&pd_rd_r=01162b1c-a725-45c5-ad33-10c7d3e50f75&ref_=pd_hp_d_btf_crs_zg_bs_7791985011&th=1",
    "DualSense Midnight Black":"https://www.amazon.com.br/PlayStation-DualSense-Controle-sem-fio/dp/B0CQKKHT5J/?_encoding=UTF8&pd_rd_w=bguwr&content-id=amzn1.sym.8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_p=8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_r=QC2C7FCV137BG5C8P4X0&pd_rd_wg=VlwNb&pd_rd_r=5760beb4-856f-4eee-b86e-3a668ea9ca00&ref_=pd_hp_d_btf_crs_zg_bs_7791985011&th=1",
    "DualSense Volcanic Red":"https://www.amazon.com.br/PlayStation-DualSense-Controle-sem-fio/dp/B0CJT7H85N/?_encoding=UTF8&pd_rd_w=7f3us&content-id=amzn1.sym.8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_p=8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_r=CJQN0Q9D6ZWXSD51E082&pd_rd_wg=oCv2M&pd_rd_r=01162b1c-a725-45c5-ad33-10c7d3e50f75&ref_=pd_hp_d_btf_crs_zg_bs_7791985011&th=1"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9"
}

def coletar_preco(nome_produto, url):
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    titulo = soup.find(id = "productTitle")
    titulo = titulo.get_text().strip() if titulo else nome_produto

    preco = soup.find("span", class_ ="a-offscreen")
    preco = preco.get_text().strip() if preco else None

    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return titulo, preco, data


for nome, url in urls.items():
    titulo, preco, data =  coletar_preco(nome, url)
    salvar_preco(titulo, preco, data)
    print(f"Salvo: {titulo} | {preco} | {data}")
    time.sleep(2)
