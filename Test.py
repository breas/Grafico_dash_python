
from dash import Dash,html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

#criação gráfico com dash e plotly para exibir na web

df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")

app.layout = html.Div(children=[
                    html.H1(children='Faturamento de venda'),
                    html.H2(children = 'Gráfico com o faturamento de todos os sprodutos separados por loja'),
                    html.Div(children='''
                            Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
                        '''),
            html.Div(id="texto"),
                        dcc.Dropdown(opcoes, value='Todas as Lojas', id='Lista de Lojas'),

                        dcc.Graph(
                            id='grafico_quantidade_vendas',
                            figure=fig
                        )
])

@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('Lista de Lojas', 'value')
)
def update_output(value):
    if value == "Todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df["ID Loja"]==value, :]  
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=True)