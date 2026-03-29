import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Sample Data: Modify this according to your needs
queue_data = {
    'Segment': ["A", "B", "C"],
    'Arrival Rate': [2, 3, 4],
    'Service Rate': [3, 4, 5]
}

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Queuing Theory Dashboard"),
    dcc.Dropdown(
        id='queue-selector',
        options=[{'label': segment, 'value': segment} for segment in queue_data['Segment']],
        value='A'
    ),
    dcc.Graph(id='queue-graph'),
    html.Div(id='optimization-results'),
])

@app.callback(
    Output('queue-graph', 'figure'),
    [Input('queue-selector', 'value')]
)
def update_graph(selected_segment):
    filtered_data = {key: [value[i] for i in range(len(queue_data['Segment'])) if queue_data['Segment'][i] == selected_segment] for key, value in queue_data.items()}
    fig = px.bar(
        filtered_data,
        x='Segment',
        y=['Arrival Rate', 'Service Rate'],
        title=f'Queue Analysis for Segment {selected_segment}'
    )
    return fig

@app.callback(
    Output('optimization-results', 'children'),
    [Input('queue-selector', 'value')]
)
def optimize_staffing(selected_segment):
    # Placeholder logic for staffing optimization
    required_staff = queue_data['Arrival Rate'][0] / queue_data['Service Rate'][0]  # Simplified logic
    return f'Required staff for {selected_segment}: {required_staff:.2f}'

if __name__ == '__main__':
    app.run(debug=True)