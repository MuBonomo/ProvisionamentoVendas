import sqlite3
import os
import pandas as pd

nome_banco_dados = "D:/Projetos/TCC/DB/DB_TCC.db"

nome_tabela = "sales"

caminho_csv = "D:/Projetos/TCC/Arquivos Base/Vendas/Vendas_Total.csv"

dados = pd.read_csv(caminho_csv, converters={"sls_dlv": str, "cod_mat": str, "sls_tme": str, "cst_cod": str})
dados["sls_day"] = pd.to_datetime(dados["sls_day"], format="%Y%m%d")

conexao = sqlite3.connect(nome_banco_dados)

dados.to_sql(nome_tabela, conexao, if_exists="replace", index=False)

conexao.close()

print("Dados inseridos com sucesso no banco de dados SQLite.")
