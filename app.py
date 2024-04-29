# --------------------LIBRARIES----------------------------#

import streamlit as st
import pandas as pd
import base64
import plotly.express as px
import urllib.request
import json
import ssl
import locale


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

online_betting_houses=pd.read_csv("Data/online_betting_houses.csv")
mysportsbetting=pd.read_csv("Data/mysportsbetting.csv")
mysportsbetting_filtered=pd.read_csv("Data/mysportsbetting_filtered.csv")
sports_regression=pd.read_csv("Data/sports_regression.csv")

# ---------------------HEADER & LOGO-----------------------------#

logo="Images/runningreduced.png"     
st.image(logo, width=60)
st.title("Online Sports Betting")

# --------------------SIDEBAR FILTERS------------------------------#

# st.sidebar.title("Filters")
# st.sidebar.write("-------------")

#-----TABS------#
tab1, tab2, tab3, tab4, tab5,tab6 = st.tabs(["Online Sport Betting Houses in Spain","Events Distribution","Wager vs Win","Hold","PowerBI","Prediction"])

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

with tab2:
        
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        SPORT_G_OPTIONS=sorted(mysportsbetting["Sport_Group"].unique())
        sportg= st.multiselect("Select Sport Group:",SPORT_G_OPTIONS)
        if sportg:
            mysportsbetting=mysportsbetting[mysportsbetting["Sport_Group"].isin(sportg)]
    with col2:
        PURCHASE_T_OPTIONS=["Prematch","Live"]
        purchase = st.multiselect("Select Purchase Time:", PURCHASE_T_OPTIONS)
        if purchase:
            mysportsbetting=mysportsbetting[mysportsbetting["Purchase_Time"].isin(purchase)]
    with col3:
        GENDER_OPTIONS=sorted(mysportsbetting["Gender_Competition"].unique())
        gender= st.multiselect("Select Gender:",GENDER_OPTIONS)
        if gender:
            mysportsbetting=mysportsbetting[mysportsbetting["Gender_Competition"].isin(gender)]
    with col4:
        MONTH_OPTIONS=["January","February","March"]
        month= st.multiselect("Select Month:",MONTH_OPTIONS)
        if month:
            mysportsbetting=mysportsbetting[mysportsbetting["Month_Name"].isin(month)]
    with col5:
        WEEKDAY_OPTIONS=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        weekday = st.multiselect("Select Weekday:", WEEKDAY_OPTIONS)
        if weekday:
            mysportsbetting=mysportsbetting[mysportsbetting["Day_of_Week_Name"].isin(weekday)]
            
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        COMPETION_OPTIONS=sorted(mysportsbetting["Competition"].unique())
        sportg= st.multiselect("Select Competition:",COMPETION_OPTIONS)
        if sportg:
            mysportsbetting=mysportsbetting[mysportsbetting["Competition"].isin(sportg)]
    with col2:
        EVENT_OPTIONS=sorted(mysportsbetting["Event"].unique())
        purchase = st.multiselect("Select Event:", EVENT_OPTIONS)
        if purchase:
            mysportsbetting=mysportsbetting[mysportsbetting["Event"].isin(purchase)]   
    with col3:
        st.markdown("")
    with col4:
        st.markdown("")
    with col5:
        st.markdown("")
   
             
    total_events = len(mysportsbetting)
    total_events_formatted = locale.format_string("%d", total_events, grouping=True)
    # total_events_by_filters= mysportsbetting["Event"].nunique()
    # total_events_by_filters_formatted = locale.format_string("%d", total_events_by_filters, grouping=True)
        
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.markdown(f"**Total Events: {total_events_formatted}**")
    with col2:
        st.markdown(f"")
    with col3:
        st.markdown(f"")
    with col4:
        st.markdown(f"")
    with col5:
        st.markdown(f"")
        
    color_map_sport_group = {                                        #Create a color map representative of each Sport_Group for quick association and visualisation of elements
    "Football": "darkgreen",
    "Basketball": "red",
    "Greyhound Racing": "lightgrey",
    "Horse Racing": "burlywood",
    "Tennis": "lime",
    "Other": "lightblue"  
}
    color_map_sports = {
    "Basketball": "red",
    "Handball": "darkblue",
    "Bandy": "dimgray",
    "Baseball": "saddlebrown",
    "Boxing": "gold",
    "Horse Racing": "burlywood",
    "Cycling": "royalblue",
    "Cricket": "darkgreen",
    "Darts": "darkred",
    "Winter Sports": "lightblue",
    "Formula 1": "firebrick",
    "Football": "darkgreen",
    "American Football": "darkslategray",
    "Indoor Football": "green",
    "Greyhound Racing": "lightgrey",
    "Golf": "limegreen",
    "Ice Hockey": "lightsteelblue",
    "Lotto": "gold",
    "MMA": "darkslategray",
    "Padel": "midnightblue",
    "Rugby Union": "royalblue",
    "Snooker": "mediumseagreen",
    "Squash": "darkorange",
    "Tennis": "lime",
    "Table Tennis": "skyblue",
    "Volleyball": "lightcoral",
    "Beach Volleyball": "lightyellow",
    "Waterpolo": "dodgerblue"
}
    competitions_by_date = mysportsbetting.groupby("Event_Date")["Competition"].count().reset_index()
    fig = px.line(competitions_by_date, x="Event_Date", y="Competition", title="Total Competitions by Event Date",width=1750,height=300 )
    fig.update_xaxes(title="Date")
    fig.update_yaxes(title="Number of Events")
    st.plotly_chart(fig)
    
    
    # tree_data = mysportsbetting.groupby(["Sport_Group","Sport","Competition","Event"]).size().reset_index(name="count")
    # fig = px.treemap(tree_data, path=["Sport_Group","Sport","Competition","Event"], 
    #               values="count", title="Data hierarchy", color="Sport_Group", 
    #               color_discrete_map=color_map_sport_group, width=1750,height=600)
    # st.plotly_chart(fig)
    hierarchy="Images\data_hierarchy.png"
    st.image(hierarchy)
    
    
    col1,col2=st.columns(2)
    with col1:
            fig=px.histogram(mysportsbetting, x="Sport_Group", title="Event Distribution by Sport Group", 
                             color="Sport_Group",color_discrete_map=color_map_sport_group,text_auto=True,
                             category_orders={"Sport_Group": mysportsbetting["Sport_Group"].value_counts().index},height=300)
            fig.update_xaxes(title="Sport Group")
            fig.update_yaxes(title="Number of Events")
            st.plotly_chart(fig)
    with col2:
        other_sports=mysportsbetting[mysportsbetting["Sport_Group"]=="Other"]
        fig=px.histogram(other_sports, x="Sport", title="Other Sports Event Distribution", color="Sport",
                 color_discrete_map=color_map_sports,text_auto=True,
                 category_orders={"Sport": mysportsbetting["Sport"].value_counts().index},height=300)
        fig.update_xaxes(title="Sport")
        fig.update_yaxes(title="Number of Events")
        st.plotly_chart(fig)   
        
    col1,col2=st.columns([3,3])    
    color_map_purchase_time = {                                 #Create a color map different from the ones already used in Sports and Sport_Group
    "Live": "gold",
    "Prematch": "mediumpurple"
}
    color_map_gender = {
    'Male': 'cornflowerblue',
    'Female': 'lightpink',
    'Not Applicable': 'lightgrey'
}
    with col1:
        fig=px.histogram(mysportsbetting, x="Purchase_Time", title="Events Distribution by Purchase Time",
                    color="Purchase_Time",color_discrete_map=color_map_purchase_time,text_auto=True,height=300)
        fig.update_xaxes(title="Purchase Time")
        fig.update_yaxes(title="Number of Events")
        st.plotly_chart(fig)  
    with col2:
        fig=px.histogram(mysportsbetting, x="Gender_Competition", title="Events Distribution by Gender",
                 color="Gender_Competition",color_discrete_map=color_map_gender,text_auto=True,height=300)
        fig.update_xaxes(title="Gender")
        fig.update_yaxes(title="Number of Events")
        st.plotly_chart(fig)  
    col1,col2=st.columns([3,3])
    with col1:
        ordered_month_names = ["January", "February", "March"]
        fig=px.histogram(mysportsbetting, x="Month_Name", title="Event Distribution by Month",category_orders={"Month_Name":ordered_month_names}, 
                         color="Month",text_auto=True,height=300)
        fig.update_xaxes(title="Month")
        fig.update_yaxes(title="Number of Events")
        st.plotly_chart(fig)  
    with col2:
        ordered_weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        fig=px.histogram(mysportsbetting, x="Day_of_Week_Name", title="Event Distribution by Day of the Week",category_orders={"Day_of_Week_Name":ordered_weekday_names},
                         color="Day_of_Week",text_auto=True,height=300)
        fig.update_xaxes(title="Weekday")
        fig.update_yaxes(title="Number of Events")
        st.plotly_chart(fig)  

