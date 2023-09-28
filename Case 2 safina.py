#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[2]:


df = pd.read_csv('Dados_PRF_2022_translated.csv', delimiter=';')


# In[3]:


df


# In[11]:


Brazil_highway = 'highway'
new_df = df[['highway','accident_cause','accident_type']]


# In[12]:


new_df


# In[16]:


highway_counts = new_df['highway'].value_counts()
print(highway_counts)


# In[19]:


accident_cause_counts = new_df['accident_cause'].value_counts()
print(accident_cause_counts)


# In[46]:


accident_type_counts = new_df['accident_type'].value_counts()
print(accident_type_counts)


# In[74]:


time_column = df['time']
print(time_column)


# In[97]:


df['accident_cause_category'] = df['accident_cause'].map(cause_to_category)
print(df.head())


# In[116]:


cause_to_category = {
    'Driver alcohol consumption': 'Driver is to blame',
    'Late or inefficient driver reaction': 'Driver is to blame',
    'Incompatible speed': 'Driver is to blame',
    'Driving on the wrong side': 'Driver is to blame',
    'Lane change maneuver': 'Lane change maneuver',
    'Water accumulation on the pavement': 'Environmental events',
    'Animals on the road': 'Environmental events',
    'Slippery road': 'Environmental events',
    'Potholed road': 'Environmental events',
    'Accumulation of sand or debris on the pavement': 'Environmental events',
    'Pavement sinking or undulation': 'Environmental events',
    'Oil accumulation on the pavement': 'Environmental events',
    'Lack of shoulder': 'Environmental events',
    'Other natural phenomena': 'Environmental events',
    'Uneven road': 'Environmental events',
    'Steep decline': 'Environmental events',
    'Other roadway failures': 'Environmental events',
    'Uneven shoulder': 'Environmental events',
    'Lane change maneuvers': 'Traffic maneuvers',
    'Improper overtaking': 'Traffic maneuvers',
    'Disregarding intersection priority': 'Traffic maneuvers',
    'Entering the roadway without noticing other vehicles': 'Traffic maneuvers',
    'Forbidden conversion': 'Traffic maneuvers',
    'Entering the roadway without noticing other vehicles': 'Traffic maneuvers',
    'Driving on the wrong side': 'Traffic maneuvers',
    'Exit from carriageway': 'Traffic maneuvers',
    'Riding a motorcycle (or similar) between lanes': 'Traffic maneuvers',
    'Braking sharply': 'Traffic maneuvers',
    'Driving on the shoulder': 'Traffic maneuvers',
    'Forbidden U-turn': 'Traffic maneuvers',
    'Parking or stopping in a prohibited place': 'Traffic maneuvers',
    'Driving on the sidewalk': 'Traffic maneuvers',
    'Other mechanical or electrical failures': 'Improper or failed equipment',
    'Excessive and/or poorly stowed load': 'Improper or failed equipment',
    'Brake issue': 'Improper or failed equipment',
    'Covered signage': 'Improper or failed equipment',
    'Malfunctioning traffic light': 'Improper or failed equipment',
    'Damages and/or excessive tire wear': 'Improper or failed equipment',
    'Poor lighting': 'Improper or failed equipment',
    'Suspension problem': 'Improper or failed equipment',
    'Deficiency in the Lighting/Signaling System': 'Improper or failed equipment',
    'Failure to turn on motorcycle (or similar) headlights': 'Improper or failed equipment',
    'Forbidden modification': 'Improper or failed equipment',
    'Non-compliant speed reducer': 'Improper or failed equipment',
    'Misaligned headlights': 'Improper or failed equipment',
    'Inefficient drainage system': 'Improper or failed equipment',
    'Driving on the wrong side': 'Traffic situations',
    'Unexpected pedestrian entry': 'Traffic situations',
    'Pedestrian walking on the road': 'Traffic situations',
    'Restricted visibility on vertical curves': 'Traffic situations',
    'Restricted visibility on horizontal curves': 'Traffic situations',
    'Irregular access': 'Traffic situations',
    'Pedestrian crossing the road outside the crosswalk': 'Traffic situations',
    'Lack of signaling': 'Traffic situations',
    'Sharp curve': 'Traffic situations',
    'Road obstruction': 'Traffic situations',
    'Roadworks': 'Traffic situations',
    'Temporary detour': 'Traffic situations',
    'Static object on the carriageway': 'Traffic situations',
    'Pedestrian consumption of alcohol and/or psychoactive substances': 'Traffic situations',
    'Pedestrian consumption of alcohol or psychoactive substances': 'Traffic situations',
    'Urban area without an appropriate pedestrian crossing location': 'Traffic situations',
    'Lack of containment element preventing the exit from the carriageway': 'Traffic situations',
    'Poorly positioned signage': 'Traffic situations',
    'Traffic lanes with insufficient width': 'Traffic situations',
    'Fog': 'Weather conditions',
    'Rain': 'Weather conditions',
    'Smoke': 'Weather conditions'
}

