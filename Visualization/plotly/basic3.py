import plotly.express as px
 
# Loading the data
df = px.data.tips()
 
# Creating the bar chart
fig = px.bar(df, x='day', y="total_bill")
 
fig.show()