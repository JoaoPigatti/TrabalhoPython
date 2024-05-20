import requests
import pandas as pd

secao = requests.Session()
secao.auth = ("alex.machado", "aszxcfd123")

resposta = secao.get(url="https://nacional-prd-protheus.totvscloud.com.br:12563/rest/wsgestor/comissao?PeriodoInicial=20240501&PeriodoFinal=20240531")
print(resposta.json())

df1 = pd.DataFrame(resposta.json())

df1.to_csv("Metas Vendedores.csv", index=False)

