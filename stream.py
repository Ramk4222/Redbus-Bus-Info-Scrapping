import streamlit as st 
import time
import pandas as pd
import pymysql
import subprocess
import time
from pyspark.sql import SparkSession
import sys
path='/Users/ramkumarbalusamy/Downloads/project/project_1u.py'

st.title("Welcome to Redbus")
st.image("/Users/ramkumarbalusamy/Downloads/project/ram/red.jpeg",width=800)
st.title("Get Your Best Choice")
with st.form("Search Bus:"):
    departure=st.text_input("From")
    arrival=st.text_input('To')
    Submit=st.form_submit_button('Submit')
if Submit:
     request_id = str(int(time.time()))
     subprocess.Popen([sys.executable,path, departure, arrival,request_id] )
     st.write("Scraping started...")
     connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="Ramk@2001",
        database="now"
    )
     cursor=connection.cursor()
     max_wait = 130
     waited = 0

     with st.spinner("Fetching data..."):
       
        while waited < max_wait:
            connection.commit()
            query = f"""
                SELECT * FROM redbus_table 
                where request_id ='{request_id}'
            """
            cursor.execute(query)
            t1=cursor.fetchall()
            df=pd.DataFrame(t1,columns=["event","Busname","Bustype","Departure","Duration","Arrival","Seats_Avail","Price","Star_Rate","request_id"])
            print(df)

            if not df.empty:
                st.success("Data Loaded ✅")
                st.write(df)
                i=1
                break

            time.sleep(5)
            waited += 4

        if waited >= max_wait:
            st.error("Timeout! No data found.")

     connection.close()