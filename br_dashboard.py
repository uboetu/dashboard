import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go


# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('Dados_PRF_2022.csv', delimiter=';', encoding='latin1')
    return data

# Load the data
df = load_data()

# Convert the 'date' column to datetime, coerce errors
# Attempt to convert the 'date' column to datetime and extract the year
try:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year
except KeyError:
    st.warning("Date column not found in the DataFrame. Skipping date conversion and year extraction.")
    
# Title of the dashboard
st.title("Accident Data Brazil Dashboard")

st.markdown(
    """
    ### About the Original Untranslated Dataset
    The original, untranslated datasets were sourced from Kaggle, from a collection of Police Traffic Incidents 
    datasets provided by the user tgomesjuliana. We opted for this particular dataset because of its substantial 
    file size compared to others, offering a more extensive and comprehensive dataset for analysis.
    You can access the original datasets [here](https://www.kaggle.com/datasets/tgomesjuliana/police-traffic-incidents).
    """
)    

st.subheader("Original Dataset Information")
st.write("Delimiter used: ;")
st.write("Encoding used: latin1")

# Displaying columns in a more horizontal way
st.write("Columns in the dataset:")
columns = df.columns.tolist()
col1, col2, col3 = st.columns(3)  # create three columns
for i in range(0, len(columns), 3):
    col1.write(f"{i}: `{columns[i]}`")
    if i + 1 < len(columns):
        col2.write(f"{i + 1}: `{columns[i + 1]}`")
    if i + 2 < len(columns):
        col3.write(f"{i + 2}: `{columns[i + 2]}`")

st.write("Sample data from the original dataset:")
st.write(df.head())

dataset_paths = {
    '2017': 'Dados_PRF_2017_translated.csv',
    '2018': 'Dados_PRF_2018_translated.csv',
    '2019': 'Dados_PRF_2019_translated.csv',
    '2020': 'Dados_PRF_2020_translated.csv',
    '2021': 'Dados_PRF_2021_translated.csv',
    '2022': 'Dados_PRF_2022_translated.csv',
}

def load_data(year):
    data = pd.read_csv(dataset_paths[year], delimiter=';', encoding='latin1')
    # Attempt to convert the 'date' column to datetime
    try:
        data['date'] = pd.to_datetime(data['date'], errors='coerce')
        if data['date'].isnull().all():
            raise Exception("Date conversion failed.")
    except Exception as e:
        st.warning(f"Error processing date column: {e}. Skipping date conversion.")
    return data

st.markdown(
    """
    ## Translation of Dataset
    The datasets used in this dashboard were originally in Portuguese. 
    We have translated all the data to English to make the analysis more accessible to a global audience. 
    The translation was done using a custom script, which can be found at the following GitHub link:
    [Translation Script](https://github.com/uboetu/dashboard/blob/main/br_traffic_v2_translated_adaptable_modified.py)
    """
)

# Title of the dashboard
st.title("Accident Data Brazil 2017-2022")


# Selector for year
selected_year = st.sidebar.selectbox("Choose a Year", list(dataset_paths.keys()))
df = load_data(selected_year)

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# Displaying the year and the first few rows of the selected dataset
st.write(f"Selected Dataset Year: {selected_year}")
st.write("Sample data from the selected dataset:")
st.write(df.head())

# Display basic information about the dataset
st.write("### Dataset Information:")
st.write(f"Number of Rows: {df.shape[0]}")
st.write(f"Number of Columns: {df.shape[1]}")
st.write("Translated column names in the dataset:")
columns = df.columns.tolist()
col1, col2, col3 = st.columns(3)  # create three columns
for i in range(0, len(columns), 3):
    col1.write(f"{i}: `{columns[i]}`")
    if i + 1 < len(columns):
        col2.write(f"{i + 1}: `{columns[i + 1]}`")
    if i + 2 < len(columns):
        col3.write(f"{i + 2}: `{columns[i + 2]}`")

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataframe df here

# Your line plot code
df['hour'] = pd.to_datetime(df['datetime']).dt.hour
hourly_counts = df['hour'].value_counts().sort_index().reset_index()
hourly_counts.columns = ['hour', 'count']
fig_line = px.line(hourly_counts, x='hour', y='count', 
                   title='Accidents Over Time (by Hour)',
                   labels={'hour': 'Hour of the Day', 'count': 'Accident Count'},
                   width=400, height=300)

# EDA Plots
def plot_categorical_distribution(data, column, title):
    fig, ax = plt.subplots(figsize=(5, 3))  # Create a new figure and axis object
    sns.countplot(y=data[column], order=data[column].value_counts().index, palette='viridis', ax=ax)
    ax.set_title(title, fontsize=15)
    ax.set_ylabel('')
    st.pyplot(fig)  # Pass the figure object to st.pyplot()
    plt.clf()  # Clear the current figure


