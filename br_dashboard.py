import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


# Load the data
@st.cache
def load_data():
    data = pd.read_csv("Dados_PRF_2022_translated.csv", delimiter=';')
    return data

df = load_data()

df['longitude'] = df['longitude'].str.replace(',', '.').astype(float)
df['latitude'] = df['latitude'].str.replace(',', '.').astype(float)

# Title and introduction
st.title("Brazil Traffic Data Dashboard for 2022")
st.write("This dashboard provides insights into the traffic data of Brazil for the year 2022.")

# Data Overview
st.subheader('Data Overview')
st.write(f"Total Accidents: {len(df)}")
st.write(f"Total Deceased: {df['deceased'].sum()}")
st.write(f"Total Injured: {df['injured'].sum()}")

# Filtering
state = st.multiselect("Select State(s)", df['state'].unique())
if state:
    df = df[df['state'].isin(state)]

# Display raw data on request
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

# Visualizations
st.subheader('Number of Accidents per State')
fig, ax = plt.subplots()
df['state'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

st.subheader('Distribution of Accidents based on Accident Cause')
fig, ax = plt.subplots()
df['accident_cause'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

st.subheader('Distribution of Accidents based on Weekday')
fig, ax = plt.subplots()
df['weekday'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

# Map visualization using Plotly
# Map the accident types to numeric values
unique_accident_types = df['accident_type'].unique()
accident_type_mapping = {accident_type: index for index, accident_type in enumerate(unique_accident_types)}
df['accident_type_numeric'] = df['accident_type'].map(accident_type_mapping)

# Count the occurrences of each accident type
accident_type_counts = df['accident_type'].value_counts().reset_index()
accident_type_counts.columns = ['accident_type', 'count']

# Create a pie chart using Plotly
fig = px.pie(accident_type_counts, 
             names='accident_type', 
             values='count',
             title='Distribution of Accident Types')

# Show the pie chart in Streamlit
st.plotly_chart(fig)

# Create a Mapbox scatter plot with markers colored based on mapped accident type values
fig99 = go.Figure(go.Scattermapbox(
        lat=df['latitude'],
        lon=df['longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=5,
            color=df['accident_type_numeric'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(tickvals=list(accident_type_mapping.values()), 
                          ticktext=list(accident_type_mapping.keys()))
        ),
        text=df['city'] + '<br>' + df['accident_type'],
    ))

fig99.update_layout(
    title='Accidents in Brazil Based on Latitude and Longitude (Colored by Accident Type)',
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