#-----TAB 3 (WAGER VS WIN)------#


with tab3:
    col1,col2,col3=st.columns(3)
    with col1:
        SPORTS=['Basketball', 'Other', 'Horse Racing', 'Football', 'Greyhound Racing', 'Tennis']
        sport= st.multiselect("Select Sport Group:",SPORTS)
        if sport:
            mysportsbetting=mysportsbetting[mysportsbetting["Sport_Group"].isin(sport)]
    with col2:
        PURCHASE=["Live","Prematch"]
        purchaset = st.multiselect("Select Purchase Time:", PURCHASE)
        if purchaset:
            mysportsbetting=mysportsbetting[mysportsbetting["Purchase_Time"].isin(purchaset)]
    with col3:
        GENDER=['Male', 'Female', 'Not Applicable']
        genderc= st.multiselect("Select Gender:",GENDER)
        if genderc:
            mysportsbetting=mysportsbetting[mysportsbetting["Gender_Competition"].isin(genderc)]
            
    total_wager = mysportsbetting["Wager"].sum().astype(int)
    total_winnings = mysportsbetting["Winnings"].sum().astype(int)
    # hold = ((total_winnings*100)/total_wager).round(2)
    
    locale.setlocale(locale.LC_ALL, '')
    total_wager_formatted = locale.format_string("%d", total_wager, grouping=True)
    total_winnings_formatted = locale.format_string("%d", total_winnings, grouping=True)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.markdown(f"**Total wager: {total_wager_formatted}€**")
    with col2:
        st.markdown(f"**Total Win: {total_winnings_formatted}€**")
    with col3:
        st.markdown(f"")
    with col4:
        st.markdown(f"")
    with col5:
        st.markdown(f"")
        
    data_by_date = mysportsbetting.groupby("Event_Date").agg({"Wager": "sum", "Winnings": "sum"}).reset_index()
    fig = px.line(data_by_date, x="Event_Date", y=["Wager", "Winnings"], title="Evolution of Wager and Winnings by Date",
                labels={"Event_Date": "Date", "value": "Amount", "variable": "Type"},width=1750,height=400)
    st.plotly_chart(fig)
    
    # data_by_weekday = mysportsbetting.groupby("Day_of_Week_Name").agg({"Wager": "sum", "Winnings": "sum"}).reset_index()
    # fig = px.line(data_by_weekday, x="Day_of_Week_Name", y=["Wager", "Winnings"], title="Evolution of Wager and Winnings by Weekday",
    #             labels={"Day_of_Week_Name": "Weekday", "value": "Amount", "variable": "Type"},width=1750,height=300)
    # st.plotly_chart(fig)
    
    data_by_sport = mysportsbetting.groupby("Sport_Group").agg({"Wager": "sum", "Winnings": "sum"}).reset_index()
    fig = px.scatter(data_by_sport, x="Sport_Group", y=["Wager", "Winnings"], title="Evolution of Wager and Winnings by Sport Group",
                labels={"Sport_Group": "Sport Group", "value": "Amount", "variable": "Type"},width=1750,height=400)
    st.plotly_chart(fig)

