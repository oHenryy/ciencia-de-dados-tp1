# Trabalho Prático TP1: Análise Exploratória de Duas Bases Reais

Resolução em Jupyter Notebook do **Trabalho Prático TP1 (individual)** da disciplina *Ciência de Dados 1*
(Sistemas de Informação, Escola Superior de Tecnologia / UEA, 2026/02), com ênfase em **Pandas**
e **Matplotlib**.

O enunciado completo está em [`Trabalho Prático TP1.pdf`](Trabalho%20Prático%20TP1.pdf).

## Conteúdo

- [`TP1_Analise_Exploratoria.ipynb`](TP1_Analise_Exploratoria.ipynb): notebook com as 8 etapas do trabalho, executável do início ao fim.
- [`netflix_titles.csv`](netflix_titles.csv) e [`StudentsPerformance.csv`](StudentsPerformance.csv): as duas bases analisadas.
- [`scripts/baixar_bases.py`](scripts/baixar_bases.py): script que baixa novamente as bases do Kaggle.
- [`Trabalho Prático TP1.pdf`](Trabalho%20Prático%20TP1.pdf): enunciado original.

## Estrutura do notebook

| Etapa | Base | Conteúdo |
| --- | --- | --- |
| 1. Conhecendo e preparando os dados | Netflix | carga, dimensões, head/tail, tipos, ausentes, duplicados, `describe()`, problemas encontrados e tratamento |
| 2. Investigação dos dados | Netflix | 8 perguntas (tipos, países, diretores, classificações, anos, décadas, durações, filme mais antigo/recente) |
| 3. Visualização dos dados | Netflix | 4 gráficos (Movies × TV Shows, top 10 países, títulos por ano, categorias mais frequentes) |
| 4. Conhecendo e preparando os dados | Estudantes | carga, head/tail, dimensões, tipos, ausentes, duplicados, `describe()`, média e mediana |
| 5. Análise do desempenho | Estudantes | 10 perguntas (médias, medianas, `media_geral`, top 10, aprovação, gênero, curso, escolaridade, grupo) |
| 6. Visualização dos dados | Estudantes | 5 gráficos (distribuição de Matemática, médias por disciplina, gênero, curso, Matemática × Leitura) |
| 7. Investigação livre | ambas | 4 perguntas próprias (2 por base): pergunta → tratamento → análise → gráfico → conclusão |
| 8. Conclusões | ambas | descobertas, dificuldades, comparação entre as bases e limitações |

## Regras da atividade

- Toda a manipulação de dados usa **Pandas** (DataFrames, leitura de arquivos, seleção, filtros,
  indexação, agrupamentos e estatísticas); todos os gráficos usam **Matplotlib**.
- Cada questão traz **código, resultado e uma breve interpretação** em markdown.
- Todo gráfico traz título, identificação dos eixos X/Y e legenda quando há mais de uma série; cada
  entidade (Movie/TV Show, gênero, curso preparatório) mantém a mesma cor em todo o notebook.
- As conclusões são descritivas (sem testes de hipótese, conforme o enunciado).

## Como executar

### 1. Clonar e criar o ambiente

```bash
git clone <url-do-repositorio>
cd ciencia-de-dados-tp1
python -m venv .venv
```

Ativar o ambiente:

```bash
# Windows (PowerShell/cmd)
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

Instalar as dependências:

```bash
pip install -r requirements.txt
```

### 2. Registrar o kernel do Jupyter (opcional, recomendado)

```bash
python -m ipykernel install --user --name=tp1-ciencia-dados --display-name "Python (tp1-ciencia-dados)"
```

### 3. Abrir e rodar

```bash
jupyter notebook TP1_Analise_Exploratoria.ipynb
```

Selecione o kernel **Python (tp1-ciencia-dados)** e execute **Kernel → Restart & Run All**.

Alternativamente, sem abrir a interface, para validar que o notebook roda sem erros do início ao fim:

```bash
jupyter nbconvert --to notebook --execute --inplace TP1_Analise_Exploratoria.ipynb
```

## Bases de dados

As duas bases **já estão incluídas neste repositório**, na raiz, ao lado do notebook, com o nome
exato esperado por ele. Para baixá-las novamente do Kaggle:

```bash
python scripts/baixar_bases.py
```

| Base | Etapas | Arquivo | Fonte | Formato |
| --- | --- | --- | --- | --- |
| Netflix Movies and TV Shows | 1, 2, 3, 7, 8 | `netflix_titles.csv` | [Kaggle: shivamb/netflix-shows](https://www.kaggle.com/datasets/shivamb/netflix-shows) | CSV `,`, UTF-8; 8.807 linhas × 12 colunas (catálogo até set/2021) |
| Students Performance in Exams | 4, 5, 6, 7, 8 | `StudentsPerformance.csv` | [Kaggle: spscientist/students-performance-in-exams](https://www.kaggle.com/spscientist/students-performance-in-exams) | CSV `,`, UTF-8; 1.000 linhas × 8 colunas |

## Critérios de avaliação

| Etapa | Pontos |
| --- | --- |
| 1. Netflix: preparação | 1,0 |
| 2. Netflix: investigação | 1,2 |
| 3. Netflix: gráficos | 0,8 |
| 4. Estudantes: preparação | 1,0 |
| 5. Estudantes: investigação | 1,5 |
| 6. Estudantes: gráficos | 1,0 |
| 7. Investigação livre | 1,0 |
| 8. Conclusões | 0,5 |
| **Total (notebook)** | **8,0** |

Nota de defesa: de 0 a 1,0. **Nota final = notebook × defesa.** Entrega em 19/10; defesas em 20 e 22/10.

## Autor

Henrique da Silva Furtado
