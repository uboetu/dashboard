import plotly.graph_objs as go
import pandas as pd

result_df = pd.read_csv('progress.csv')
# Separate all 'Known' points
known_data = result_df[result_df['status'] == 'Known']

# Sample 20k 'Known' points for plotting
sampled_known_data = known_data.sample(10000)

# Combine the sampled known and unknown data
plotting_df = pd.concat([sampled_known_data, result_df[result_df['status'] == 'Unknown']])

# Map the status to numeric values for coloring
color_map = {'Known': 0, 'Unknown': 1}
plotting_df['color'] = plotting_df['status'].map(color_map)

# Create a Mapbox scatter plot with markers colored based on status
fig99 = go.Figure(go.Scattermapbox(
        lat=plotting_df['latitude'],
        lon=plotting_df['longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=5,
            color=plotting_df['color'],
            colorscale='Viridis',
            showscale=True,
        ),
        text=plotting_df['status'] + '<br>BR: ' + plotting_df['br'].astype(str) + '<br>KM: ' + plotting_df['km'].astype(str)  # This will show 'Known' or 'Unknown' on hover
    ))

fig99.update_layout(
    title='Accidents in Brazil: Known vs Unknown Data',
    autosize=True,
    hovermode='closest',
    showlegend=False,
    mapbox=go.layout.Mapbox(
        accesstoken=None,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=-10,
            lon=-55
        ),
        pitch=0,
        zoom=3,
        style='open-street-map'
    ),
)

fig99.show()
