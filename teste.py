import pandas as pd
from openpyxl import load_workbook

excelVol = 'Pasta1.xlsx'

book = load_workbook(excelVol)

with pd.ExcelWriter (excelVol, engine='openpyxl') as writer:
    writer.book = book
    writer.sheets.update(dict((ws.title, ws) for ws in book.worksheets))

    try:
        writer.save()
    except:
        pass