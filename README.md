# **Online Sports Bettings**

<p align="center">
  <img src="Images\soccer-9133_256.gif">
</p>

 This is a project related to Online Sports Betting in Spain where the aim is to obtain a model that predicts the sports group that brings the most profit to a company given a sample data set. 

## **Table of Contents**

 1. [Streamlit App](#Streamlit-App)
 2. [User Guide](User-Guide)
 3. [Files & Main Challenges](Files-&-Main-Challenges)
 4. [Key Results](Key-Results)
 5. [Contributing](Contributing)


### ![alt text](streamlit-1.png)**Streamlit App**

A Streamlit application has been created to show some of the results obtained during this project. It can be accessed directly from [Online Sports Betting](https://online-sports-bettings-kbrepywzhd5mjvfpihsmsb.streamlit.app/).    
  
This is a multi-tab application where you can browse through different information on each tab.     
  - Tabs & Content:     

    - Context: This tab provides an overview of the number of Online Sportbetting houses in Spain and their ratings. It has a filter to display them according to the rating of the public.       
    - Events Distribution: This tab shows the number of events (competitions) on which bets have been placed during the period recorded in the dataset used in the project.     
    - Wager vs Win: Overview and comparison of the amount bet by the players and the amount earned by the company. By using filters, some more concrete data can be displayed.      
    - PowerBI: A PowerBI panel with different statistics has been added in this Tab. It can also be consulted [PowerBI](https://app.fabric.microsoft.com/view?r=eyJrIjoiZTIyMjcxNjktZGExMS00MDljLWJmMjYtYzFiZDMzMmZhMDZiIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9&pageName=ReportSection).     
    - Prediction: In this tab you can predict the company's profit by specifying a sport group and the time of purchase of the bet.       

### **User Guide**

#### Replicate the application  

  It's easy! Just copy this repository and use your Streamlit Share account.  
 
#### Modify application elements 

- Streamlit Local Host  

  - Open the repository in Visual Studio Code.  
  - Open the Terminal by pressing Ctrl+J or from the top right menu.  
  - Type in the Terminal "Streamlit run app.py". If necessary, replace "app.py" with the relative path of the application's main .py file.  
  - Once the app is visualised in Streamlit Local, you can start applying changes and improvements. Always from the application's .py files.  
  - Whenever you save a change in Visual Studio Code, you will have to refresh Streamlit to be able to see the applied changes. 

- Share Streamlit 

  - Make a copy of the repository on your GitHub. 
  - Open the repository in Visual Studio Code.  
  - Log in to your Share Streamlit account. 
  - Select "New app". 
  - Choose the repository containing the application. 
  - Click the "Deploy!" button. 
  - Make sure that the versions in the requirements.txt file match the ones you have in your version of Visual Studio Code. If not, update them to avoid errors.  
  - Once the app is visualised in Share Streamlit, you can start applying changes and improvements. Always from the application's .py files.  
  - Whenever you save a change in Visual Studio Code, you will have to refresh Streamlit to be able to see the applied changes. 

### **Files & Main Challenges**

- [App](app.py)
- Notebooks:
  - [Preprocesing & EDA](Notebooks/Data Pre-Processing & EDA.ipynb)
  - [Data Analysis](Notebooks\Data Analysis Graphs.ipynb)
  - [Webcrapping](Notebooks\Webscrapping_Betting_Houses.ipynb)
  - [Regression Model](Notebooks\Regression model, Wager.ipynb)
- [Data](Data)
- [Images](Images)


### **Key Results**

### **Contributing**

  Contributions to this project are welcome. If you find any bugs or have any suggestions for improvement, feel free to open an Issue or send a Pull Request.


