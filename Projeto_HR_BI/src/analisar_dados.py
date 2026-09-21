import pandas as pd
from io import StringIO

arquivo = "dados/query_01.csv"

# Corrige a formatação do CSV
with open(arquivo, "r", encoding="utf-8") as f:
    linhas = f.readlines()

linhas_corrigidas = []

for linha in linhas:
    linha = linha.strip()

    # Remove as aspas externas
    if linha.startswith('"') and linha.endswith('"'):
        linha = linha[1:-1]

    # Corrige aspas duplicadas
    linha = linha.replace('""', '"')

    linhas_corrigidas.append(linha)

# Cria o DataFrame
df = pd.read_csv(StringIO("\n".join(linhas_corrigidas)))

print("Quantidade de linhas:", len(df))
print("Quantidade de colunas:", len(df.columns))

print("\nColunas:")
print(df.columns.tolist())

print("\nPrimeiras linhas:")
print(df.head())