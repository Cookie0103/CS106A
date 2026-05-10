# x and y given as array_like objects
import plotly.express as px

fig = px.bar(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16], title="Testing out Plotly")

fig.show()