# Sidebar options for EDA
st.sidebar.header("EDA Options")
plot_options = st.sidebar.multiselect(
    "Select the features to plot", 
    ('weekday', 'accident_cause', 'accident_type', 'accident_classification', 'time_of_day', 'weather_condition', 'type_of_road', 'road_layout', 'urban_rural'), 
    ('weekday', 'accident_cause')
)

# Plotting the selected options
for opt in plot_options:
    title_map = {
        'weekday': 'Distribution of Accidents by Weekday',
        'accident_cause': 'Distribution of Accidents by Cause',
        'accident_type': 'Distribution of Accidents by Type',
        'accident_classification': 'Distribution of Accidents by Classification',
        'time_of_day': 'Distribution of Accidents by Time of the Day',
        'weather_condition': 'Distribution of Accidents by Weather Condition',
        'type_of_road': 'Distribution of Accidents by Type of Road',
        'road_layout': 'Distribution of Accidents by Road Layout',
        'urban_rural': 'Distribution of Accidents by Urban/Rural'
    }
    
    if opt == 'time_of_day':
        col1, col2 = st.columns(2)  # use st.columns() instead of st.beta_columns()
        with col1:
            st.subheader(title_map[opt])
            plot_categorical_distribution(df, opt, title_map[opt])
        with col2:
            st.plotly_chart(fig_line)
    else:
        st.subheader(title_map[opt])
        plot_categorical_distribution(df, opt, title_map[opt])



# Map visualization using Plotly
# Map the accident types to numeric values
unique_accident_types = df['accident_type'].unique()
accident_type_mapping = {accident_type: index for index, accident_type in enumerate(unique_accident_types)}
df['accident_type_numeric'] = df['accident_type'].map(accident_type_mapping)

# Ensure the 'date' column is datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Calculate the week number
df['week_number'] = df['date'].dt.isocalendar().week



grouped_data = df[['severely_injured', 'unharmed', 'unknown', 'injured']].sum().reset_index(name='count')
fig1 = px.pie(grouped_data, values='count', names=grouped_data.columns[0], hole=0.3,
              title='Distribution of Injury Types')
fig1.update_traces(textinfo='percent+label')
fig1.update_layout(annotations=[dict(text='Injury Types', x=0.5, y=0.5, font_size=13, showarrow=False)])

accident_type_counts = df['accident_type'].value_counts().reset_index()
accident_type_counts.columns = ['accident_type', 'count']
fig2 = px.pie(accident_type_counts, 
              names='accident_type', 
              values='count',
              title='Distribution of Accident Types')

fig1_html = fig1.to_html(full_html=False)
fig2_html = fig2.to_html(full_html=False)

# Using html to create side-by-side divs
html_code = f"""
    <div style="display: flex;">
        <div style="flex: 50%;">
            <iframe src="about:blank" id="fig1" style="border:none;width:100%;height:400px;"></iframe>
        </div>
        <div style="flex: 50%;">
            <iframe src="about:blank" id="fig2" style="border:none;width:100%;height:400px;"></iframe>
        </div>
    </div>
    <script>
        var fig1 = document.getElementById('fig1');
        var fig2 = document.getElementById('fig2');
        fig1.srcdoc = `{fig1_html}`;
        fig2.srcdoc = `{fig2_html}`;
    </script>
"""

components.v1.html(html_code, width=1000, height=500, scrolling=False)
























# Map accident types to numeric values before filtering the dataframe
unique_accident_types = df['accident_type'].unique()
accident_type_mapping = {accident_type: index for index, accident_type in enumerate(unique_accident_types)}
df['accident_type_numeric'] = df['accident_type'].map(accident_type_mapping)

# Slider for selecting the week number
selected_week = st.slider('Select the Week Number', 1, 52, 1)

# Filtering the dataframe based on the selected week number
df_week = df[df['week_number'] == selected_week]

df_week = df_week[(df_week['latitude'] >= -33) & (df_week['latitude'] <= 5) & 
                  (df_week['longitude'] >= -74) & (df_week['longitude'] <= -34)]

fig99 = go.Figure(go.Scattermapbox(
        lat=df_week['latitude'],
        lon=df_week['longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=5,
            color=df_week['accident_type_numeric'],
            colorscale='Jet',
            showscale=True,
            colorbar=dict(tickvals=list(accident_type_mapping.values()), 
                          ticktext=list(accident_type_mapping.keys()))
        ),
        text=df_week['city'] + '<br>' + df_week['accident_type'],
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
        zoom=2,
        style='open-street-map'
    ),
)

st.plotly_chart(fig99)