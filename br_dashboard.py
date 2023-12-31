import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px



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
    pass
    
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

def plot_missing_values(df):
    # Find missing values in the dataset
    missing_values = df.isnull()
    
    # Plotting the heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(missing_values, cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap')

    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.tick_params(axis='both', which='minor', labelsize=6)
    
    # Show the plot in Streamlit
    st.pyplot(plt.gcf())  # Use st.pyplot() to display the plot

st.write("Missing Values Heatmap")
plot_missing_values(df)

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
    ## Dataset processing
    To enhance global accessibility and comprehension, the datasets employed in this dashboard, originally in Portuguese, have been meticulously translated to English. 
    This extensive translation process involved various steps including the conversion of coordinates, translation of specific column values, and the transformation of date and time fields to datetime objects. 
    This ensures not only language translation but also the usability of the dataset for further analysis and processing.

    The translation, ensuring the seamless understanding of the analysis, was executed using a specialized script. This script also automates the processing of traffic accident data, enhancing ease of analysis across various years.
    
    For a deeper insight into the translation process or to access the script, kindly refer to the following GitHub link: 
    [Data Processing Script](https://github.com/uboetu/dashboard/blob/main/br_traffic_data_processing.py)
    """
)


# Check if the checkbox is checked
if st.checkbox("Provide enhanced insight into data processing"):
    # Display the documentation in markdown format when checkbox is checked
    st.markdown("""
    # Brazilian Traffic Data Processing Script

    This script processes and translates Brazilian traffic accident data from 2017 to 2023.

    ## Overview

    - **Main Task**: Processes and translates traffic accident data.
    - **Input**: CSV files named 'Dados_PRF_{year}.csv'.
    - **Output**: New CSV files with processed and translated data, named 'Dados_PRF_{year}_translated.csv'.

    ## Functions

    1. **`convert_coords(df)`**:
    - **Task**: Converts longitude and latitude from string to float.
    - **Input**: DataFrame `df`.
    - **Output**: Modified DataFrame.

    2. **`translate_dataframe(df, translation_dict)`**:
    - **Task**: Translates DataFrame column names.
    - **Input**: DataFrame `df`, Translation dictionary `translation_dict`.
    - **Output**: DataFrame with translated column names.

    3. **`translate_values(df, translations)`**:
    - **Task**: Translates specific values within DataFrame columns.
    - **Input**: DataFrame `df`, Translations dictionary `translations`.
    - **Output**: DataFrame with translated values.

    4. **`convert_datetime(df)`**:
    - **Task**: Converts date and time columns to datetime objects.
    - **Input**: DataFrame `df`.
    - **Output**: Modified DataFrame with datetime objects.

    ## Workflow

    - **Step 1**: Load a CSV file for each year from 2017 to 2023.
    - **Step 2**: Remove duplicate rows from the DataFrame.
    - **Step 3**: Use `translate_dataframe` to translate column names.
    - **Step 4**: Use `convert_coords` to convert coordinates.
    - **Step 5**: Use `convert_datetime` to convert date and time columns to datetime objects.
    - **Step 6**: Use `translate_values` to translate specific values within columns.
    - **Step 7**: Save the processed DataFrame as a new CSV file in the same directory.
    - **Error Handling**: If a file for a specific year is not found, print a message and continue to the next year.

    ## Conclusion

    The script automates the processing and translation of traffic accident data, making it easier to analyze and understand the data across various years.
    """)

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


st.write("Missing Values Heatmap")
st.markdown(
"""
The heatmap below gives a clear view of the missing data inside the dataset. As we can see there are only a couple missing in the ‘highway’ and ‘kilometer’ column, which are colored yellow in the heatmap.
""")
plot_missing_values(df)


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

container1 = st.container()
container2 = st.container()
st.markdown(
"""
The pie chart below shows that most drivers come out unharmed and only a small percentage are severely injured.
""")   

with container1:
    st.plotly_chart(fig1)

with container2:
    st.plotly_chart(fig2)

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

st.markdown(
"""
The map below gives a clear insight into where accidents occur in Brazil. With the slider above you can change the week its shows on the map. 
The different accident types each have a different color that can be found in the legend.
""")   
st.plotly_chart(fig99)

agg_data = df.groupby(['state', 'accident_type']).size().unstack(fill_value=0)

# Creating the plot
fig, ax = plt.subplots(figsize=(12, 6))
agg_data.plot(kind='bar', stacked=True, ax=ax)
ax.set_xlabel('State')
ax.set_ylabel('Count')
ax.set_title('Total Count of Accident Types by State')
ax.legend(title='Accident Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=90)

# Display the plot in Streamlit
st.markdown(
"""
In the bar chart below we can see the amount of accidents per state in Brazil, we can also see the types of accidents and how often the occur per state. 
It is clear to see that the state Minas Gerais (MG) is the state with the most accidents. Following this state are Parana (PR) and Santa Catarina (SC), All three of these states are in the bottom right part of the country.
""")   
st.pyplot(fig)

grouped_data = df.groupby(['highway', 'accident_cause_category']).size().reset_index(name='count')

# Summing counts for each highway and getting top 10 highways with most accidents
top_highways = grouped_data.groupby('highway')['count'].sum().nlargest(10).index.tolist()

# Filtering grouped_data for only top 10 highways
grouped_data = grouped_data[grouped_data['highway'].isin(top_highways)]

# Create the bar plot
fig = px.bar(grouped_data, x='highway', y='count', color='accident_cause_category',
             title='Accident Causes by Highway (Top 10 Highways)',
             width=900, height=450)


# Display the plot in Streamlit
st.markdown(
"""
In the bar chart below we can find the count of accidents and the types of accidents for the ten highways with the most accidents.
In Brazil the highways are named with numbers. For example, we can see that highway 101 has the most accidents with ‘Driver error’ as the most common accident type.
""") 
st.plotly_chart(fig)

accident_counts = df['accident_type'].value_counts()

# Create a DataFrame for the pie chart
df_pie = pd.DataFrame({'accident_type': accident_counts.index, 'count': accident_counts.values})

# Create the pie chart
fig = px.pie(df_pie, values='count', names='accident_type', hole=0.3, title='Accidents types for drivers to blame')
fig.update_traces(textinfo='percent+label')

# Update layout
fig.update_layout(
    annotations=[dict(text='Accident Type', x=0.5, y=0.5, font_size=13, showarrow=False)],
    width=750, 
    height=600
)
st.markdown(
"""
This pie charts shows the accidents types for only drivers to blame, which was the main cause of the accident types. This chart is a combination of the ‘Distribution of accident Types’ and ‘Distribution of accidents by cause’ combined focused on only drivers to blame. 
""")   
# Show the pie chart in Streamlit
st.plotly_chart(fig)



plt.figure(figsize=(10, 6))
sns.countplot(x='accident_cause_category', data=df, order=df['accident_cause_category'].value_counts().index)

# Update the x-axis labels and rotate them
plt.xticks(rotation=60)

# Update the labels and title to be in English
plt.xlabel('Cause of the Accident')
plt.ylabel('Number of Accidents')
plt.title('Bar Chart of Accident Causes')

st.markdown(
"""
This pie charts shows the accidents types for only drivers to blame, which was the main cause of the accident types. This chart is a combination of the ‘Distribution of accident Types’ and ‘Distribution of accidents by cause’ combined focused on only drivers to blame.
""")  
# Display the plot in Streamlit
st.pyplot(plt.gcf())