import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

file_path = "D:/Projetos/TCC/Arquivos Base/Vendas/Vendas_Total.csv"

vendas = pd.read_csv(file_path, converters={'cst_cod': str})
vendas = vendas.drop(columns=['sls_tme'])
vendas['sls_day'] = pd.to_datetime(vendas['sls_day'], format='%Y%m%d')

vendas['mes_ano'] = vendas['sls_day'].dt.to_period('M')
vendas_valor = vendas.groupby('mes_ano')['sls_vle'].sum()
vendas_valor = vendas_valor.sort_index()

modelo_valor = ARIMA(vendas_valor, order=(7, 2, 0)) 
resultado_valor = modelo_valor.fit()
futuro_valor = resultado_valor.forecast(steps=15)

plt.figure(figsize=(24, 12))

plt.bar(vendas_valor.index.astype(str), vendas_valor, label='Vendas (Valor)', color='blue') 
plt.plot(futuro_valor.index.astype(str), futuro_valor, label='Previsão de Vendas (Valor)', color='red', linestyle='dashed')
plt.title("Vendas e Previsão de Vendas (Valor)")
plt.xlabel("Mês")
plt.ylabel("Valor de Venda")
plt.xticks(rotation=45, ha='right')
plt.legend()

plt.savefig('D:/Projetos/TCC/Arquivos Base/Vendas/ARIMA.png')