#-----TAB 4 (HOLD)------#

with tab4:
    col1,col2=st.columns(2)
    with col1:
        hold_avg_by_sport_group = (mysportsbetting.groupby("Sport_Group")["Hold"].mean()).round(4)*100
        fig=px.histogram(hold_avg_by_sport_group,x=hold_avg_by_sport_group.index,y=hold_avg_by_sport_group.values,title="Hold Average of each Sports Group",
                        template="plotly_dark",color=hold_avg_by_sport_group.index,color_discrete_map=color_map_sport_group,text_auto=True)
        fig.update_traces(texttemplate='%{y:.2f}%', textposition='outside')
        fig.update_xaxes(title="Sport Group")
        fig.update_yaxes(title="Hold")
        st.plotly_chart(fig)  
        
    with col2:
        total_hold = mysportsbetting["Hold"].sum()
        hold_avg_by_sport_group_relative = (mysportsbetting.groupby("Sport_Group")["Hold"].sum() / total_hold).round(4)*100
        fig = px.pie(hold_avg_by_sport_group_relative, values=hold_avg_by_sport_group_relative.values,
             names=hold_avg_by_sport_group_relative.index,title="Average Hold from the total Hold by Sport Group",
             hole=0.3, color=hold_avg_by_sport_group_relative.index,color_discrete_map=color_map_sport_group)
        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig)  
        
    col1,col2=st.columns(2)
    with col1:
        hold_avg_by_purchase_time = (mysportsbetting.groupby("Purchase_Time")["Hold"].mean()).round(4)*100
        fig=px.histogram(hold_avg_by_purchase_time,x=hold_avg_by_purchase_time.index,y=hold_avg_by_purchase_time.values,title="Hold Average of each Purchase Time",
                        color=hold_avg_by_purchase_time.index,color_discrete_map=color_map_purchase_time,text_auto=True)
        fig.update_traces(texttemplate='%{y:.2f}%', textposition='outside')
        fig.update_xaxes(title="Purchase Time")
        fig.update_yaxes(title="Hold")                 
        st.plotly_chart(fig)  
    with col2:
        # hold_avg_by_purchase_time_relative = (mysportsbetting.groupby("Purchase_Time")["Hold"].sum() / total_hold).round(4) * 100
        # fig = px.bar(hold_avg_by_purchase_time_relative,x=hold_avg_by_purchase_time_relative.index, 
        #             y=hold_avg_by_purchase_time_relative.values, color=hold_avg_by_purchase_time_relative.index, color_discrete_map=color_map_purchase_time,text_auto=True,
        #             title="Avergae Hold of each Pruchase Time respect to the total Hold")
        # fig.update_traces(texttemplate='%{y:.2f}%', textposition='outside')
        # fig.update_xaxes(title="Purchase Time")
        # fig.update_yaxes(title="Hold Average from total Hold")
        hold_avg_by_purchase_time_relative = (mysportsbetting.groupby("Purchase_Time")["Hold"].sum() / total_hold).round(4)*100
        fig = px.pie(hold_avg_by_purchase_time_relative, values=hold_avg_by_purchase_time_relative.values,
                    color=hold_avg_by_purchase_time.index,color_discrete_map=color_map_purchase_time,
                    names=hold_avg_by_purchase_time_relative.index, title="Avergae Hold of each Pruchase Time respect to the total Hold",hole=0.3)
        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig)  


