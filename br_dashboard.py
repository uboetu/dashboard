import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    data = pd.read_csv("Dados_PRF_2022_translated.csv", delimiter=';')
    return data

df = load_data()

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

# Voorbeeld: Staafdiagram van ongevalsoorzaken
plt.figure(figsize=(10, 6))
sns.countplot(x='accident_cause', data=df, order=df['accident_cause'].value_counts().index)
plt.xticks(rotation=90)
plt.xlabel('Oorzaak van het Ongeval')
plt.ylabel('Aantal Ongevallen')
plt.title('Staafdiagram van Ongevalsoorzaken')
plt.show()

# Add more visualizations and interactivity...
