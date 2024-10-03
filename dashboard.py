import dash
from dash import dcc, html
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Criar a conexão com o banco de dados
engine = create_engine("mysql+pymysql://root:Deskmk1@localhost/sales_management")

# Consultar os dados de vendas
query = """
    SELECT p.name AS Product, SUM(s.quantity) AS Total_Sold
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY p.name
"""

# Carregar os dados em um DataFrame
df = pd.read_sql(query, engine)

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div(
    style={"textAlign": "center"},  # Centraliza todo o conteúdo
    children=[
        html.H1("Dashboard de Vendas"),
        dcc.Graph(id="grafico-vendas"),
        dcc.Dropdown(
            id="dropdown-produtos",
            options=[
                {"label": row["Product"], "value": row["Product"]}
                for index, row in df.iterrows()
            ],
            value=None,  # Deixe o dropdown sem valor inicial
            placeholder="Selecione um produto",
            multi=False,
        ),
        html.Button("Home", id="home-button", n_clicks=0),  # Botão de Home
    ],
)


# Callback para atualizar o gráfico
@app.callback(
    dash.dependencies.Output("grafico-vendas", "figure"),
    [dash.dependencies.Input("dropdown-produtos", "value")],
)
def update_graph(selected_product):
    if selected_product is None:
        filtered_df = df  # Exibir todos os produtos
    else:
        filtered_df = df[
            df["Product"] == selected_product
        ]  # Filtrar produtos selecionados

    # Criar o gráfico de barras
    fig = px.bar(
        filtered_df, x="Product", y="Total_Sold", title="Total de Vendas por Produto"
    )

    # Atualizar o layout do gráfico
    fig.update_layout(
        title="Total de Vendas por Produto",
        xaxis_title="Produto",
        yaxis_title="Total Vendido",
        height=400,
        width=800,
    )

    return fig


# Callback para o botão Home
@app.callback(
    dash.dependencies.Output("dropdown-produtos", "value"),
    [dash.dependencies.Input("home-button", "n_clicks")],
)
def reset_dropdown(n_clicks):
    if n_clicks > 0:
        return None  # Reseta o dropdown para o estado inicial
    return dash.no_update  # Não altera o valor se o botão não foi clicado


# Executar o aplicativo
if __name__ == "__main__":
    app.run_server(debug=True)
