import pandas as pd
import matplotlib.pyplot as plt

# --- Query 1: Limpeza ---

# Fazendo a leitura do arquivo CSV original.
# O header=None é usado, pois a primeira linha do arquivo não deve ser tratada como nome das colunas.
df_raw = pd.read_csv("dados/query_01.csv", header=None)

# O arquivo foi lido inicialmente como uma única coluna.
# Aqui separo os valores dessa coluna usando a vírgula como delimitador.
# Com ajuda da IA, verifiquei que o expand=True transforma os valores separados em novas colunas.
df = df_raw[0].str.split(",", expand=True)

# Depois de separar os dados, atribuí os nomes para cada uma das colunas, conforme as informações presentes no arquivo:
# ID do funcionário, nome, sobrenome, salário, departamento e cargo.
df.columns = [
    "EMPLOYEE_ID",
    "FIRST_NAME",
    "LAST_NAME",
    "SALARY",
    "DEPARTMENT_NAME",
    "JOB_TITLE"
]

# Percorro todas as colunas do DataFrame.
# O objetivo é remover as aspas duplas (") que vieram junto com os valores do arquivo CSV.
for col in df.columns:
    df[col] = df[col].str.strip('"')

# Removendo a primeira linha do DataFrame.
# Ela corresponde ao cabeçalho original do arquivo, que foi mantido como dado porque usei header=None na leitura.
df = df.drop(0)

# Convertendo a coluna SALARY de texto (string) para número.
df["SALARY"] = pd.to_numeric(df["SALARY"])

# Salvando o DataFrame já limpo em um novo arquivo CSV.
# Utilizei o index=False para evitar que o índice do DataFrame seja salvo como uma coluna adicional no arquivo.
df.to_csv("dados/query_01_limpo.csv", index=False)

# Exibindo uma mensagem no terminal informando que o arquivo foi salvo.
print("\nArquivo limpo salvo em dados/query_01_limpo.csv")