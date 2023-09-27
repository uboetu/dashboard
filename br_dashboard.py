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
