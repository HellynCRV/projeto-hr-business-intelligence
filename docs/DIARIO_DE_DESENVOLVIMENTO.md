# Diário de Desenvolvimento — Projeto HR BI

Este documento registra o processo de desenvolvimento do projeto,
incluindo decisões técnicas, problemas encontrados, soluções adotadas
e aprendizados obtidos durante a construção da solução de Business
Intelligence aplicada à área de Recursos Humanos.

---

## 18/09/2026 — Desenvolvimento da Query 1 (Salários por Departamento e Cargo)

### Objetivo
Construir a primeira consulta SQL solicitada no projeto, analisando a distribuição de salários por departamento e cargo.

### Atividades realizadas
- Acesso ao banco FreeSQL (schema HR).
- Criação da consulta `query_1.sql` utilizando `LEFT JOIN` entre as tabelas EMPLOYEES, DEPARTMENTS e JOBS.
- Aplicação de filtro simples com `WHERE SALARY > 0` para garantir consistência dos dados.
- Execução da query e validação dos resultados.
- Exportação do resultado para o arquivo `dados/query_01.csv`.

### Estrutura da Query
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

### Resultado
Arquivo `query_01.csv` gerado com 58 registros e 6 colunas.  
Dados prontos para serem utilizados na análise exploratória em Python.

### Aprendizados
- A importância de validar a query com filtros simples para evitar registros inconsistentes.  
- O uso de `LEFT JOIN` garantiu que todos os funcionários fossem incluídos, mesmo que alguns não tivessem departamento ou cargo associado.

### Observação adicional:  
Durante os testes iniciais, também foi utilizada a condição WHERE SALARY > 5000 ORDER BY SALARY DESC para explorar apenas os salários mais altos. Essa variação ajudou a entender melhor a distribuição dos maiores salários, mas não corresponde ao escopo oficial da Query 1.
A versão final entregue segue o enunciado do projeto, utilizando WHERE SALARY > 0 para representar a distribuição completa dos salários por departamento e cargo, garantindo consistência nos dados exportados para o arquivo query_01.csv.
---

## 21/09/2026 — Configuração inicial do projeto

### Objetivo
Preparar o ambiente de desenvolvimento para iniciar a análise dos dados de Recursos Humanos utilizando Python e Pandas.

### Atividades realizadas
- Estruturação inicial do projeto `Projeto_HR_BI`.
- Criação do ambiente virtual `.venv`.
- Ativação do ambiente virtual.
- Instalação da biblioteca Pandas.
- Criação do script `src/analisar_dados.py`.
- Identificação do arquivo de dados `dados/query_01.csv`.

### Ambiente utilizado
- Python  
- Pandas  
- Visual Studio Code  
- PowerShell  
- Ambiente virtual Python (`.venv`)

---

## 21/09/2026 — Primeiro teste de leitura dos dados

### Objetivo
Realizar a leitura do arquivo CSV utilizando o Pandas e verificar sua estrutura.

### Código inicial
    df = pd.read_csv(arquivo)

### Resultado inicial
O arquivo foi carregado, porém os dados não foram interpretados corretamente.  

- 58 linhas  
- 58 colunas identificadas pelo código  
- Apenas uma coluna aparecia na lista de nomes das colunas  

Saída:
    ['EMPLOYEE_ID,"FIRST_NAME","LAST_NAME","SALARY","DEPARTMENT_NAME","JOB_TITLE"']

### Problema identificado
Os dados deveriam possuir seis campos:
- EMPLOYEE_ID  
- FIRST_NAME  
- LASTNAME  
- SALARY  
- DEPARTMENT_NAME  
- JOB_TITLE  

Porém, o Pandas estava interpretando cada linha de forma incorreta.

---

### Investigação da estrutura do CSV
Com a ajuda da IA, foi utilizado o comando:
    Get-Content dados\query_01.csv -TotalCount 2

**Resultado:**  
Foi identificada uma estrutura de aspas diferente do formato CSV convencional:
    "EMPLOYEE_ID,""FIRST_NAME"",""LAST_NAME"",""SALARY"",""DEPARTMENT_NAME"",""JOB_TITLE"""

