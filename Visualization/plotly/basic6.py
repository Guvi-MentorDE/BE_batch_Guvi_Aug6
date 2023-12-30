import plotly.express as px
 
# Loading the iris dataset
df = px.data.tips()
 
fig = px.pie(df, values="total_bill", names="day")
fig.show()