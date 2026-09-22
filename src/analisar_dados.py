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

# --- Query 1: EDA ---

# Lendo o arquivo que foi gerado na etapa de limpeza e utilizando o arquivo já tratado para fazer a análise dos dados.
df = pd.read_csv("dados/query_01_limpo.csv")


# --- Estatísticas dos salários ---

# Calculando a média salarial de todos os funcionários.
print("Média salarial:", df["SALARY"].mean())

# Calculando a mediana salarial.
print("Mediana salarial:", df["SALARY"].median())

# Identificando o menor salário presente no conjunto de dados.
print("Menor salário:", df["SALARY"].min())

# Identificando o maior salário presente no conjunto de dados.
print("Maior salário:", df["SALARY"].max())


# --- Quantidade de funcionários por departamento ---

# Contando quantos funcionários existem em cada departamento.
# O value_counts() contabiliza a quantidade de ocorrências de cada valor na coluna DEPARTMENT_NAME.
print("\nFuncionários por departamento:")
print(df["DEPARTMENT_NAME"].value_counts())


# --- Histograma dos salários ---

# Criando um histograma para visualizar como os salários estão distribuídos.
#
# bins=10 significa que os salários serão divididos em 10 intervalos.
# color define a cor das barras.
# edgecolor define a cor das bordas das barras.
plt.hist(
    df["SALARY"],
    bins=10,
    color="lightblue",
    edgecolor="black"
)

# Definindo o título do gráfico.
plt.title("Distribuição de Salários")

# Definindo o nome do eixo X.
plt.xlabel("Faixa Salarial")

# Definindo o nome do eixo Y.
# O eixo Y representa a quantidade de funcionários em cada faixa salarial.
plt.ylabel("Número de Funcionários")

# Com ajuda da IA, salvei o histograma como uma imagem PNG.
# Isso permite utilizar o gráfico posteriormente no trabalho sem precisar gerar o gráfico novamente.
plt.savefig("graficos/query1_salarios_histograma.png")

# Com a ajuda da IA, fecho o gráfico atual para liberar memória e evitar que ele seja reutilizado junto com o próximo gráfico.
plt.close()


# --- Boxplot dos salários por departamento ---

# Criando um boxplot para comparar a distribuição dos salários entre os diferentes departamentos.
#
df.boxplot(
    column="SALARY",
    by="DEPARTMENT_NAME",
    rot=45
)

# Definindo o título principal do gráfico.
plt.title("Salários por Departamento")

# O pandas cria automaticamente um segundo título relacionado ao agrupamento utilizado no boxplot.
# Com a ajuda da IA, removo esse título para deixar o gráfico mais limpo.

plt.suptitle("")

# Salvando o boxplot como uma imagem PNG.
plt.savefig("graficos/query1_salarios_boxplot.png")

# Fechando o gráfico depois de salvá-lo.
plt.close()


# QUERY 2 - FUNCIONÁRIOS POR REGIÃO

# --- Query 2: Limpeza ---

# Fazendo a leitura do arquivo CSV original da Query 2.
# Usando header=None para que nenhuma linha seja considerada automaticamente como cabeçalho.

df2_raw = pd.read_csv("dados/query_02.csv", header=None)


# Separando os dados usando a vírgula como delimitador.
# O expand=True transforma os valores separados em várias colunas.

df2 = df2_raw[0].str.split(",", expand=True)


# --- Verificação dos dados antes da limpeza ---

# Antes de continuar a limpeza, faço uma visualização das primeiras linhas do DataFrame para verificar como os dados foram separados.

print("\nPreview Query 2 antes da limpeza:")

print(df2.head())


# --- Definição dos nomes das colunas ---

# Depois de verificar a estrutura dos dados, atribuo nomes às colunas.
# O resultado da Query 2 possui 9 colunas, reunindo informações dos funcionários, departamentos e localização geográfica.

