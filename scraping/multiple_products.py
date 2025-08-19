import requests
from bs4 import BeautifulSoup
from datetime import datetime

from database.insert_price import salvar_preco


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9"
}

def coletar_preco(url):
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    titulo = soup.find(id = "productTitle")
    titulo = titulo.get_text().strip() if titulo else None

    preco = soup.find("span", class_ ="a-offscreen")
    preco = preco.get_text().strip() if preco else None

    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   
    salvar_preco(titulo, preco, data)

    return {"nome": titulo, "preco": preco}


def coletar_varios_produtos(links: list[str]):
    resultados = []
    for url in links:
        resultados.append(coletar_preco(url))
    return resultados
