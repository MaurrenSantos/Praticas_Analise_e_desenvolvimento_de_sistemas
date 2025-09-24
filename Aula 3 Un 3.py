import pandas as pd
df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.20542/dados?formato=json")

print(df_selic.info())
print(df_selic)

#verificar duplicidade de linhas (passo muito importante), utilizando a função drop_duplicates()
df_selic.drop_duplicates(keep='last', inplace=True)
#mantem o último registro (keep='last')
#através do parâmetro inplace=True, faz com que a transformação seja salva do DataFrame
#no nosso caso não existe linhas duplicadas.

#adicionando colunas
from datetime import date
from datetime import datetime as dt

data_extração = date.today()

df_selic['data_extração'] = data_extração
df_selic['responsavel'] = "Autor"
print(df_selic.info())
df_selic.head()

##########################################

df_selic.loc[0] #Pego a informação do índice

teste = df_selic['valor'] < 0.01
print(type(teste))