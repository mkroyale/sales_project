import pandas as pd
import mysql.connector
from mysql.connector import Error

# Conectar ao MySQL
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='sales_management',
        user='root',  # Substitua pelo seu usuário do MySQL
        password='Deskmk1'  # Substitua pela sua senha do MySQL
    )
    if connection.is_connected():
        cursor = connection.cursor()

        # Carregar dados de produtos
        products_df = pd.read_csv('products.csv')
        for index, row in products_df.iterrows():
            cursor.execute("""
                INSERT INTO products (name, price)
                VALUES (%s, %s)
            """, (row['name'], row['price']))
        connection.commit()

        # Carregar dados de clientes
        customers_df = pd.read_csv('customers.csv')
        for index, row in customers_df.iterrows():
            cursor.execute("""
                INSERT INTO customers (name, email)
                VALUES (%s, %s)
            """, (row['name'], row['email']))
        connection.commit()

        # Carregar dados de vendas
        sales_df = pd.read_csv('sales.csv')
        for index, row in sales_df.iterrows():
            cursor.execute("""
                INSERT INTO sales (product_id, customer_id, quantity, sale_date)
                VALUES (%s, %s, %s, %s)
            """, (row['product_id'], row['customer_id'], row['quantity'], row['sale_date']))
        connection.commit()

        print("Dados carregados com sucesso no banco de dados!")

except Error as e:
    print(f"Erro: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
