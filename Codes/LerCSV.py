import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt

# Definir as variáveis para os arquivos CSVs
vendas = "D:/Projetos/TCC/Arquivos Base/Vendas/Vendas_Total.csv"
clientes = "D:/Projetos/TCC/Arquivos Base/Costumers.csv"
estoque = "D:/Projetos/TCC/Arquivos Base/Estoque.csv"
itens = "D:/Projetos/TCC/Arquivos Base/Itens.csv"
bins = "D:/Projetos/TCC/Arquivos Base/Posições.csv"

#Tratativas dos arquivos CSV
dados_vendas = pd.read_csv(vendas, converters={"sls_dlv":str, "cod_mat":str, "cst_cod":str})
dados_vendas["sls_day"] = pd.to_datetime(dados_vendas["sls_day"], format="%Y%m%d")
dados_vendas = dados_vendas.drop(columns=['sls_tme'])

dados_clientes = pd.read_csv(clientes, converters={"cst_cod":str})

dados_estoque = pd.read_csv(estoque)

dados_itens = pd.read_csv(itens, converters={"cod_mat":str})

dados_bins = pd.read_csv(bins)

# Configurar índice de data
dados_vendas.set_index('sls_day', inplace=True)

# Visualizar os dados
plt.plot(dados_vendas['sls_qty'])
plt.title('Série Temporal de Demanda')
plt.show()