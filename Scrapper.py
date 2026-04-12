from selenium import webdriver#for automation
from selenium.webdriver.common.by import By# for indentify 
from selenium.webdriver.common.keys import Keys#to insert values
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import streamlit as st 
import pandas as pd
import pymysql
from producer import send_to_kafka
from spark_consumer import Spark_cons
from multiprocessing import Process
import sys

source = sys.argv[1]
destination = sys.argv[2]
request=sys.argv[3]
print("Script started")
print("Arguments received:", sys.argv)
def b1(source,destination,request):
    d=webdriver.Chrome()
    d.get('https://www.redbus.in/')
    d.maximize_window()
    src=d.find_element(By.XPATH,'//*[@id="srcinput"]')
    src.send_keys(source)
    time.sleep(2)
    src.send_keys(Keys.ARROW_DOWN)
    src.send_keys(Keys.ENTER)
    srh=d.find_element(By.XPATH,'//*[@id="destinput"]')
    srh.send_keys(destination)
    time.sleep(2)
    srh.send_keys(Keys.ARROW_DOWN)
    srh.send_keys(Keys.ENTER)
    time.sleep(2)
    w=WebDriverWait(d,10)
    u=w.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[aria-label='Search buses']"))) 
    u.click()
    time.sleep(5)
    p1=[]
    p=[]
    BusName=[]
    BusType=[]
    Departure=[]
    Duration=[]
    Arrival=[]
    StarRating=[]
    Price=[]
    seats=[]
    data=[]
    try:
       w=WebDriverWait(d,10)
       u=w.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[aria-label='Proceed']"))) 
       u.click()  
       time.sleep(5)
    except:
       print("proceeded")
    finally:    
        total=d.find_element(By.CSS_SELECTOR,"span[class='subtitle___66e96d']")
        print(round(int(total.text[0:2])/4))
        for _ in range(18):
          body=d.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
          time.sleep(2)
        bus_name=d.find_elements(By.CSS_SELECTOR,"div[class='travelsName___3da91c']")
        all_bus_name=[h.text for h in bus_name]
        BusName.extend(all_bus_name)
        bus_type=d.find_elements(By.CSS_SELECTOR,"p[class='busType___e916fc']")
        all_bus_type=[h.text for h in bus_type]
        BusType.extend(all_bus_type)
        departure=d.find_elements(By.CSS_SELECTOR,"p[class='boardingTime___8cd3ac']")
        all_departure=[h.text for h in departure]
        Departure.extend(all_departure)
        duration=d.find_elements(By.CSS_SELECTOR,"p[class='duration___3da8b4']")
        all_duration=[h.text for h in duration]
        Duration.extend(all_duration)
        arrival=d.find_elements(By.CSS_SELECTOR,"p[class='droppingTime___ac8c6a']")
        all_arrival=[h.text for h in arrival]
        Arrival.extend(all_arrival)
        star_rating=d.find_elements(By.CSS_SELECTOR,"div[class='rating___082aa7']")
        all_star_rating=[h.text for h in star_rating]
        StarRating.extend(all_star_rating)
        seats_available=d.find_elements(By.CSS_SELECTOR,"p[class='totalSeats___4cda5d']")
        all_seats_available=[h.text for h in seats_available]
        seats.extend(all_seats_available)
        price_d=d.find_elements(By.CSS_SELECTOR,"p[class='finalFare___0b90fc']")
        pric_d=[h.text for h in price_d]
        Price.extend(pric_d)
        print(BusName) 
        print(len(BusName))
        if len(BusName) and len(BusType) and len(Departure) and len(Duration) and len(Arrival):
          for i in range(len(bus_name)):
            data1={"Busname":BusName[i],
                  "Bustype":BusType[i],
                  "Departure":Departure[i],
                  "Duration":Duration[i],
                  "Arrival":Arrival[i],
                  "Seats_Avail":seats[i],
                  "Price":Price[i],
                  "Star_Rate":StarRating[i],
                  "request_id":request}
            data.append(data1)
        print(data) 
        
        for i in range(len(data)):  
            send_to_kafka(data[i])
            time.sleep(1)
        Spark_cons()       
b1(source,destination,request)    