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