Também foi identificado que os campos estavam separados por vírgulas.

### Conclusão
O problema estava relacionado à formatação do arquivo de origem, principalmente à forma como as aspas estavam estruturadas.

---

## 21/09/2026 — Tratamento da leitura do CSV

### Objetivo
Corrigir a interpretação dos dados antes de iniciar a análise.

### Tentativa inicial
    pd.read_csv(arquivo, sep=",")

Porém, apenas informar o separador não foi suficiente para corrigir completamente a estrutura das aspas do arquivo.

### Solução implementada
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

---

## Validação da estrutura dos dados
Após o tratamento, o DataFrame passou a apresentar a estrutura esperada.

**Resultado:**
- Quantidade de linhas: 58  
- Quantidade de colunas: 6  

Colunas identificadas:
- EMPLOYEE_ID  
- FIRST_NAME  
- LASTNAME  
- SALARY  
- DEPARTMENT_NAME  
- JOB_TITLE  

Correção aplicada:
    len(df.columns)

**Resultado final da validação:**
- Quantidade de linhas: 58  
- Quantidade de colunas: 6  
- [5 rows x 6 columns]

---

## Situação atual
A etapa de carregamento e validação inicial dos dados foi concluída.  

O conjunto possui:
- 58 registros  
- 6 atributos  
- Identificação do funcionário  
- Nome e sobrenome  
- Salário  
- Departamento  
- Cargo  

---

## Aprendizados desta etapa
- Importância de verificar a estrutura real dos dados antes de iniciar uma análise.  
- Problemas podem parecer relacionados ao Pandas ou ao separador, mas a inspeção direta do arquivo revelou que a origem estava na formatação do CSV.  
- Necessidade de validar o DataFrame após a importação:
  - Quantidade de registros  
  - Quantidade de colunas  
  - Nomes das colunas  
  - Primeiras linhas dos dados  

Essa validação evita iniciar análises sobre uma estrutura de dados incorreta.

## 21/09/2026 — Desenvolvimento da Query 2 (Funcionários por Região e Localização)

### Objetivo
Analisar a distribuição de funcionários por região, incluindo informações de localização (cidade, estado, país e região).

### Atividades realizadas
- Acesso ao banco FreeSQL (schema HR).
- Criação da consulta `query_2.sql` utilizando múltiplos `LEFT JOIN` entre EMPLOYEES, DEPARTMENTS, LOCATIONS, COUNTRIES e REGIONS.
- Aplicação de filtro simples para garantir consistência dos dados.
- Execução da query e validação dos resultados.
- Exportação do resultado para o arquivo `dados/query_02.csv`.

### Estrutura da Query
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

### Resultado
Arquivo `query_02.csv` gerado com registros contendo informações de funcionários, departamentos e localização completa (cidade, estado, país e região).  
Dados prontos para análise exploratória em Python.

### Aprendizados
- A importância de relacionar múltiplas tabelas para enriquecer a análise com informações geográficas.  
- O uso de `LEFT JOIN` garantiu que todos os funcionários fossem incluídos, mesmo que alguns não tenham localização detalhada.  
- O filtro `WHERE r.region_name IS NOT NULL` assegurou consistência nos dados exportados.

## 21/09/2026 – Desenvolvimento da Query 3 (Funcionários por Cargo e Faixa Salarial)
### Aprendizados
- O uso de `CASE WHEN` permitiu agrupar salários em faixas, facilitando a análise da distribuição salarial.
- A junção com a tabela `HR.JOBS` trouxe insights sobre como diferentes cargos se concentram em determinadas faixas de remuneração.
- A ordenação por cargo e faixa salarial deixou os resultados mais organizados e claros para interpretação.

## 22/09/2026 — Análise Exploratória da Query 1 (EDA em Python)
### Objetivo
Explorar os dados da Query 1 utilizando Pandas e Matplotlib para identificar padrões salariais.

### Atividades realizadas
Leitura do arquivo query_01_limpo.csv.

