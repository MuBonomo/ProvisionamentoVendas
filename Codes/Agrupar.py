import os
import pandas as pd

diretorio = "D:/Projetos/TCC/Arquivos Base/Vendas/"

dataframes = []

for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith(".csv"):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        df = pd.read_csv(caminho_arquivo, converters = {"HR":str, "REMESSA":str, "CLIENTE":str, "MATERIAL":str})
        dataframes.append(df)

vendas_total = pd.concat(dataframes, ignore_index=True)

caminho_saida = os.path.join(diretorio, "Vendas_Total.csv")
vendas_total.to_csv(caminho_saida, index=False)

print("Arquivo 'Vendas_Total.csv' criado com sucesso!")