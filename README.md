Este projeto é uma aplicação de visualização de dados de vendas de produtos, utilizando Python, MySQL, e bibliotecas de visualização de dados como Matplotlib e Seaborn. Ele oferece uma solução para extrair, transformar e visualizar dados de vendas de forma gráfica e interativa.

Funcionalidades
Conexão com banco de dados MySQL para obtenção de dados de vendas.
Visualização gráfica dos dados de vendas utilizando gráficos de barras.
Processo de ETL (Extract, Transform, Load) para carregar dados de arquivos CSV no banco de dados.
Tecnologias Utilizadas
Python: Linguagem principal do projeto.
MySQL: Para armazenamento e consulta de dados de vendas.
Pandas: Para manipulação de dados.
Matplotlib e Seaborn: Para visualização de dados em gráficos.
Como Executar o Projeto

1. Instalar as Dependências
   Execute o seguinte comando para instalar todas as bibliotecas necessárias:

bash
Copiar código
pip install mysql-connector-python pandas matplotlib seaborn 2. Configurar o Banco de Dados
Configure o banco de dados MySQL com o script SQL (caso necessário).

3. Executar o Script de ETL
   Execute o script de ETL para carregar os dados no banco de dados:

bash
Copiar código
python etl_sales.py 4. Visualizar os Gráficos
Visualize os gráficos de vendas utilizando o seguinte comando:

bash
Copiar código
python visualize_sales.py
Estrutura do Projeto
graphql
Copiar código
├── etl_sales.py # Script de ETL para carregar dados CSV no banco de dados MySQL
├── visualize_sales.py # Script para gerar gráficos de vendas por produto
├── clientes.csv # Arquivo CSV com dados de clientes
├── produtos.csv # Arquivo CSV com dados de produtos
├── vendas.csv # Arquivo CSV com dados de vendas
└── README.md # Instruções e detalhes do projeto