Cálculo de estatísticas descritivas (média, mediana, mínimo e máximo).

Contagem de funcionários por departamento.

Criação de gráficos: histograma de salários e boxplot por departamento.

Exportação dos gráficos para a pasta graficos/.

### Resultado
Média salarial: 6461,83

Mediana salarial: 6200

Faixa salarial entre 2100 e 24000.

Departamentos com maior número de funcionários: Shipping (45) e Sales (34).

Gráficos salvos em graficos/query1_salarios_histograma.png e graficos/query1_salarios_boxplot.png.

### Aprendizados
A visualização gráfica facilita a interpretação dos dados.

O boxplot evidenciou diferenças significativas entre departamentos.

## 22/09/2026 — Análise Exploratória da Query 2 (Funcionários por Região)
### Objetivo
Explorar os dados da Query 2 para entender a distribuição de funcionários por localização.

### Atividades realizadas
Limpeza do arquivo query_02.csv.

Contagem de funcionários por região (Americas e Europe).

Criação de gráfico de barras mostrando a distribuição.

Exportação do gráfico para a pasta graficos/.

### Resultado
Americas: 70 funcionários.

Europe: 36 funcionários.

Gráfico salvo em graficos/query2_regioes.png.

### Aprendizados
A integração de múltiplas tabelas enriqueceu a análise com dados geográficos.

A predominância da região Americas reflete a concentração da base de dados.

## 22/09/2026 — Análise Exploratória da Query 3 (Faixas Salariais por Cargo)
### Objetivo
Explorar os dados da Query 3 para identificar a distribuição de funcionários por faixa salarial.

### Atividades realizadas
Limpeza do arquivo query_03.csv.

Contagem de funcionários por faixa salarial.

Criação de gráfico de barras mostrando a predominância das faixas.

Exportação do gráfico para a pasta graficos/.

### Resultado
Faixa acima de 10k: 8 funcionários.

Faixa entre 6k–10k: 7 funcionários.

Faixa entre 3k–6k: 7 funcionários.

Faixa até 3k: 3 funcionários.

Gráfico salvo em graficos/query3_departamentos.png.

### Aprendizados
O uso de CASE WHEN na query SQL foi essencial para agrupar salários.

A análise mostrou concentração em faixas mais altas, indicando cargos de maior responsabilidade.

## 22/09/2026 — Versionamento com GitHub (Branches e Commits)
### Objetivo
Organizar o histórico do projeto utilizando Git e GitHub.

### Atividades realizadas
Criação de branches para cada etapa (feature/query1-eda, feature/query2-eda, feature/query3-eda).

Commits com mensagens descritivas.

Merge das branches na main.

Organização da estrutura de pastas (src/, dados/, graficos/, docs/).

### Resultado
Repositório organizado e pronto para entrega, com histórico claro de evolução.

### Aprendizados
O uso de branches facilita o desenvolvimento incremental.

Commits bem descritos tornam o projeto mais profissional e fácil de acompanhar.

### Observação adicional
O vídeo explicativo do projeto foi gravado e será enviado separadamente pelo sistema AVA do SENAI, conforme exigências da entrega.

## 22/09/2026 — Encerramento do Projeto
### Objetivo
Finalizar o desenvolvimento e validar se todas as exigências do Projeto Avaliativo – Módulo 1 foram contempladas.

### Atividades realizadas
Revisão das queries SQL e dos arquivos CSV gerados.

Conferência das análises exploratórias (EDA) com gráficos salvos na pasta graficos/.

Organização da estrutura de pastas (src, dados, graficos, sql, docs).

Criação e atualização do arquivo README.md com objetivos, etapas, resultados e referência ao Diário de Desenvolvimento.

Validação do versionamento no GitHub (branches, commits descritivos e merge na main).

### Conclusão
O projeto foi concluído em 22/09/2026, atendendo integralmente às exigências do módulo.
A entrega final inclui queries SQL, tratamento dos dados, análises exploratórias com gráficos, documentação completa e versionamento profissional no GitHub.