import pandas as pd
caminho_arquivo = "MODULO1/SEMANA05/BO_2007_1.csv"
df = pd.read_csv(caminho_arquivo, encoding="ISO-8859-1", on_bad_lines="skip")
#Exibe as primeiras linhas válidas encontradas
print(df.head(5))

 # Descobre o total de linhas e colunas reais lidas
linhas, colunas = df.shape
print(f"Total de linhas válidas lidas: {linhas}")
print(f"Total de colunas válidas lidas: {colunas}")

print(list(df.columns))

# O método .unique() vai listar todas as idades que existem no arquivo sem repetir
idades_unicas = df['IDADE_PESSOA'].unique()
print(idades_unicas)