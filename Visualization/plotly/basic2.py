import plotly.express as px
 
# using the iris dataset
df = px.data.iris()
 
# plotting the line chart
fig = px.line(df, y="sepal_width", line_dash='species',
              color='species')
 
# showing the plot
fig.show()