category_df = pd.DataFrame(list(cause_to_category.items()), columns=['Accident Cause', 'Category'])

category_df.to_csv("accident_cause_categories.csv", index=False)

print(category_df)

combined_df = df.merge(category_df, on='', how='left')

print(combined_df)


combined_df.to_csv("combined_dataset.csv", index=False)  # Replace with your desired file name


# In[50]:


selected_highways = [316, 116, 163, 101, 40]
filtered_data = df[df['highway'].isin(selected_highways)]
grouped_data = filtered_data.groupby(['highway', 'accident_cause']).size().reset_index(name='count')
fig = px.bar(grouped_data, x='highway', y='count', color='accident_cause',
             title='Accident Causes by Highway',
             width=1200, height=600)

fig.show()


# In[111]:


cause_to_category = {
    'Driver alcohol consumption': 'Driver is to blame',
    'Late or inefficient driver reaction': 'Driver is to blame',
    'Incompatible speed': 'Driver is to blame',
    'Driving on the wrong side': 'Driver is to blame',
    'Lane change maneuver': 'Lane change maneuver',
    'Water accumulation on the pavement': 'Environmental events',
    'Animals on the road': 'Environmental events',
    'Slippery road': 'Environmental events',
    'Potholed road': 'Environmental events',
    'Accumulation of sand or debris on the pavement': 'Environmental events',
    'Pavement sinking or undulation': 'Environmental events',
    'Oil accumulation on the pavement': 'Environmental events',
    'Lack of shoulder': 'Environmental events',
    'Other natural phenomena': 'Environmental events',
    'Uneven road': 'Environmental events',
    'Steep decline': 'Environmental events',
    'Other roadway failures': 'Environmental events',
    'Uneven shoulder': 'Environmental events',
    'Lane change maneuvers': 'Traffic maneuvers',
    'Improper overtaking': 'Traffic maneuvers',
    'Disregarding intersection priority': 'Traffic maneuvers',
    'Entering the roadway without noticing other vehicles': 'Traffic maneuvers',
    'Forbidden conversion': 'Traffic maneuvers',
    'Entering the roadway without noticing other vehicles': 'Traffic maneuvers',
    'Driving on the wrong side': 'Traffic maneuvers',
    'Exit from carriageway': 'Traffic maneuvers',
    'Riding a motorcycle (or similar) between lanes': 'Traffic maneuvers',
    'Braking sharply': 'Traffic maneuvers',
    'Driving on the shoulder': 'Traffic maneuvers',
    'Forbidden U-turn': 'Traffic maneuvers',
    'Parking or stopping in a prohibited place': 'Traffic maneuvers',
    'Driving on the sidewalk': 'Traffic maneuvers',
    'Other mechanical or electrical failures': 'Improper or failed equipment',
    'Excessive and/or poorly stowed load': 'Improper or failed equipment',
    'Brake issue': 'Improper or failed equipment',
    'Covered signage': 'Improper or failed equipment',
    'Malfunctioning traffic light': 'Improper or failed equipment',
    'Damages and/or excessive tire wear': 'Improper or failed equipment',
    'Poor lighting': 'Improper or failed equipment',
    'Suspension problem': 'Improper or failed equipment',
    'Deficiency in the Lighting/Signaling System': 'Improper or failed equipment',
    'Failure to turn on motorcycle (or similar) headlights': 'Improper or failed equipment',
    'Forbidden modification': 'Improper or failed equipment',
    'Non-compliant speed reducer': 'Improper or failed equipment',
    'Misaligned headlights': 'Improper or failed equipment',
    'Inefficient drainage system': 'Improper or failed equipment',
    'Driving on the wrong side': 'Traffic situations',
    'Unexpected pedestrian entry': 'Traffic situations',
    'Pedestrian walking on the road': 'Traffic situations',
    'Restricted visibility on vertical curves': 'Traffic situations',
    'Restricted visibility on horizontal curves': 'Traffic situations',
    'Irregular access': 'Traffic situations',
    'Pedestrian crossing the road outside the crosswalk': 'Traffic situations',
    'Lack of signaling': 'Traffic situations',
    'Sharp curve': 'Traffic situations',
    'Road obstruction': 'Traffic situations',
    'Roadworks': 'Traffic situations',
    'Temporary detour': 'Traffic situations',
    'Static object on the carriageway': 'Traffic situations',
    'Pedestrian consumption of alcohol and/or psychoactive substances': 'Traffic situations',
    'Pedestrian consumption of alcohol or psychoactive substances': 'Traffic situations',
    'Urban area without an appropriate pedestrian crossing location': 'Traffic situations',
    'Lack of containment element preventing the exit from the carriageway': 'Traffic situations',
    'Poorly positioned signage': 'Traffic situations',
    'Traffic lanes with insufficient width': 'Traffic situations',
    'Fog': 'Weather conditions',
    'Rain': 'Weather conditions',
    'Smoke': 'Weather conditions'
}

