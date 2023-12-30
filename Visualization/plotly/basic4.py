
import plotly.express as px
 
# using the dataset
df = px.data.tips()
 
# plotting the scatter chart
fig = px.scatter(df, x='total_bill', y="tip")
 
# showing the plot
fig.show()