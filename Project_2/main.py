import pandas as pd 
import plotly.express as px 

df = pd.read_csv('avocado-updated-2020.csv')
df.info()

print(df['type'].value_counts(dropna=False))
print(df['geography'].value_counts(dropna=False))

msk = df['geography'] == 'Los Angeles'
px.line(df[msk], x='date', y='average_price', color='type')