selected_highways = [316, 116, 163, 101, 40]

filtered_data = df[df['highway'].isin(selected_highways)]

filtered_data['accident_cause_category'] = filtered_data['accident_cause'].map(cause_to_category)
grouped_data = filtered_data.groupby(['highway', 'accident_cause_category']).size().reset_index(name='count')

fig = px.bar(grouped_data, x='highway', y='count', color='accident_cause_category',
             title='Accident Causes by Highway',
             width=1200, height=600)

fig.show()


# In[72]:


grouped_data = df[['severely_injured', 'unharmed', 'unknown', 'injured']].sum().reset_index(name='count')
fig = px.pie(grouped_data, values='count', names=grouped_data.columns[0], hole=0.3,
             title='Distribution of Injury Types')
fig.update_traces(textinfo='percent+label')
fig.update_layout(annotations=[dict(text='Injury Types', x=0.5, y=0.5, font_size=13
                                , showarrow=False)])

fig.show()


# In[77]:


df['hour'] = pd.to_datetime(df['time']).dt.hour
hourly_counts = df['hour'].value_counts().sort_index().reset_index()
hourly_counts.columns = ['hour', 'count']

fig = px.line(hourly_counts, x='hour', y='count', 
              title='Accidents Over Time (by Hour)',
              labels={'hour': 'Hour of the Day', 'count': 'Accident Count'},
              width=1200, height=600)

fig.show()


# In[ ]:


cause_to_category = {
   
}


category_df = pd.DataFrame(list(cause_to_category.items()), columns=['Accident Cause', 'Category'])

# Save the DataFrame as a CSV file
category_df.to_csv("accident_cause_categories.csv", index=False)

