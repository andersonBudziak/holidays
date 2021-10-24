from _typeshed import Self
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta

class Holidays():

    def holidays(url=None, path=None):

        url = 'http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls'

        nao_uteis = pd.read_excel(url, usecols="A", parse_dates=True)
        
        nao_uteis.dropna(inplace=True)
        
        for index, row in nao_uteis.iterrows():
            if type(row["Data"]) == str:
                nao_uteis.drop(index,axis=0,inplace=True)
        
        lista_datas = []
        for index, row in nao_uteis.iterrows():
            lista_datas.append(row['Data'])

        return lista_datas
    
    #Passar um datetime ou uma string no formato 'yyyy-mm-dd'
    def returnDayUtil(self, dia, datas:list):

        if type(dia) == str:
            dia = dt.strptime(dia, '%Y-%m-%d')

        while True:
            if (dia in datas) or (dia.weekday() == 6) or (dia.weekday() == 5):
                dia =  dia + timedelta(1)
            else:
                break

        return dia
    
    def  isNotDU(self, dia, datas):       
    
        if type(dia) == str:
            dia = dt.strptime(dia, '%Y-%m-%d')
        
        return (dia in datas) or (dia.weekday() == 6) or (dia.weekday() == 5)