df2.columns = [
    "EMPLOYEE_ID",
    "FIRST_NAME",
    "LAST_NAME",
    "SALARY",
    "DEPARTMENT_NAME",
    "CITY",
    "STATE_PROVINCE",
    "COUNTRY_NAME",
    "REGION_NAME"
]


# --- Remoção das aspas ---

# Percorro todas as colunas do DataFrame.
# Em cada coluna, removo as aspas duplas que vieram junto com os valores do arquivo CSV.

for col in df2.columns:
    df2[col] = df2[col].str.strip('"')


# --- Remoção do cabeçalho original ---

# Removendo a primeira linha do DataFrame, que corresponde ao cabeçalho original exportado junto com os dados.

df2 = df2.drop(0)


# --- Salvamento do arquivo limpo ---

# Depois de realizar a limpeza, salvo os dados em um novo arquivo CSV.
# O parâmetro index=False impede que o índice do DataFrame seja salvo como uma coluna adicional.

df2.to_csv("dados/query_02_limpo.csv", index=False)

# Mostro uma mensagem no terminal para confirmar que o arquivo foi salvo corretamente.

print("\nArquivo limpo salvo em dados/query_02_limpo.csv")


# --- Query 2: EDA ---

# Abrindo o arquivo já limpo para iniciar a análise exploratória dos dados.

df2 = pd.read_csv("dados/query_02_limpo.csv")


# --- Análise das regiões ---

# Conto quantos funcionários existem em cada região.
# O value_counts() contabiliza a quantidade de registros para cada valor da coluna REGION_NAME.

print("\nFuncionários por região:")

print(df2["REGION_NAME"].value_counts())


# --- Gráfico de funcionários por região ---

plt.figure(figsize=(8, 5))

df2["REGION_NAME"].value_counts().plot(kind="bar")

plt.title("Funcionários por Região")
plt.xlabel("Região")
plt.ylabel("Total de Funcionários")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("graficos/query2_regioes.png", dpi=300)

plt.close()

#QUERY 3 - FUNCIONÁRIOS POR CARGO E FAIXA SALARIAL

# Esta é uma análise extra do projeto.
# O objetivo é identificar como os funcionários estão distribuídos entre os cargos e as diferentes faixas salariais.

# --- Query 3: Limpeza ---

# Fazendo a leitura do arquivo CSV original da Query 3.
# Usando header=None para que nenhuma linha seja considerada automaticamente como cabeçalho.

df3_raw = pd.read_csv("dados/query_03.csv", header=None)


# --- Verificação inicial dos dados ---

# O CSV exportado apresenta inicialmente os dados em uma única coluna. Por isso, verificamos as primeiras linhas antes de realizar a separação dos campos.

print("\nPreview Query 3 antes da limpeza:")

print(df3_raw.head())


# --- Separação das colunas ---

# Separando os dados utilizando a vírgula como delimitador.
# O parâmetro expand=True transforma os valores separados em diferentes colunas do DataFrame.

df3 = df3_raw[0].str.split(",", expand=True)


# --- Verificação da estrutura ---

print("\nNúmero de colunas:")

print(df3.shape[1])


# --- Definição dos nomes das colunas ---

# A Query 3 possui três informações: cargo, faixa salarial e quantidade de funcionários.

df3.columns = [
    "JOB_TITLE",
    "FAIXA_SALARIAL",
    "TOTAL_FUNCIONARIOS"
]


# --- Remoção das aspas ---

# Removendo as aspas duplas que foram importadas junto com os valores do arquivo CSV.

for col in df3.columns:
    df3[col] = df3[col].str.strip('"')


# --- Remoção do cabeçalho original ---

# A primeira linha contém os nomes das colunas do CSV original.
# Como os nomes já foram definidos anteriormente, essa linha é removida do DataFrame.

df3 = df3.drop(0)


# --- Conversão dos dados numéricos ---

# Convertendo a quantidade de funcionários para um tipo numérico.
# Isso permite realizar cálculos e agrupamentos corretamente.

