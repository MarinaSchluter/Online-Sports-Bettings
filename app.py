# --------------------LIBRARIES----------------------------#

import streamlit as st
import pandas as pd
import base64
import plotly.express as px


import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import joblib


# -----------------SITE CONFIGURATION----------------#

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(
    page_title="Online Sports Betting",
    page_icon="⚽🏀🎾",
    layout="wide", #centered, wire
    initial_sidebar_state="expanded" #auto, collapsed, expanded
)

#-------------------BACKGROUND IMAGE----------------------#

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file, horizontal_offset=0, vertical_offset=0):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .main {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-attachment: local;
        background-position: {horizontal_offset}px {vertical_offset}px; /* Ajustes horizontal y vertical */
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('Images/footballstadiumtransparent.png', horizontal_offset=100, vertical_offset=50)  # Ajuste horizontal de 100 píxeles y ajuste vertical de 50 píxeles

# ---------------------DATAFRAMES-----------------------------#

mysportsbetting=pd.read_csv("Data\mysportsbetting.csv")
online_betting_houses=pd.read_csv("Data\online_betting_houses.csv")

# ---------------------HEADER & LOGO-----------------------------#

logo="Images/runningreduced.png"     
st.image(logo, width=60)
st.title("Online Sports Betting")

# --------------------SIDEBAR FILTERS------------------------------#

# st.sidebar.title("Filters")
# st.sidebar.write("-------------")

#-----TABS------#
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Context","Events Distribution","Wager vs Win","PowerBi","Prediction"])

#-----TAB 1 (CONTEXT)------#

with tab1:
    st.markdown("- Ranking of the 44 Spanish Online Betting Houses in April 2024")
   
   
    min_rating = online_betting_houses["Rating"].min()
    max_rating = online_betting_houses["Rating"].max()
    selected_min_rating, selected_max_rating = st.slider("Select Rating Range", min_value=min_rating, 
                                                         max_value=max_rating, value=(min_rating, max_rating), step=0.1)
    
    filtered_df = online_betting_houses[(online_betting_houses["Rating"] >= selected_min_rating) & (online_betting_houses["Rating"] <= selected_max_rating)]
    
    fig = px.bar(filtered_df, x="Rating", y="Name", text_auto=True, color="Name", width=1500, height=1000)
    st.plotly_chart(fig)
    
    st.markdown("- Information source: https://www.casasdeapuestas.com/")

#-----TAB 2 (EVENTS DISTRIBUTION)------#

#-----TAB 3 (WAGER VS WIN)------#

#-----TAB 4 (POWERBI)------#

with tab4:
    power_bi_url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiZTIyMjcxNjktZGExMS00MDljLWJmMjYtYzFiZDMzMmZhMDZiIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9&pageName=ReportSection"
    iframe_width = 2500
    iframe_height = 800

    st.markdown(f'<iframe src="{power_bi_url}" width={iframe_width} height={iframe_height} style="position:absolute; left:-300px;"></iframe>', unsafe_allow_html=True)

#-----TAB 5 (PREDICTION)------#

with tab5:
# API_KEY = 'ZafUdLi6NvawUl62GVALTCKe8AluIo7F'
# URL = 'https://machinelearningarea-cbbjm.francecentral.inference.ml.azure.com/score'

    st.title("Profit Prediction by Wager, Sport Group & Purchase Time")


# minimum_capacity = st.number_input("Número de personas:", min_value=1, value=1)
# bedrooms = st.number_input("Número de habitaciones:", min_value=1, value=1)
# bathrooms = st.number_input("Número de baños:", min_value=1, value=1)
# bathroom_type = st.selectbox("Baño compartido:", SHARED_BATHROOMS_OPTIONS)
# ratings = st.number_input("Valoración:", min_value=1, value=1)
# ratings = st.selectbox("Valoración:", list(range(1,5)),index=0)

# if st.button("Realizar predicción"):
#     # Estructura de datos para la solicitud POST
#     data = {
#         "input_data": {
#         "columns": [
#         "neighbourhood_group",
#         "room_type",
#         "accommodates",
#         "bedrooms"
#             ],
#             "index": [0],
#             "data": [[neighbourhood_group,room_type,minimum_capacity,bedrooms]]
#         }
#     }

#     # Convertir a JSON
#     body = str.encode(json.dumps(data))

#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': ('Bearer ' + API_KEY)
#     }

#     # Crear y enviar la solicitud POST
#     try:
#         req = urllib.request.Request(URL, body, headers)
#         with urllib.request.urlopen(req) as response:
#             result = json.loads(response.read())
#             predicted_price = round(result[0], 2)
#             st.write("Precio predicho:")
#             st.markdown(f"### Precio predicho: **${predicted_price}**")
            
#     except urllib.error.HTTPError as error:
#         st.error(f"Error en la solicitud: {error.code}")
#         st.write(error.info())
#         st.write(error.read().decode("utf8", 'ignore'))