import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

# Load the data
@st.cache
def load_data():
    data = pd.read_csv("Dados_PRF_2022_translated.csv", delimiter=';')
    return data

df = load_data()

# Assuming the 'date' column is in 'YYYY-MM-DD' format
df['date'] = pd.to_datetime(df['date'])
df['week'] = df['date'].dt.strftime('%U')

# Title and introduction
st.title("Brazil Traffic Data Dashboard for 2022")
st.write("This dashboard provides insights into the traffic data of Brazil for the year 2022.")

# Week Slider
selected_week = st.slider('Select a week', 0, 52, 0)  # weeks from 0 to 52
df_week = df[df['week'] == str(selected_week).zfill(2)]  # filter data for the selected week

# Play Button
if st.button('Play Animation'):
    for week in range(selected_week, 53):
        st.slider('Select a week', 0, 52, week)
        df_week = df[df['week'] == str(week).zfill(2)]
        time.sleep(1)  # sleep for 1 second before showing the next week
        st.experimental_rerun()  # rerun the script to update the slider and map

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
        zoom=3,
        style='open-street-map'
    ),
)

st.plotly_chart(fig99)
