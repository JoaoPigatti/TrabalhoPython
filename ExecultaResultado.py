from datetime import date
from art import tprint
tprint('Resultado diario',font='standard')
tprint(str(date.strftime(date.today(),"%d/%m/%Y")),font='standard')
print('______________________________________________________________________________________________________\n')



#Imports

import time
import pandas as pd
import excel2img
import sys
from openpyxl import load_workbook
from Resultados2 import update,boup

data_i, data_f = update()
try:
    boup(data_i,data_f)
except Exception as E:
    print(E)
    input ()
    sys.exit()

print('\n Item gerado: ')
file = 'BackOffice2.csv'
print (file)

print ('\n Relatorio: ')
excelVol = 'Resultados05.xlsx'

lerMetas = pd.read_csv("Metas Vendedores.csv")

lerArq = pd.read_csv(file)
book = load_workbook (excelVol)
with pd.ExcelWriter (excelVol, engine='openpyxl') as writer:
    writer.book = book
    writer.sheets.update(dict((ws.title, ws) for ws in book.worksheets))
    
    lerArq.to_excel(writer, sheet_name = "BD_Total" , index=False)
    lerMetas.to_excel(writer, sheet_name= "Metas", index=False )
   
    try: 
        writer.save(excelVol)
    except:
        pass    

print ('\n Imagen Geradas: ')
gerarPng = ["TotalFinal"]
for s in gerarPng:
    nomeimg = f"{str(date.today().month)}-{str(date.today().year)} {s}.png"
    excel2img.export_img(excelVol,nomeimg,s)
    print(nomeimg)
    time.sleep(1)
    
print("Acabou !")
time.sleep(2)
    
