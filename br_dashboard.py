import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('Dados_PRF_2022.csv', delimiter=';', encoding='latin1')
    return data

df = load_data()

# Title of the dashboard
st.title("Accident Data Dashboard")

# Selectors for different types of analyses
analysis = st.sidebar.selectbox("Choose an Analysis Type", 
                                ["Original Dataset Info", "Time Analysis", "Location Analysis", 
                                 "Accident Details", "Weather and Road Conditions", "Outcome Analysis"])

# Depending on the selected analysis, display the corresponding visualization
if analysis == "Original Dataset Info":
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
    return data

# Title of the dashboard
st.title("Accident Data Dashboard")

# Selector for year
selected_year = st.sidebar.selectbox("Choose a Year", list(dataset_paths.keys()))
df = load_data(selected_year)

# Displaying the year and the first few rows of the selected dataset
st.write(f"Selected Dataset Year: {selected_year}")
st.write("Sample data from the selected dataset:")
st.write(df.head())


### EDA hier ###