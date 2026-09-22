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

# --- Query 2: Limpeza ---

# Fazendo a leitura do arquivo CSV original da Query 2.
# Usando o header=None faz para que nenhuma linha seja considerada automaticamente como cabeçalho.
df2_raw = pd.read_csv("dados/query_02.csv", header=None)

# Separando os dados usando a vírgula como delimitador.
# Transformando os valores separados, em várias colunas com expand=True.
df2 = df2_raw[0].str.split(",", expand=True)


# --- Verificação dos dados antes da limpeza ---

# Antes de continuar a limpeza, faço uma visualização das primeiras linhas do DataFrame para verificar como os dados foram separados.
print("\nPreview Query 2 antes da limpeza:")
print(df2.head())


# --- Definição dos nomes das colunas ---

# Depois de verificar a estrutura dos dados, atribuo nomes às colunas.
# Neste arquivo existem 9 colunas relacionadas às localizações.
df2.columns = [
    "LOCATION_ID",
    "STREET_ADDRESS",
    "POSTAL_CODE",
    "CITY",
    "STATE_PROVINCE",
    "COUNTRY_ID",
    "REGION_ID",
    "REGION_NAME",
    "LOCATION_NAME"
]


# --- Remoção das aspas ---

# Percorro todas as colunas do DataFrame. Em cada coluna, removo as aspas duplas que vieram junto com os valores do arquivo CSV.
for col in df2.columns:
    df2[col] = df2[col].str.strip('"')


# --- Remoção do cabeçalho original ---

# Removendo a primeira linha do DataFrame.
df2 = df2.drop(0)


# --- Salvamento do arquivo limpo ---

# Depois de realizar a limpeza, salvo os dados em um novo arquivo CSV.
# Utilizei o parâmetro index=False para impeder que o índice do DataFrame seja salvo como uma coluna adicional no arquivo.
df2.to_csv("dados/query_02_limpo.csv", index=False)

# Mostro uma mensagem no terminal para confirmar que o arquivo foi salvo corretamente.
print("\nArquivo limpo salvo em dados/query_02_limpo.csv")


# --- Query 2: EDA ---

# Abrindo o arquivo já limpo para iniciar a análise exploratória dos dados.
df2 = pd.read_csv("dados/query_02_limpo.csv")


# --- Análise das localizações ---

# Conto quantos registros existem para cada localização.
# O value_counts() contabiliza quantas vezes cada localização aparece na coluna LOCATION_NAME.
print("\nFuncionários por localização:")
print(df2["LOCATION_NAME"].value_counts())


# --- Gráfico de funcionários por localização ---

# Criando um gráfico de barras com a quantidade de registros existente em cada localização.
#
# kind="bar" define que o gráfico será de barras.
# color define a cor das barras.
# edgecolor define a cor das bordas das barras.
df2["LOCATION_NAME"].value_counts().plot(
    kind="bar",
    color="lightgreen",
    edgecolor="black"
)

# Definindo o título do gráfico.
plt.title("Funcionários por Localização")

# Definindo o nome do eixo X.
plt.xlabel("Localização")

# Definindo o nome do eixo Y.
plt.ylabel("Número de Funcionários")

# Com ajuda da IA, girei os nomes das localizações em 45 graus, para facilitar a leitura.
plt.xticks(rotation=45)

# Com ajuda da IA, ajusto automaticamente os espaços do gráfico para evitar que os textos fiquem cortados.
plt.tight_layout()

# Salvando o gráfico em formato PNG na pasta de gráficos.
plt.savefig("graficos/query2_localizacoes.png")

# Fechando o gráfico depois de salvá-lo.
plt.close()