# Display the DataFrame (optional)
print(category_df)


# In[81]:


accident_cause_counts = df_nieuw['accident_cause_cleaned'].value_counts().reset_index()
accident_cause_counts.columns = ['accident_cause_cleaned', 'count']

fig = px.pie(accident_cause_counts, 
             names='accident_cause_cleaned', 
             values='count',
             title='Distribution of Accident Causes')

fig.show()


# In[82]:


df['injury_category'] = 'Lightly Injured'
df.loc[df['severely_injured'] > 0, 'injury_category'] = 'Severely Injured'


injury_category_counts = df['injury_category'].value_counts().reset_index()
injury_category_counts.columns = ['injury_category', 'count']


fig = px.bar(
    injury_category_counts,
    x='injury_category',
    y='count',
    color='injury_category',
    title='Comparison of Lightly and Severely Injured',
    labels={'injury_category': 'Injury Category', 'count': 'Count'},
    category_orders={'injury_category': ['Lightly Injured', 'Severely Injured']},
)


fig.update_layout(xaxis_title='Injury Category', yaxis_title='Count')


fig.show()


# In[83]:


accident_type_counts = df['accident_type'].value_counts().reset_index()
accident_type_counts.columns = ['accident_type', 'count']

fig = px.pie(accident_type_counts, 
             names='accident_type', 
             values='count',
             title='Distribution of Accident Types')

fig.show()


# In[89]:


fig = px.scatter(
    df[df['severely_injured'] > 0],
    x='people',
    y='severely_injured',
    color='accident_type',
    title='Comparison of Severely Injured by Accident Type',
    labels={'people': 'Number of People', 'severely_injured': 'Number of Severely Injured'},
)


fig.update_layout(xaxis_title='Number of People', yaxis_title='Number of Severely Injured')

fig.show()


# In[84]:


plt.figure(figsize=(10, 6))
sns.countplot(x='accident_cause_cleaned', data=df_nieuw, order=df_nieuw['accident_cause_cleaned'].value_counts().index)
plt.xticks(rotation=60)
plt.xlabel('Accident cause')
plt.ylabel('Amount of Accidents')
plt.title('Bar Chart of Accident Causes')
plt.show()


# In[88]:


specific_causes = ['Late or inefficient driver reaction', 
                   'Lack of driver reaction',
                   'Driver alcohol consumption',
                   'Incompatible speed',
                   'Driver failed to maintain distance from the vehicle in front',
                   'Driver sleeping',
                   'Driving on the wrong side', 
                   'Driver sudden illness',
                   'Driver disrespected the red traffic light',
                   'Driver using cellphone',
                   'Driver consumption of psychoactive substances',
                   'Engaging in street racing']

filtered_df_driverstoblame = df[df['accident_cause'].isin(specific_causes)]

plt.figure(figsize=(12, 8))  
plt.hist(filtered_df_driverstoblame['accident_cause'], bins=len(specific_causes), edgecolor='k', alpha=0.7)
plt.xlabel('Causes')
plt.ylabel('Amount of Accidents')
plt.title('Histogram of Specific Causes (Drivers to Blame)')
plt.xticks(rotation=80)
plt.grid(axis='y', linestyle='-', alpha=0.7)  
plt.tight_layout()
plt.show()


# In[92]:


cross_table = pd.crosstab(df['accident_cause_cleaned'], df['accident_type'])

cross_table = cross_table.reset_index()

fig = px.bar(cross_table, x='accident_cause_cleaned', y=cross_table.columns[1:], title='Influence of Causes on Types of Accidents')

fig.update_layout(
    xaxis_title='Causes',
    yaxis_title='Amount of Accidents',
    xaxis=dict(categoryorder='total ascending'),  
    width=1000,  
    height=700)  
fig.update_xaxes(categoryorder='total ascending')  
fig.update_layout(legend_title_text="Type of Accidents")

fig.show()

