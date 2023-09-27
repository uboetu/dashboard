import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load the data
@st.cache(allow_output_mutation=True)  # reverted to use st.cache
def load_data():
    data = pd.read_csv("Dados_PRF_2022_translated.csv", delimiter=';')
    return data

# Make a copy of the DataFrame to avoid modifying the cached object
df = load_data().copy()

# Assuming the 'date' column is in 'YYYY-MM-DD' format
df['date'] = pd.to_datetime(df['date'])
df['week'] = df['date'].dt.strftime('%W')  # using %W to consider weeks starting from Monday

print(df['week'].unique()) 

# Week Slider
selected_week = st.slider('Select a week', 0, 52, 0, key='week_slider') # weeks from 0 to 52
# Filter data for the selected week and make a copy
print(type(df['week'].iloc[0]))  # print the data type of 'week' in df
print(type(str(selected_week).zfill(2)))
df_week = df[df['week'] == str(selected_week).zfill(2)]  # ensuring two-digit week number

# Title and introduction
st.title("Brazil Traffic Data Dashboard for 2022")
st.write("This dashboard provides insights into the traffic data of Brazil for the year 2022.")

# Map visualization using Plotly
unique_accident_types = df_week['accident_type'].unique()
accident_type_mapping = {accident_type: index for index, accident_type in enumerate(unique_accident_types)}
df_week['accident_type_numeric'] = df_week['accident_type'].map(accident_type_mapping)

fig99 = go.Figure(go.Scattermapbox(
        lat=df_week['latitude'],
        lon=df_week['longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=5,
            color=df_week['accident_type_numeric'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(tickvals=list(accident_type_mapping.values()), 
                          ticktext=list(accident_type_mapping.keys()))
        ),
        text=df_week['city'] + '<br>' + df_week['accident_type'],
    ))

fig99.update_layout(
    title=f'Accidents in Brazil for Week {selected_week} Based on Latitude and Longitude (Colored by Accident Type)',
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
        zoom=2,
        style='open-street-map'
    ),
)

st.plotly_chart(fig99)


# Print df_week to verify
# Print a random sample of 10 rows from the 'date' and 'week' columns
print(df[['date', 'week']].sample(25))
