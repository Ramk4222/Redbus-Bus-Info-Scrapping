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

def b1():
    d=webdriver.Chrome()
    d.get('http://www.google.com/');
    c=d.find_element(By.TAG_NAME,'textarea')
    c.send_keys('redbus')
    c.submit()
    d.get('https://www.redbus.in/')

    V=d.find_element(By.TAG_NAME,"body")
    V.send_keys(Keys.PAGE_DOWN)
    d.get('https://www.redbus.in/online-booking/rtc-directory')
    h1=d.find_elements(By.CSS_SELECTOR,"a[class='D113_link']")
    g=[i.text for i in h1]
    d.find_element(By.XPATH,"//*[@id='root']")
    route_1link=[]
    route_2name=[]
    f1=set()
    route_2name=[]
    for i in route_2name:
        if i not in f1:
            f1.add(i)
            route_2name.append(i)
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
    star=[]
    h=[k for k in range(3,24,2)]

    j=0
    while j<=10:
        h2=d.find_elements(By.CSS_SELECTOR,"a[class='D113_link']")
        
        
        link=[h2[i].get_attribute('href') for i in range(0,len(h2))]
        if j<=5:
            h=[k for k in range(2,14,2)]
            d.get(link[h[j]])
        else:
            h=[k for k in range(0,24,2)]
            h.remove(14)
            h.remove(12)
            d.get(link[h[j]])
    
        L=d.find_element(By.TAG_NAME,"body")
        L.send_keys(Keys.PAGE_DOWN) 
        n=d.find_elements(By.CLASS_NAME,"DC_117_pageTabs")
        t=2
        while t<=len(n)+1:
            m=d.find_element(By.CLASS_NAME,"DC_117_paginationTable")
            link=[h.get_attribute('href') for h in d.find_elements(By.CSS_SELECTOR,"a[class='route']")]
            route_1link.extend(link)
            name=[h.get_attribute('title') for h in d.find_elements(By.CSS_SELECTOR,"a[class='route']")]
            R=0
            while R>=0:
                wait=WebDriverWait(d,10)
                m=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,f"{name[R]}")))
                actions = ActionChains(d)
                actions.move_to_element(m).perform()                                     
                time.sleep(1)
                m.click()
                
                l=d.find_element(By.TAG_NAME,"body")
                w=WebDriverWait(d,10)
                try:
                    u=w.until(EC.presence_of_element_located((By.CSS_SELECTOR,"i[class='icon icon-right']"))) 
                    time.sleep(1)
                    u.click()
                except:
                    u=w.until(EC.presence_of_element_located((By.CSS_SELECTOR,"i[class='icon icon-right']"))) 
                    time.sleep(1)
                    u.click()
                finally:      
                    try:
                        mt1=w.until(EC.presence_of_element_located((By.CSS_SELECTOR,"i[class='p-left-10 icon icon-down']")))
                        mt1.click()
                    except:
                        a=1+1   
                    finally: 
                        i=0   
                        while i>=0:
                            old_page_source=d.page_source   
                        
                            body=d.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
                            time.sleep(2)
                        
                            new_page_source=d.page_source
                            i+=5
                            if i>=40:
                                break     
                        bus_name=d.find_elements(By.CSS_SELECTOR,"div[class='travels lh-24 f-bold d-color']")
                        all_bus_name=[h.text for h in bus_name]
                        BusName.extend(all_bus_name)
                        bus_type=d.find_elements(By.CSS_SELECTOR,"div[class='bus-type f-12 m-top-16 l-color evBus']")
                        all_bus_type=[h.text for h in bus_type]
                        BusType.extend(all_bus_type)
                        departure=d.find_elements(By.CSS_SELECTOR,"div[class='dp-time f-19 d-color f-bold']")
                        all_departure=[h.text for h in departure]
                        Departure.extend(all_departure)
                        duration=d.find_elements(By.CSS_SELECTOR,"div[class='dur l-color lh-24']")
                        all_duration=[h.text for h in duration]
                        Duration.extend(all_duration)
                        arrival=d.find_elements(By.CSS_SELECTOR,"div[class='bp-time f-19 d-color disp-Inline']")
                        all_arrival=[h.text for h in arrival]
                        Arrival.extend(all_arrival)
                        star_rating=d.find_elements(By.CSS_SELECTOR,"span[class='']")
                        all_star_rating=[h.text for h in star_rating]
                        for i in range(0,len(all_star_rating),2):
                            StarRating.append(all_star_rating[i])
                        price=d.find_elements(By.CSS_SELECTOR,"span[class='f-19 f-bold']")
                        all_price=[h.text for h in price]
                        print(all_price)
                        price_float=[float(v) for v in all_price]
                        price_int=[int(v) for v in price_float]
                        Price.extend(price_int)
                        seats_available=d.find_elements(By.CSS_SELECTOR,"div[class='column-eight w-15 fl']")
                        all_seats_available=[h.text for h in seats_available]
                        SeatsAvailable=[h.replace('\n','') for h in all_seats_available]
                        star_int=[float(c) for c in all_star_rating]
                        for i in range(0,len(SeatsAvailable)):
                            seats.append(SeatsAvailable[i])        
                        for i in range(0,len(star_int),2):
                            star.append(star_int[i])  
                        f1=f'{name[R]}' 
                        for q in range(len(all_bus_name)):
                            c=p.append(f1)     
                        z=f'{link[R]}' 
                        for q in range(len(all_bus_name)):
                            c1=p1.append(z) 
                        
                        d.back()
                        d.back()
                        d.back()
                R+=1 
                if R>=len(name)-1: 
                    break    
                        
            if t>=len(n)+1:
                break
            else: 
                m=d.find_element(By.CLASS_NAME,"DC_117_paginationTable")
                next=m.find_element(By.XPATH,f"//*[@id='root']/div/div[4]/div[12]/div[{t}]")
                actions = ActionChains(d)
                actions.move_to_element(next).perform()
                t+=1 
                next.click() 
        if j<=10:
            g1=Price*(len(BusName)//len(Price))+Price[:len(BusName)%len(Price)]
            g2=star*(len(BusName)//len(star))+star[:len(BusName)%len(star)]
            details=dict(route_name=p,route_link=p1,Bus_name=BusName,Bus_type= BusType,Departure=Departure,Duration=Duration,
                    Arrival=Arrival,Starrating=g2,Price=g1,Seats=seats)  
            c9=pd.DataFrame(details)
    
            w1=",".join(f"{i2} {j3}"
            for i2,j3 in zip(c9.columns,c9.dtypes)).replace("object","text").replace("int64","int").replace("float64","float")
            g1=['BSTDC', 'West_Bengal_Transport_Corporation','BSRTC', 'NORTH_BENGAL_STATE_TRANSPORT_CORPORATION','CTC','BSRTC_Operated_By_VIP_Travels','SBSTC','HPTDC', 
                'PEPSU','PEPSU','RSRTC','HRTC','UPSRTC','CTU','PRTC','TNSTC','KSRTC','KTCL','TSRTC','APSRTC','ASTC','KAAC_TRANSPORT','SNT', 
                'MTC','GSRTC']
            if j<=5:
                h3=[k for k in range(2,14,2)]
            else:
                h3=[k for k in range(0,24,2)]
                h3.remove(14)
                h3.remove(12)
            r2=f"create table {g1[h3[j]]}({w1})"  
            myconnection=pymysql.connect(host='127.0.0.1',user='root',password='Ramk@2001',database='Redbus')
            cursor=myconnection.cursor()
            myconnection.cursor().execute(r2) 
            r3=f"insert into {g1[h3[j]]} values"
            print(c9["Starrating"])
            for i in range(len(c9)):
               f1= f"insert into {g1[h3[j]]} (route_name, route_link, Bus_name, Bus_type, Departure, Duration, Arrival, Starrating, Price, Seats) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
               print(f1)
               f2=tuple(c9.iloc[i])
               print(f2)
               cursor.execute(f1,f2)
               myconnection.commit()
        
            p.clear()
            p1.clear()
            BusName.clear()
            BusType.clear()
            Departure.clear()
            Duration.clear()
            Arrival.clear()
            seats.clear()
            Price.clear()
            star.clear()
            route_1link.clear()
            j+=1
            d.get('https://www.redbus.in/online-booking/rtc-directory')                                                                                                 
with st.sidebar:
    st.title(":red[RedBus]")
    st.header('Home')
    st.subheader("Project Done By Using")
    st.caption("Selenium")
    st.caption("MySQL")
    st.caption("Python")

st.title("Welcome to Redbus")
st.image("/Users/ramkumarbalusamy/Downloads/project/ram/red.jpeg",width=800)    
st.title("Profile")
Name,age=st.columns(2)
h=Name.text_input("Name")
age.text_input("Age")
Email,MobileNo=st.columns([3,1])
Email.text_input("Email")
MobileNo.text_input("Mob NO")
Password,Repassword=st.columns(2)
Password.text_input("Password",type="password")
Repassword.text_input("Re-password",type="password")
ch,sb=st.columns(2)
ch.checkbox("I agree")
p=sb.button("Submit")
S=st.checkbox("Show Buses")
myconnection=pymysql.connect(host='127.0.0.1',user='root',password='Ramk@2001',database='Redbus_info')   
cursor=myconnection.cursor()
if S:
    Buses=st.radio("SELECT THE BUSES",('BSRTC','CTC','SBSTC','PEPSU','RSRTC','UPSRTC','KSRTC','TSRTC','ASTC','SNT'))  
    if Buses=='BSRTC':
        query="select * from BSRTC"
        cursor.execute(query)
        t1=cursor.fetchall()
        df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
        st.write(df)

    elif Buses=='CTC':
        query="select * from CTC"
        cursor.execute(query)
        t1=cursor.fetchall()
        df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
        st.write(df)
    elif Buses=='SBSTC':
        query="select * from SBSTC"
        cursor.execute(query)
        t1=cursor.fetchall()
        df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
        st.write(df)
    elif Buses=='PEPSU':
        query="select * from PEPSU"
        cursor.execute(query)
        t1=cursor.fetchall()
        df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
        st.write(df)
    elif Buses=='RSRTC':
        query="select * from RSRTC"
        cursor.execute(query)
        t1=cursor.fetchall()
        df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
        st.write(df)
    elif Buses=='UPSRTC':
        query="select * from UPSRTC"
        cursor.execute(query)
        t1=cursor.fetchall()
        df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
        st.write(df)
    elif Buses=='KSRTC':
        query="select * from KSRTC"
        cursor.execute(query)
        t1=cursor.fetchall()
        df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
        st.write(df)    
    elif Buses=='TSRTC':
        query="select * from TSRTC"
        cursor.execute(query)
        t1=cursor.fetchall()
        df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
        st.write(df)           
    elif Buses=='ASTC':
        query="select * from ASTC"
        cursor.execute(query)
        t1=cursor.fetchall()
        df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
        st.write(df)      
    elif Buses=='SNT':
        query="select * from SNT"
        cursor.execute(query)
        t1=cursor.fetchall()
        df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
        st.write(df)                                                          
    Search_BUS=st.text_input("Enter State_name")
    from_to=st.text_input("Enter from-to")
    buses=st.selectbox("buses",("top rating",
                                        "less price",
                                        "Government BUS",
                                        "AC",
                                        "NON-AC"))
    if Search_BUS and from_to:
        if buses=="top rating":
            query=f"select * from {Search_BUS} where route_name='{from_to}' order by Starrating desc;"
            print(query)
            cursor.execute(query)
            t1=cursor.fetchall()
            df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
            st.write(df)     
        elif buses=="less price":
            query=f"select * from {Search_BUS} where route_name='{from_to}' order by Price asc;"
            print(query)
            cursor.execute(query)
            t1=cursor.fetchall()
            df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
            st.write(df)     
        elif buses=="Government BUS":
            query=f"select * from {Search_BUS} where Bus_name like '%{Search_BUS}%' order by Duration asc;"
            print(query)
            cursor.execute(query)
            t1=cursor.fetchall()
            df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
            st.write(df)         
        elif buses=="AC":
            query=f"select * from {Search_BUS} where Bus_name like '%{Search_BUS}%' and Bus_type not like '%Non%' order by Duration asc;"
            print(query)
            cursor.execute(query)
            t1=cursor.fetchall()
            df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
            st.write(df)             
        elif buses=="NON-AC":
            query=f"select * from {Search_BUS} where Bus_name like '%{Search_BUS}%' and Bus_type  like '%Non%' order by Duration asc;"
            print(query)
            cursor.execute(query)
            t1=cursor.fetchall()
            df=pd.DataFrame(t1,columns=["route_name","route_link","Bus_name","Bus_type","Departure","Duration","Arrival","Starrating","Price","Seats"])
            st.write(df)   
Bus_type=st.text_input("Bustype")
Bus_Name=st.text_input("BusName")
Price=st.text_input("Price")                        
selected=st.checkbox("Details")
if selected:
    st.write(Search_BUS)     
    st.write(from_to)         
    st.write(Bus_type)
    st.write(Bus_Name)
    st.write(Price)

pay=st.checkbox("Payment")   
if pay:
    st.write("Booking Confirmed",h)
    st.text("Thanks for choosing Redbus")
    st.snow()
