import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import plotly.express as px

# Load data from notebook.ipynb
# Assuming the data is saved in a CSV file after processing in the notebook
data = pd.read_csv('/D:/1 Programming/python/jupyter/Bike_Sharing_Analysis/notebook_data.csv')

# Example questions and answers
questions_answers = [
    {
        "question": "What is the peak hour for bike sharing?",
        "answer": "The peak hour for bike sharing is 5 PM."
    },
    {
        "question": "Which day of the week has the highest bike usage?",
        "answer": "Saturday has the highest bike usage."
    }
]

# Create a Dash application
app = dash.Dash(__name__)

# Create a figure for visualization
fig = px.line(data, x='hour', y='count', title='Bike Sharing Count by Hour')

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Bike Sharing Analysis Dashboard'),

    html.Div(children='''
        This dashboard provides insights from the bike sharing data analysis.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.H2(children='Questions and Answers'),
    html.Ul(children=[
        html.Li(children=[
            html.Strong(q['question']),
            html.P(q['answer'])
        ]) for q in questions_answers
    ])
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

