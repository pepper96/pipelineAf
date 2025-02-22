import yfinance as yf
import pandas as pd
import datetime
from datetime import date,datetime
import os
import pandas as pd

from airflow.decorators import dag, task
from airflow.utils.task_group import TaskGroup

tickers = ["IRDM11.SA","LSAG11.SA","RECR11.SA","TGAR11.SA",
            "TRXF11.SA","VRTA11.SA","HCTR11.SA","VGIP11.SA","DEVA11.SA","MXRF11.SA"]



@dag(
    dag_id = "fii_info",
    schedule = "@daily",
    start_date = datetime(year=2025,month=2,day=22),
    catchup=False
)

def main():
    
    transform = TaskGroup("transform")
    store = TaskGroup("store")

    @task(task_id = "extract",task_group=transform)
    def extract_fii():

        dados_mercado = yf.download(tickers, period="5d",progress=False)
        return dados_mercado
    
    @task(task_id = "transform",task_group=transform)
    def process_data(dados_mercado):
        dados_close = dados_mercado["Close"].reset_index()
        dados_close.columns.name=None
        dados_close['Date']=dados_close['Date'].dt.strftime('%d/%m/%Y')
        dados_close=pd.melt(dados_close,id_vars=['Date'],value_vars=tickers,var_name="FII",value_name="Close")
        return dados_close

    @task(task_id = "store" , task_group = store)
    def store_fii(dados_close):
        #caminho = f"/mnt/c/Users/pimen/OneDrive/Área de Trabalho/Teste_Fii/cotacoes_{datetime.today().strftime('%d_%m_%Y')}.csv"
        caminho = f"/mnt/c/Users/pimen/OneDrive/projetoFii/cotacoesFii/cotacoes_{datetime.today().strftime('%d_%m_%Y')}.csv"
        dados_close.to_csv(caminho,sep=';',decimal=',',index=False,encoding='latin-1')


    @task(task_id = "store_parquet",task_group = store)
    def store_parquet():
        diretorio = "/mnt/c/Users/pimen/OneDrive/projetoFii/cotacoesFii/"
        list_cot = []
        for doc in os.listdir(diretorio):
            if doc.endswith('.csv'):
                cot = pd.read_csv(diretorio+doc, sep=';', encoding='latin-1',dtype=str)
                list_cot.append(cot)
        parquet_base = pd.concat(list_cot,axis=0,ignore_index=True)
        parquet_base.to_parquet("/mnt/c/Users/pimen/OneDrive/projetoFii/cotacoes_fii.parquet",index=False, engine='pyarrow')



    dados_mercado = extract_fii()  # A primeira task, para extrair os dados
    dados_transformados = process_data(dados_mercado)  # A segunda task, para processar os dados
    store_fii(dados_transformados) >> store_parquet() #Salvar Dados

main()




        