# Diário de Desenvolvimento — Projeto HR BI

Este documento registra o processo de desenvolvimento do projeto, incluindo decisões técnicas, problemas encontrados, soluções adotadas e aprendizados obtidos durante a construção da solução de Business Intelligence aplicada à área de Recursos Humanos.

---

## 18/09/2026 — Desenvolvimento da Query 1 (Salários por Departamento e Cargo)

### Objetivo

Construir a primeira consulta SQL solicitada no projeto, analisando a distribuição de salários por departamento e cargo.

### Atividades realizadas

* Acesso ao banco FreeSQL (schema HR).
* Criação da consulta `query_1.sql` utilizando `LEFT JOIN` entre as tabelas `EMPLOYEES`, `DEPARTMENTS` e `JOBS`.
* Aplicação de filtro simples com `WHERE SALARY > 0` para garantir consistência dos dados.
* Execução da query e validação dos resultados.
* Exportação do resultado para o arquivo `dados/query_01.csv`.

### Estrutura da Query

```sql
SELECT 
    e.employee_id,
    e.first_name,
    e.last_name,
    e.salary,
    d.department_name,
    j.job_title
FROM hr.employees e
LEFT JOIN hr.departments d ON e.department_id = d.department_id
LEFT JOIN hr.jobs j ON e.job_id = j.job_id
WHERE e.salary > 0;
```

### Resultado inicial

Durante os testes iniciais, o arquivo `query_01.csv` apresentou 58 registros e 6 colunas.

Essa etapa foi importante para validar a estrutura da consulta e iniciar os testes de importação e tratamento dos dados.

Posteriormente, a extração foi revisada para representar a base completa utilizada na análise final.

### Aprendizados

* A importância de validar a query com filtros simples para evitar registros inconsistentes.
* O uso de `LEFT JOIN` permite manter os funcionários na consulta mesmo quando algum relacionamento não possui correspondência.
* A validação dos dados extraídos é fundamental antes de iniciar a análise exploratória.

### Observação adicional

Durante os testes iniciais, também foi utilizada a condição:

```sql
WHERE SALARY > 5000
ORDER BY SALARY DESC
```

Essa variação foi utilizada para explorar os salários mais altos, mas não corresponde ao escopo oficial da Query 1.

A versão final utiliza `WHERE SALARY > 0`, permitindo representar a distribuição completa dos salários utilizada na análise.

---

## 21/09/2026 — Configuração inicial do projeto

### Objetivo

Preparar o ambiente de desenvolvimento para iniciar a análise dos dados de Recursos Humanos utilizando Python e Pandas.

### Atividades realizadas

* Estruturação inicial do projeto `Projeto_HR_BI`.
* Criação do ambiente virtual `.venv`.
* Ativação do ambiente virtual.
* Instalação da biblioteca Pandas.
* Criação do script `src/analisar_dados.py`.
* Identificação dos arquivos de dados na pasta `dados/`.

### Ambiente utilizado

* Python
* Pandas
* Visual Studio Code
* PowerShell
* Ambiente virtual Python (`.venv`)

---

## 21/09/2026 — Primeiro teste de leitura dos dados

### Objetivo

Realizar a leitura do arquivo CSV utilizando o Pandas e verificar sua estrutura.

### Código inicial

```python
df = pd.read_csv(arquivo)
```

### Resultado inicial

O arquivo foi carregado, porém os dados não foram interpretados corretamente.

Durante o primeiro teste, foram identificados problemas na interpretação das colunas e dos registros.

A lista de colunas retornada pelo Pandas apresentava todo o cabeçalho como uma única coluna:

```text
['EMPLOYEE_ID,"FIRST_NAME","LAST_NAME","SALARY","DEPARTMENT_NAME","JOB_TITLE"']
```

### Problema identificado

Os dados deveriam possuir seis campos:

* `EMPLOYEE_ID`
* `FIRST_NAME`
* `LAST_NAME`
* `SALARY`
* `DEPARTMENT_NAME`
* `JOB_TITLE`

Porém, o Pandas estava interpretando cada linha de forma incorreta.

---

## 21/09/2026 — Investigação da estrutura do CSV

### Objetivo

Identificar a causa do problema de leitura apresentado pelo Pandas.

### Procedimento realizado

Com a ajuda da IA, foi utilizado o comando:

```powershell
Get-Content dados\query_01.csv -TotalCount 2
```

### Resultado

Foi identificada uma estrutura de aspas diferente do formato CSV convencional:

