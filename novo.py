import requests
import pandas as pd

secao = requests.Session()
secao.auth = ("usuario", "senha")

resposta = secao.get(url="https")
print(resposta.json())

df1 = pd.DataFrame(resposta.json())

df1.to_csv("Metas Vendedores.csv", index=False)

