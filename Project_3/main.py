import plotly.express as px 

fig = px.bar(x=["a", "b", "c"], y=[1, 2, 3])
fig.write_html('first_figure.html', auto_open=True)