```text
"EMPLOYEE_ID,""FIRST_NAME"",""LAST_NAME"",""SALARY"",""DEPARTMENT_NAME"",""JOB_TITLE"""
```

Também foi identificado que os campos estavam separados por vírgulas.

### Conclusão

O problema estava relacionado principalmente à formatação do arquivo de origem e à maneira como as aspas estavam estruturadas.

Essa investigação mostrou a importância de verificar o arquivo original antes de modificar o código de leitura.

---

## 21/09/2026 — Tratamento da leitura do CSV

### Objetivo

Corrigir a interpretação dos dados antes de iniciar a análise exploratória.

### Tentativa inicial

```python
pd.read_csv(arquivo, sep=",")
```

Apenas informar o separador não foi suficiente para corrigir completamente a estrutura das aspas do arquivo.

### Solução implementada

Com a ajuda da IA, foi realizado um tratamento prévio do conteúdo do arquivo antes da leitura com Pandas:

```python
with open(arquivo, "r", encoding="utf-8") as f:
    linhas = f.readlines()

linhas_corrigidas = []

for linha in linhas:
    linha = linha.strip()

    if linha.startswith('"') and linha.endswith('"'):
        linha = linha[1:-1]

    linha = linha.replace('""', '"')
    linhas_corrigidas.append(linha)

df = pd.read_csv(StringIO("\n".join(linhas_corrigidas)))
```

---

## 21/09/2026 — Validação da estrutura dos dados

Após o tratamento, o DataFrame passou a apresentar a estrutura esperada.

### Resultado

* Quantidade de linhas no primeiro arquivo analisado: 58
* Quantidade de colunas: 6

Colunas identificadas:

* `EMPLOYEE_ID`
* `FIRST_NAME`
* `LAST_NAME`
* `SALARY`
* `DEPARTMENT_NAME`
* `JOB_TITLE`

Foi utilizada a validação:

```python
len(df.columns)
```

### Aprendizados desta etapa

* Importância de verificar a estrutura real dos dados antes de iniciar uma análise.
* Problemas de importação podem estar relacionados ao arquivo de origem e não necessariamente ao Pandas.
* A inspeção direta do arquivo ajudou a identificar a causa do problema.
* É importante validar o DataFrame após a importação, verificando:

  * quantidade de registros;
  * quantidade de colunas;
  * nomes das colunas;
  * primeiras linhas dos dados.

Essa validação evita iniciar análises sobre uma estrutura incorreta.

---

## 21/09/2026 — Desenvolvimento da Query 2 (Funcionários por Região e Localização)

### Objetivo

Analisar a distribuição de funcionários por região, incluindo informações de localização como cidade, estado, país e região.

### Atividades realizadas

* Acesso ao banco FreeSQL (schema HR).
* Criação da consulta `query_2.sql`.
* Utilização de múltiplos `LEFT JOIN` entre `EMPLOYEES`, `DEPARTMENTS`, `LOCATIONS`, `COUNTRIES` e `REGIONS`.
* Aplicação de filtro para garantir consistência dos dados.
* Execução da query e validação dos resultados.
* Exportação do resultado para `dados/query_02.csv`.

### Estrutura da Query

```sql
SELECT 
    e.employee_id,
    e.first_name,
    e.last_name,
    e.salary,
    d.department_name,
    l.city,
    l.state_province,
    c.country_name,
    r.region_name
FROM hr.employees e
LEFT JOIN hr.departments d ON e.department_id = d.department_id
LEFT JOIN hr.locations l ON d.location_id = l.location_id
LEFT JOIN hr.countries c ON l.country_id = c.country_id
LEFT JOIN hr.regions r ON c.region_id = r.region_id
WHERE r.region_name IS NOT NULL;
```

### Resultado

O arquivo `query_02.csv` foi gerado contendo informações de funcionários, departamentos e localização completa.

Os dados ficaram preparados para a etapa de análise exploratória em Python.

### Aprendizados

* A utilização de múltiplos relacionamentos permite enriquecer uma análise com informações geográficas.
* O uso de `LEFT JOIN` possibilita preservar os registros da tabela principal.
* O filtro `WHERE r.region_name IS NOT NULL` ajudou a garantir consistência dos dados utilizados na análise.

---

## 21/09/2026 — Desenvolvimento da Query 3 (Funcionários por Cargo e Faixa Salarial)

### Objetivo

Criar uma análise complementar para identificar a distribuição dos funcionários de acordo com o cargo e a faixa salarial.

### Atividades realizadas

