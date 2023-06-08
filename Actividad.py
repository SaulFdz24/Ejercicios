import streamlit as st
#import numpy as np
import pandas as pd
#import plotly as px
#import plotly.figure_factury as ff
#from brokeh.plotting import figure
#import matplotlib.pyplot as plt

st.title('Police Incidents Reports from 2018 to 2020 in San Francisco')
df = pd.read_csv('Police_Department_Incident_Reports__2018_to_Present.csv')
st.dataframe(df)
st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa = pd.DataFrame()
mapa['Date']= df['Incident Date']
mapa['Day']= df['Incident Day of Week']
mapa['Police District']= df['Police District']
mapa['Neighborhood']= df['Analysis Neighborhood']
mapa['Incident Category']= df['Incident Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()
st.map(mapa.astype({'lat': 'float32', 'lon': 'float32'}))

subset_data2=mapa
police_district_input= st.sidebar.multiselect(
    'Police District',
    mapa.groupby('Police District').count().reset_index()['Police District'].tolist())
if len(police_district_input)>0:
    subset_data2=mapa[mapa['Police District'].isin(police_district_input)]
    

subset_data1=subset_data2
neighborhood_input= st.sidebar.multiselect(
    'Neighborhood',
    mapa.groupby('Neighborhood').count().reset_index()['Neighborhood'].tolist())
if len(neighborhood_input)>0:
    subset_data1=subset_data2[subset_data2['Neighborhood'].isin(neighborhood_input)]


subset_data=subset_data1
incident_input= st.sidebar.multiselect(
    'Incident Category',
    mapa.groupby('Incident Category').count().reset_index()['Incident Category'].tolist())
if len(incident_input)>0:
    subset_data=subset_data1[subset_data1['Incident Category'].isin(incident_input)]
    
subset_data

st.markdown('It is important to mention that any police district can answer to any incident, the neighborhood in which it happened is not related to the police district.')
st.markdown('Crime locations in San Francisco')
st.map(subset_data)
st.markdown('Crimes ocurred per day of the week')
st.bar_chart(subset_data['Day'].value_counts())