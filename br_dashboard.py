import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Slider for selecting the date range
start_year, end_year = st.slider('Select the Year Range', min(df['year']), max(df['year']), (min(df['year']), max(df['year'])))
start_month, end_month = st.slider('Select the Month Range', 1, 12, (1, 12))

# Filtering the dataframe based on the selected date range
df = df[(df['year'] >= start_year) & (df['year'] <= end_year) & 
        (df['month'] >= start_month) & (df['month'] <= end_month)]

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

# EDA Plots
def plot_categorical_distribution(data, column, title):
    fig, ax = plt.subplots(figsize=(10, 6))  # Create a new figure and axis object
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
    st.subheader(title_map[opt])
    plot_categorical_distribution(df, opt, title_map[opt])


# # Map visualization using Plotly
# # Map the accident types to numeric values
# unique_accident_types = df['accident_type'].unique()
# accident_type_mapping = {accident_type: index for index, accident_type in enumerate(unique_accident_types)}
# df['accident_type_numeric'] = df['accident_type'].map(accident_type_mapping)


# # Create a Mapbox scatter plot with markers colored based on mapped accident type values
# fig99 = go.Figure(go.Scattermapbox(
#         lat=df['latitude'],
#         lon=df['longitude'],
#         mode='markers',
#         marker=go.scattermapbox.Marker(
#             size=5,
#             color=df['accident_type_numeric'],
#             colorscale='Jet',
#             showscale=True,
#             colorbar=dict(tickvals=list(accident_type_mapping.values()), 
#                           ticktext=list(accident_type_mapping.keys()))
#         ),
#         text=df['city'] + '<br>' + df['accident_type'],
#     ))

# fig99.update_layout(
#     title='Accidents in Brazil Based on Latitude and Longitude (Colored by Accident Type)',
#     autosize=True,
#     hovermode='closest',
#     showlegend=False,
#     mapbox=go.layout.Mapbox(
#         accesstoken=None,
#         bearing=0,
#         center=go.layout.mapbox.Center(
#             lat=-10,
#             lon=-55
#         ),
#         pitch=0,
#         zoom=3,
#         style='open-street-map'
#     ),
# )

# st.plotly_chart(fig99)