# iFood Case Study

Este projeto contém a análise e modelagem de dados para um case study do iFood.

## Estrutura do Projeto

```
ifood-case/
├── data/                       # Datasets
│   ├── raw/                   # Dados originais (JSON)
│   │   ├── offers.json        # Dados de ofertas
│   │   ├── profile.json       # Dados de perfil dos usuários
│   │   └── transactions.json  # Dados de transações
│   └── processed/             # Dados processados (Parquet)
│       └── offers_processed.parquet/  # Ofertas processadas
├── notebooks/                 # Jupyter notebooks para análise
│   ├── 1_data_processing.ipynb    # Processamento e limpeza dos dados
│   ├── 2_data_exploratory.ipynb  # Análise exploratória dos dados
│   ├── 3_modeling.ipynb           # Modelagem e machine learning
│   └── artifacts/                 # Artefatos do Spark
├── src/                       # Código fonte modular
│   └── utils.py              # Funções utilitárias (Spark, carregamento de dados)
├── presentation/              # Slides e materiais para stakeholders
├── README.md                 # Este arquivo
└── requirements.txt          # Dependências do projeto
```

## Como Usar

### 1. Configuração do Ambiente

```bash
# Clone o repositório
git clone <repository-url>
cd ifood-case

# Criar ambiente virtual (recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou .venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 2. Estrutura de Execução

Os notebooks devem ser executados na seguinte ordem:

1. **`1_data_processing.ipynb`** - Processamento inicial dos dados
2. **`2_data_exploratory.ipynb`** - Análise exploratória 
3. **`3_modeling.ipynb`** - Modelagem e machine learning

### 3. Tecnologias Utilizadas

- **PySpark**: Processamento distribuído de dados em larga escala
- **Pandas**: Manipulação e análise de dados
- **Scikit-learn**: Machine learning (modelos de ensemble)
- **LightGBM**: Gradient boosting otimizado
- **Matplotlib/Seaborn**: Visualização de dados

### 4. Execução

```bash
# Iniciar Jupyter
jupyter notebook

# Ou usar Jupyter Lab
jupyter lab
```

## Notebooks

### 📊 1_data_processing.ipynb
- **Objetivo**: Processamento e limpeza dos dados brutos
- **Principais atividades**:
  - Configuração do ambiente PySpark
  - Carregamento dos dados JSON (offers, profile, transactions)
  - Limpeza e transformação dos dados
  - Salvamento dos dados processados em formato Parquet
- **Saídas**: Dados processados na pasta `data/processed/`

### 🔍 2_data_exploratory.ipynb  
- **Objetivo**: Análise exploratória detalhada dos dados
- **Principais atividades**:
  - Análise estatística descritiva
  - Visualizações de distribuições e correlações
  - Identificação de padrões nos dados
  - Análise de ofertas, perfis de usuários e transações
- **Ferramentas**: Matplotlib, Seaborn para visualizações

### 🤖 3_modeling.ipynb
- **Objetivo**: Modelagem preditiva e causal inference
- **Principais atividades**:
  - Preparação dos dados para modelagem
  - Implementação de modelos de machine learning
  - Análise de uplift/causal inference usando T-Learner
  - Avaliação de modelos (AUC, métricas de regressão)
  - Interpretação dos resultados
- **Modelos**: Random Forest, Gradient Boosting, T-Learner para uplift modeling


## Dados

### Datasets Disponíveis

#### 📁 raw/ - Dados Originais
- **`offers.json`**: Informações sobre ofertas/campanhas promocionais
- **`profile.json`**: Dados demográficos e comportamentais dos usuários
- **`transactions.json`**: Histórico de transações dos clientes

#### 📁 processed/ - Dados Processados
- **`offers_processed.parquet/`**: Dados de ofertas limpos e estruturados em formato Parquet para otimização de performance

### Características dos Dados
- **Formato original**: JSON (dados semi-estruturados)
- **Formato processado**: Parquet (colunar, otimizado para analytics)
- **Processamento**: PySpark para escalabilidade
- **Armazenamento**: Local filesystem com possibilidade de migração para cloud storage

### Considerações Técnicas
- Os dados brutos são mantidos intactos para rastreabilidade
- Formato Parquet oferece compressão e query performance otimizada
- Pipeline de processamento documented nos notebooks