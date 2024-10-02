import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from decimal import Decimal

# Conectar ao MySQL
connection = mysql.connector.connect(
    host="localhost",
    database="sales_management",
    user="root",
    password="Deskmk1",
)
cursor = connection.cursor()

# Consulta SQL para obter as vendas totais por produtos
query = """
    SELECT p.name, SUM(s.quantity) AS total_quantity_sold
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY p.name
"""

cursor.execute(query)

# Extrair os resultados da consulta
results = cursor.fetchall()

# Criar um DataFrame para armazenar os dados
df = pd.DataFrame(results, columns=["Product", "Total Sold"])

# Converter a coluna 'Total Sold' para float, caso esteja em formato Decimal
df["Total Sold"] = df["Total Sold"].apply(
    lambda x: float(x) if isinstance(x, Decimal) else x
)

# Fechar a conexão
cursor.close()
connection.close()

# Plotar o gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(
    x="Product", y="Total Sold", data=df, palette="Blues_d"
)  # Usando uma paleta de cores mais amigável
plt.title(
    "Total de Vendas por Produto", fontsize=16, fontweight="bold"
)  # Título mais destacado
plt.xlabel("Produto", fontsize=12)  # Label ajustado para o eixo X
plt.ylabel("Total Vendido", fontsize=12)  # Label ajustado para o eixo Y
plt.xticks(rotation=0, ha="center")  # Deixa os rótulos na horizontal
plt.tight_layout()  # Ajusta o layout para evitar cortes

# Adicionar valores no topo das barras
for i in range(len(df)):
    plt.text(
        i,
        df["Total Sold"][i] + 0.1,
        round(df["Total Sold"][i], 2),
        ha="center",
        fontsize=10,
    )

# Exibir o gráfico
plt.show()
