import pandas as pd
import requests
import json
from datetime import date

url = "https://nacional-prd-protheus.totvscloud.com.br:12529/rest/INT_SHELL_BO_NOVOANT"

#Função para tratamento de data *zfill usado para completar com zero
def update ():
    Data = date.today()
    DataIni = "01"
    DataDia = str(Data.day).zfill(2)
    DataMes = str(Data.month).zfill(2)
    DataAno = str(Data.year)
    return DataIni+ "/" + DataMes+ '/' + DataAno , DataDia+ '/' + DataMes + '/' + DataAno #usados para retornar as datas formatadas 
# "Boup" gera reatorio de vendas

def boup (inicio, fim):   
    json1 = {
    "data_inicial":inicio,
    "data_final":fim,
    "tipo_cliente":"B2B,B2C,VAREJO,FWS,FWS NN,B2BJD",
    "cnpjs":"",
    "armazem":"",
    "tipo_prod":"",
    "distribuidor":"NACIONAL / ATACADO"
    }
    json2= {
        "data_inicial":inicio,
        "data_final":fim,
        "tipo_cliente":"B2B,B2C,VAREJO,FWS,FWS NN,B2BJD",
        "cnpjs":"",
        "armazem":"",
        "tipo_prod":"",
        "distribuidor":"NACIONAL / ES"
    }    
    
    try:
        req = requests.post (url=url, json=json1)
        json12 = req.json()
    except:
        json12 = {}
        
    try:
        req2 = requests.post (url=url, json=json2)
        json25 = req2.json()
    except:
        json25 = {}
        
    df12 = pd.DataFrame(json12)
    df25 = pd.DataFrame(json25)
    frames = [df12 , df25]
    bonovo = pd.concat(frames)
    bonovo.to_csv('BackOffice2.csv',index=False, encoding="UTF-8")
if __name__ == "__main__":
    data_i, data_f = update()
    boup(data_i, data_f)        
 
    

    