df3["TOTAL_FUNCIONARIOS"] = pd.to_numeric(
    df3["TOTAL_FUNCIONARIOS"],
    errors="coerce"
)


# --- Verificação de valores ausentes ---

# Verificando se existem valores ausentes após a limpeza.

print("\nValores ausentes:")

print(df3.isnull().sum())


# --- Remoção de registros incompletos ---

# Removendo registros que não possuem informações essenciais para a análise.

df3 = df3.dropna(
    subset=[
        "JOB_TITLE",
        "FAIXA_SALARIAL",
        "TOTAL_FUNCIONARIOS"
    ]
)


# --- Salvamento do arquivo limpo ---

# Salvando os dados tratados em um novo arquivo CSV.
# O parâmetro index=False impede que o índice do DataFrame seja salvo como uma coluna adicional.

df3.to_csv(
    "dados/query_03_limpo.csv",
    index=False
)

print("\nArquivo limpo salvo em:")

print("dados/query_03_limpo.csv")


#  --- Query 3: EDA ---
# Abrindo novamente o arquivo limpo para iniciar a análise exploratória dos dados.

df3 = pd.read_csv("dados/query_03_limpo.csv")


# --- Visualização dos dados ---

print("\nDados da Query 3:")

print(df3)


# --- Informações do DataFrame ---

# O info() apresenta informações sobre quantidade de registros, colunas e tipos de dados.

print("\nInformações do DataFrame:")

print(df3.info())


# --- Total de funcionários por cargo ---

# Somando a quantidade de funcionários de cada cargo.
# Como um mesmo cargo pode aparecer em mais de uma faixa salarial, utilizei sum() para obter o total do cargo.

print("\nTotal de funcionários por cargo:")

print(
    df3.groupby("JOB_TITLE")["TOTAL_FUNCIONARIOS"]
    .sum()
    .sort_values(ascending=False)
)


# --- Total de funcionários por faixa salarial ---

# Contabilizando o total de funcionários existente em cada faixa salarial.

print("\nTotal de funcionários por faixa salarial:")

print(
    df3.groupby("FAIXA_SALARIAL")["TOTAL_FUNCIONARIOS"]
    .sum()
    .sort_values(ascending=False)
)


# --- Total geral de funcionários ---

# Somando todos os funcionários presentes no resultado da Query 3.

total_funcionarios = df3["TOTAL_FUNCIONARIOS"].sum()

print("\nTotal geral de funcionários:")

print(total_funcionarios)


# --- Gráfico - Funcionários por Cargo e Faixa Salarial ---

# Criando uma tabela que organiza os cargos nas linhas e as faixas salariais nas colunas.

grafico = df3.pivot_table(
    index="JOB_TITLE",
    columns="FAIXA_SALARIAL",
    values="TOTAL_FUNCIONARIOS",
    aggfunc="sum",
    fill_value=0
)


# Definindo uma ordem lógica para as faixas salariais.

ordem_faixas = [
    "Até 3k",
    "3k - 6k",
    "6k - 10k",
    "Acima de 10k"
]


# Mantendo somente as faixas que realmente existem no DataFrame e organizando-as na ordem definida acima.

faixas_existentes = [
    faixa
    for faixa in ordem_faixas
    if faixa in grafico.columns
]

grafico = grafico[faixas_existentes]


# Criando o gráfico.

grafico.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Funcionários por Cargo e Faixa Salarial")
plt.xlabel("Cargo")
plt.ylabel("Total de Funcionários")

plt.xticks(
    rotation=45,
    ha="right"
)

plt.legend(title="Faixa Salarial")

plt.tight_layout()


# Salvando o gráfico.

plt.savefig(
    "graficos/query3_funcionarios_cargo_faixa.png",
    dpi=300
)

plt.close()

print(
    "\nGráfico salvo em "
    "graficos/query3_funcionarios_cargo_faixa.png"
)