#-----TAB 5 (POWERBI)------#

with tab5:
    power_bi_url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiZTIyMjcxNjktZGExMS00MDljLWJmMjYtYzFiZDMzMmZhMDZiIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9&pageName=ReportSection"
    iframe_width = 2500
    iframe_height = 800

    st.markdown(f'<iframe src="{power_bi_url}" width={iframe_width} height={iframe_height} style="position:absolute; left:-300px;"></iframe>', unsafe_allow_html=True)

#-----TAB 6 (PREDICTION)------#

with tab6:
    
    st.markdown("**Equivalence Tables**:")
    col1,col2,col3=st.columns(3)
    with col1:
        purchase_time_mapping = sports_regression.drop_duplicates(subset=["Purchase_Time_encoded"])[["Purchase_Time_encoded", "Purchase_Time"]]
        purchase_time_mapping=purchase_time_mapping.sort_values(by="Purchase_Time_encoded")
        purchase_time_mapping_html=purchase_time_mapping.to_html(index=False)
        st.write(purchase_time_mapping_html, unsafe_allow_html=True)
    with col2:
        sport_group_mapping = sports_regression.drop_duplicates(subset=["Sport_Group_encoded"])[["Sport_Group_encoded", "Sport_Group"]]
        sport_group_mapping = sport_group_mapping.sort_values(by="Sport_Group_encoded")
        sport_group_mapping_html=sport_group_mapping.to_html(index=False)
        st.write(sport_group_mapping_html, unsafe_allow_html=True)
    with col3:
        st.markdown("")
    st.markdown("")
        
    ssl._create_default_https_context = ssl._create_stdlib_context


    API_KEY = '6lvhYcEDrhQ7DdyN8XSfWjH2QrbLX2jU'

    URL = 'https://marina-mpxpr.francecentral.inference.ml.azure.com/score'

    Purchase_Time_encoded, Sport_Group_encoded, Wager = st.columns(3)
    with Purchase_Time_encoded:
        Purchase_Time_encoded = st.number_input("Select/Enter Purchase Time:", min_value=0, value=1)

    with Sport_Group_encoded:
        Sport_Group_encoded = st.number_input("Select/Enter Sport Group:", min_value=0, value=1)

    with Wager:
        Wager = st.number_input("Select/Enter Wager amount:", min_value=0, value=1)

    if st.button("Perform prediction"):
        # Estructura de datos para la solicitud POST
        data = {
            "input_data": {
            "columns": [
            "Purchase_Time_encoded",
            "Sport_Group_encoded",
            "Wager"
                ],
                "index": [0],
                "data": [[Purchase_Time_encoded,Sport_Group_encoded,Wager]]

            }
        }

        # Convertir a JSON
        body = str.encode(json.dumps(data))

        headers = {
            'Content-Type': 'application/json',
            'Authorization': ('Bearer ' + API_KEY)
        }

        # Crear y enviar la solicitud POST
        try:
            req = urllib.request.Request(URL, body, headers)
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read())
                predicted_profit = round(result[0], 2)
                st.write("Pedicted Profit:")
                st.markdown(f"### Predicted Profit: **${predicted_profit}**")
                
        except urllib.error.HTTPError as error:
            st.error(f"Application error: {error.code}")
            st.write(error.info())
            st.write(error.read().decode("utf8", 'ignore'))    
