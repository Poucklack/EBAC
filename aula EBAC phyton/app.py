import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Carregando o DataFrame
df = pd.read_csv("ecommerce_estatistica.csv")

# Inicializando o app
app = dash.Dash(__name__)
app.title = "Dashboard de E-commerce"

# Criando alguns gráficos com Plotly
fig_vendas_categoria = px.bar(df, x='Categoria', y='Vendas', title='Vendas por Categoria')
fig_vendas_estado = px.pie(df, names='Estado', values='Vendas', title='Vendas por Estado')
fig_lucro_tempo = px.line(df, x='Data', y='Lucro', title='Lucro ao Longo do Tempo')

# Layout da aplicação
app.layout = html.Div(children=[
    html.H1("Painel Interativo de E-commerce", style={'textAlign': 'center'}),
    
    html.Div([
        dcc.Graph(figure=fig_vendas_categoria),
        dcc.Graph(figure=fig_vendas_estado),
        dcc.Graph(figure=fig_lucro_tempo),
    ])
])

# Rodando o servidor
if __name__ == "__main__":
    app.run_server(debug=True)
