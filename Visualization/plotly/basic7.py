import plotly.graph_objects as px
import numpy as np
import pandas as pd
 
df = pd.read_csv(r'D:\\Guvi\dashboard\tips.csv')
 
plot = px.Figure(data=[px.Scatter(
    x=df['day'],
    y=df['tip'],
    mode='markers',)
])
 
# Add dropdown
plot.update_layout(
    updatemenus=[
        dict(buttons=list([
            dict(
                args=["type", "scatter"],
                label="Scatter Plot",
                method="restyle"
            ),
            dict(
                args=["type", "bar"],
                label="Bar Chart",
                method="restyle"
            )
        ]),
            direction="down",
        ),
    ]
)
 
plot.show()