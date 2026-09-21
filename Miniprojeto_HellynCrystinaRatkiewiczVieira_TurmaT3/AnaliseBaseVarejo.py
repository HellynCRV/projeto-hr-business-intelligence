# ==========================================
# SPRINT 1: IMPORTAÇÃO E EXPLORAÇÃO INICIAL
# ==========================================

import pandas as pd
import numpy as np

# Carregando a base de dados com o separador correto (ponto e vírgula)
df = pd.read_csv("Base Varejo.csv", sep=";")

# Visualizando as primeiras linhas para entender a estrutura dos dados
print("Primeiras linhas do dataset:")
print(df.head())

# Verificando informações gerais: quantidade de registros, colunas e tipos de dados
print("\nInformações gerais sobre a base de dados:")
df.info()