* Criação da consulta `query_3.sql`.
* Utilização das tabelas `EMPLOYEES` e `JOBS`.
* Criação das faixas salariais utilizando `CASE WHEN`.
* Contagem dos funcionários por cargo e faixa salarial.
* Organização dos resultados por cargo e faixa salarial.
* Exportação dos resultados para CSV.

### Aprendizados

* O uso de `CASE WHEN` permitiu transformar valores salariais em categorias, facilitando a análise.
* A utilização da tabela `JOBS` permitiu relacionar os cargos às respectivas faixas salariais.
* A organização dos resultados por cargo e faixa tornou a análise mais clara.

---

## 22/09/2026 — Análise Exploratória da Query 1 (EDA em Python)

### Objetivo

Explorar os dados da Query 1 utilizando Pandas e Matplotlib para identificar padrões relacionados aos salários e departamentos.

### Atividades realizadas

* Leitura do arquivo tratado da Query 1.
* Limpeza e preparação dos dados.
* Cálculo de estatísticas descritivas.
* Cálculo de média, mediana, salário mínimo e salário máximo.
* Contagem de funcionários por departamento.
* Criação de histograma dos salários.
* Criação de boxplot dos salários por departamento.
* Exportação dos gráficos para a pasta `graficos/`.

### Resultado final da análise

* **Média salarial:** R$ 6.461,83
* **Mediana salarial:** R$ 6.200,00
* **Menor salário:** R$ 2.100,00
* **Maior salário:** R$ 24.000,00

Os departamentos com maior quantidade de funcionários foram:

* **Shipping:** 45
* **Sales:** 34

### Gráficos gerados

```text
graficos/query1_salarios_histograma.png
graficos/query1_salarios_boxplot.png
```

### Aprendizados

* A estatística descritiva permite compreender rapidamente a distribuição dos salários.
* O histograma facilita a visualização da concentração dos valores.
* O boxplot permite comparar a distribuição salarial entre departamentos e identificar diferenças e possíveis valores extremos.

---

## 22/09/2026 — Análise Exploratória da Query 2 (Funcionários por Região)

### Objetivo

Explorar os dados da Query 2 para compreender a distribuição dos funcionários entre as regiões geográficas.

### Atividades realizadas

* Limpeza e preparação do arquivo `query_02.csv`.
* Contagem de funcionários por região.
* Análise da distribuição entre as regiões.
* Criação de gráfico de barras.
* Exportação do gráfico para a pasta `graficos/`.

### Resultado

A distribuição encontrada foi:

* **Americas:** 70 funcionários.
* **Europe:** 36 funcionários.

### Gráfico gerado

```text
graficos/query2_regioes.png
```

### Aprendizados

* A integração entre diferentes tabelas permitiu ampliar a análise com informações geográficas.
* O gráfico de barras facilitou a comparação da quantidade de funcionários entre as regiões.
* A análise evidenciou uma maior concentração de funcionários na região Americas dentro da base analisada.

---

## 22/09/2026 — Análise Exploratória da Query 3 (Funcionários por Cargo e Faixa Salarial)

### Objetivo

Explorar os dados da Query 3 para identificar a distribuição dos funcionários entre as diferentes faixas salariais e cargos.

### Atividades realizadas

* Limpeza e preparação do arquivo `query_03.csv`.
* Contagem de funcionários por faixa salarial.
* Análise da distribuição entre as faixas.
* Identificação dos cargos com maior quantidade de funcionários.
* Criação de gráfico de barras.
* Exportação do gráfico para a pasta `graficos/`.

### Resultado final

A distribuição dos 107 funcionários entre as faixas salariais foi:

* **6k - 10k:** 40 funcionários.
* **3k - 6k:** 26 funcionários.
* **Até 3k:** 26 funcionários.
* **Acima de 10k:** 15 funcionários.

O cargo com maior quantidade de funcionários foi:

* **Sales Representative:** 30 funcionários.

### Gráfico gerado

```text
graficos/query3_funcionarios_cargo_faixa.png
```

### Aprendizados

* O `CASE WHEN` utilizado na consulta SQL facilitou a criação das categorias salariais.
* A análise conjunta de cargo e faixa salarial permitiu uma visão mais detalhada da distribuição dos funcionários.
* A representação gráfica tornou mais clara a comparação entre cargos e faixas de remuneração.

---

## 22/09/2026 — Organização da documentação do projeto

### Objetivo

Documentar de forma clara o desenvolvimento e os resultados obtidos durante o projeto.

### Atividades realizadas

