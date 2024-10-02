# Sales Project - Visualização de Vendas

Este projeto é uma aplicação de visualização de dados de vendas de produtos, utilizando Python, MySQL e bibliotecas de visualização de dados como Matplotlib e Seaborn.

## Funcionalidades

- Conexão com banco de dados MySQL para obtenção de dados de vendas.
- Visualização gráfica dos dados de vendas por produto utilizando gráficos de barras.
- Processo de ETL (Extract, Transform, Load) para carregar dados de arquivos CSV no banco de dados.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **MySQL**: Para armazenamento e consulta dos dados de vendas.
- **Pandas**: Para manipulação de dados.
- **Matplotlib e Seaborn**: Para visualização dos dados em gráficos.

## Como executar o projeto

1. Instale as bibliotecas necessárias:
   ```bash
   pip install mysql-connector-python pandas matplotlib seaborn
   ```

Configure o banco de dados MySQL com o script SQL (caso necessário).

Execute o script de ETL para carregar os dados no banco:

bash

python etl_sales.py

Visualize os gráficos com o script de visualização:
bash

python visualize_sales.py

Estrutura do Projeto

etl_sales.py: Script de ETL para carregar dados CSV no banco de dados MySQL.
visualize_sales.py: Script para gerar gráficos de vendas por produto.
customers.csv, products.csv, sales.csv: Arquivos de dados CSV utilizados no projeto
