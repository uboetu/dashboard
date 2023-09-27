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
    st.write("Columns in the dataset:")
    st.write(list(df.columns))
    st.write("Sample data from the original dataset:")
    st.write(df.head())

elif analysis == "Time Analysis":
    # Accidents by day of the week
    st.subheader("Accidents by Day of the Week")
    fig, ax = plt.subplots()
    sns.countplot(data=df, y='dia_semana', ax=ax, order=df['dia_semana'].value_counts().index)
    st.pyplot(fig)
    
    # Accidents by time of the day
    st.subheader("Accidents by Time of the Day")
    df['horario'] = pd.to_datetime(df['horario'])
    df['hour'] = df['horario'].dt.hour
    fig, ax = plt.subplots()
    sns.histplot(data=df, x='hour', bins=24, ax=ax)
    st.pyplot(fig)

elif analysis == "Location Analysis":
    # Accidents by federal unit
    st.subheader("Accidents by Federal Unit")
    fig, ax = plt.subplots()
    sns.countplot(data=df, y='uf', ax=ax, order=df['uf'].value_counts().index)
    st.pyplot(fig)

elif analysis == "Accident Details":
    # Distribution of the cause of accident
    st.subheader("Distribution of Cause of Accident")
    fig, ax = plt.subplots()
    sns.countplot(data=df, y='causa_acidente', ax=ax, order=df['causa_acidente'].value_counts().index)
    st.pyplot(fig)


