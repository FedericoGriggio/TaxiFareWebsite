import streamlit as st
import pandas as pd
import numpy as np
import requests

'''
streamlit test 08/07/2022
'''

st.markdown('''
## 🤔 Do you really want to pay a Taxi ? Check the Taxi fare first!
''')

slat = float(st.text_input('Start Latitude', '40.73'))
slon = float(st.text_input('Start Longitude', '-73.93'))
elat = float(st.text_input('End Latitude', '40.73'))
elon = float(st.text_input('End Longitude', '-73.93'))
npass = int(st.text_input('Passengers number', '1'))

df = pd.DataFrame(columns=['lat', 'lon'])

dfstart = {'lat': float(slat), 'lon': float(slon)}
dfend = {'lat': float(elat), 'lon': float(elon)}

df = df.append(dfstart, ignore_index = True)
df = df.append(dfend, ignore_index = True)

params = {
  "pickup_datetime": "2013-07-06 17:18:00",
  "pickup_longitude": slat,
  "pickup_latitude": slon,
  "dropoff_longitude": elat,
  "dropoff_latitude": elon,
  "passenger_count": npass
}

response = requests.get('https://taxifare.lewagon.ai/predict',
                        params=params)

fare = response.json()['fare']

st.markdown(f'''
## Predicted Fare: {fare}
''')

st.map(df)
