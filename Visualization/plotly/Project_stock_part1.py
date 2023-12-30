import dash
from dash import html
from dash import dcc
# from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

# Load datapd.read_csv(r'D:\\Guvi\dashboard\tips.csv')
df = pd.read_csv(r'D:\\Guvi\dashboard\stockdata2.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('DASH - STOCK PRICES'),
                                 html.P('Visualising time series with Plotly - Dash.'),
                                 html.P('Pick one or more stocks from the dropdown below.'),
                                ]
                             )
                              ])
        ]

)


if __name__ == '__main__':
    app.run_server(debug=True)
