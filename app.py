import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import datetime
from PIL import Image


data=pd.read_excel('Data_Train.xlsx')
data.drop(['Route','Duration'],axis=1)

data['Total_Stops'].map({'non-stop':0, '2 stops':2, '1 stop':3, '3 stops':3,'4 stops':4})

label=LabelEncoder()
data['Airline']=label.fit_transform(data['Airline'])
data['Source']=label.fit_transform(data['Source'])
data['Destination']=label.fit_transform(data['Destination'])
data['Additional_Info']=label.fit_transform(data['Additional_Info'])
data['Total_Stops']=label.fit_transform(data['Total_Stops'])

x=data.drop(['Price','Route','Duration','Date_of_Journey','Dep_Time','Arrival_Time'],axis=1)
y=data['Price']
model=RandomForestRegressor()
model.fit(x,y)
#Image
image=Image.open('Emirates-Dreamliner-916x516.jpg')


def main():
    
   st.title("Flight-Price-Prediction")
   st.write(" *--Built using StreamLit--* ")
   #html code
   html_temp = """
   <div style ="background-color:Purple;padding:13px">
   <h1 style ="color:MediumSeaGreen;text-align:center;"> Check the flight price prediction the below  ML App </h1>
   <style>
   reportview-container {
      background: url("pexels-thomas-petitroche-2517931.jpg")
   }
   sidebar .sidebar-content {
      background: url("url_goes_here")
   }
   </style>
   </div>
   """
   st.markdown(html_temp, unsafe_allow_html = True)


   st.image(image,caption='Check you have heart disease')



    
    


   st.subheader("Select Source")
   source = st.selectbox(" " , ['Bangalore', 'Mumbai','Delhi','Kolkata',"Chennai"])
   if source == "Bangalore":
      source_inp = 0
   elif source == "Chennai":
      source_inp = 1
   elif source == "Delhi":
      source_inp = 2
   elif source == "Kolkata":
      source_inp = 3
   elif source == "Mumbai":
      source_inp = 4
    
   st.write("Source -- " , source)

    #destination
   st.subheader("Select Destination")
   dest = st.selectbox("" , ['Bangalore', 'Cochin', 'Hyderabad',"New Delhi",'Delhi','Kolkata'])

   if dest == "Bangalore":
      dest_inp = 0
   elif dest == "Cochin":
      dest_inp = 1
   elif dest == "Delhi":
      dest_inp = 2
   elif dest == "Hyderabad":
      dest_inp = 3
   elif dest == "Kolkata":
      dest_inp = 4
   elif dest == "New Delhi":
      dest_inp = 5

   st.write("Destination -- ",dest)

    #airline
   st.subheader("Select Airline")
   airline = st.selectbox("  " , ["Air India","GoAir","IndiGo","Jet Airways","Multiple carriers","SpiceJet",
                                    "Vistara","Air Asia"])

   if airline == "Jet Airways":
      air_inp = 0
   elif airline == "IndiGo":
      air_inp = 1
   elif airline == "Air India":
      air_inp = 2
   elif airline == "Multiple carriers":
      air_inp = 3
   elif airline == "SpiceJet":
      air_inp = 4
   elif airline == "Vistara":
      air_inp = 5
   elif airline == "Air Asia":
      air_inp = 6
   elif airline == "GoAir":
      air_inp = 7

   st.write("Airline -- " , airline)
   addition_info=st.selectbox(" ",['No info', 'In-flight meal not included',
       'No check-in baggage included', '1 Short layover', 'No Info',
       '1 Long layover', 'Change airports', 'Business class',
       'Red-eye flight', '2 Long layover'])
   if addition_info== 'No info':
      addition_info=8
   elif  addition_info== 'In-flight meal not included':
      addition_info=7
   elif  addition_info== 'No check-in baggage included':
      addition_info=6
   elif  addition_info== '1 Short layover':
      addition_info=5
   elif  addition_info== '1 Long layover':
      addition_info=4
   elif  addition_info== 'Change airports':
      addition_info=3
   elif  addition_info== 'Business class':
      addition_info=2
   elif  addition_info== 'Red-eye flight':
      addition_info=1
   elif  addition_info== '2 Long layover':
      addition_info=0
   Date_of_Journey=st.date_input('Enter your journy',datetime.date(2019,1,1))
   Dep_Time=st.time_input("Enter Dep_time")
   Arrival_Time=st.time_input("Enter Arrival_Time")
   
    


   st.subheader("Select Stops")
   stop = st.selectbox("   " , [0,1,2,3,4])
   


   if st.button("PREDICT"):
      result= model.predict([[air_inp , source_inp , dest_inp,addition_info,stop ]])
      st.success(f'The flight  price is {result[0]:.2f}')



if __name__ == "__main__":
   main()