* Revisão do `README.md`.
* Organização das seções de objetivo, etapas, modelagem, resultados e gráficos.
* Inclusão da estrutura de pastas do projeto.
* Inclusão das tecnologias e ferramentas utilizadas.
* Inclusão das instruções para execução do projeto.
* Inclusão do link para o Diário de Desenvolvimento.
* Revisão das sugestões de melhoria.
* Revisão da conclusão do projeto.

### Resultado

O README passou a apresentar de forma organizada:

* objetivo do projeto;
* consultas desenvolvidas;
* estrutura dos dados;
* resultados das análises;
* gráficos;
* estrutura de pastas;
* tecnologias utilizadas;
* instruções de execução;
* referência ao Diário de Desenvolvimento;
* possibilidades de evolução do projeto.

### Aprendizados

A documentação é uma parte importante do projeto, pois permite que outra pessoa compreenda a finalidade da solução, as ferramentas utilizadas, o processo de desenvolvimento e os resultados obtidos.

---

## 22/09/2026 — Versionamento com Git e GitHub

### Objetivo

Organizar e registrar a evolução do projeto utilizando Git e GitHub.

### Atividades realizadas

* Organização dos arquivos do projeto.
* Estruturação das pastas `src/`, `dados/`, `graficos/`, `sql/` e `docs/`.
* Utilização de commits com mensagens descritivas.
* Organização do histórico do projeto.
* Atualização dos arquivos no repositório remoto.
* Revisão do estado da branch `main`.
* Atualização do README no GitHub.

### Resultado

O projeto ficou organizado e versionado no GitHub, com os arquivos necessários para a entrega e documentação do desenvolvimento.

### Aprendizados

* O Git permite acompanhar as alterações realizadas durante o desenvolvimento.
* Commits com mensagens claras facilitam a compreensão do histórico.
* O GitHub permite disponibilizar o projeto de forma organizada e facilita sua apresentação e avaliação.

### Observação adicional

O vídeo explicativo do projeto foi gravado e será enviado separadamente pelo sistema AVA do SENAI, conforme as exigências da entrega.

---

## 22/09/2026 — Encerramento do Projeto

### Objetivo

Finalizar o desenvolvimento e validar se as exigências do Projeto Avaliativo – Módulo 1 foram contempladas.

### Atividades realizadas

* Revisão das queries SQL.
* Revisão dos arquivos CSV utilizados nas análises.
* Conferência das análises exploratórias.
* Conferência dos gráficos gerados.
* Organização da estrutura de pastas.
* Revisão e atualização do `README.md`.
* Atualização do Diário de Desenvolvimento.
* Validação do versionamento no GitHub.
* Conferência da branch `main`.
* Conferência dos arquivos necessários para a entrega.

### Entregáveis finais

O projeto contém:

* Queries SQL das três análises.
* Arquivos de dados utilizados.
* Código Python para tratamento e análise dos dados.
* Gráficos das análises exploratórias.
* README com documentação do projeto.
* Diário de Desenvolvimento.
* Versionamento utilizando Git e GitHub.

## 23/09/2026 — Ajustes finais e encerramento do projeto

Nesta data foram realizados os ajustes finais na documentação do projeto, principalmente no README.md e no DIARIO_DE_DESENVOLVIMENTO.md, com o objetivo de revisar as informações apresentadas, melhorar a organização do conteúdo e garantir que a documentação estivesse de acordo com o desenvolvimento realizado.

Também foi realizada uma revisão final da estrutura do projeto e dos principais entregáveis, incluindo:

consultas SQL desenvolvidas;
arquivos de dados utilizados nas análises;
código Python para tratamento e análise dos dados;
gráficos gerados;
README.md;
DIARIO_DE_DESENVOLVIMENTO.md;
organização e versionamento do projeto no GitHub.

Após os ajustes e a revisão final, o projeto foi considerado concluído.

### Conclusão

O projeto foi concluído em **23/09/2026**, contemplando as etapas de extração dos dados, tratamento, análise exploratória, visualização e documentação.

Durante o desenvolvimento foram trabalhados conceitos de SQL, relacionamentos entre tabelas, tratamento de arquivos CSV, Python, Pandas, Matplotlib, análise exploratória de dados, Git e GitHub.

Além dos resultados obtidos nas três consultas, o projeto proporcionou a experiência prática de identificar problemas nos dados, investigar suas causas, implementar soluções e documentar todo o processo de desenvolvimento.

O projeto também apresenta possibilidades de evolução, como a criação de um dashboard interativo em Power BI, inclusão de novos indicadores e automatização da atualização dos dados.
