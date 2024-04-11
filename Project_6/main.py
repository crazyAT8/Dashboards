# Import Package
from dash import Dash, html 

# Initialize the app
app = Dash(__name__)

# App Layout
app.layout = html.Div([
    html.Div(children='Hello World')
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)