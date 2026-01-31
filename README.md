# Project Title
**Redbus Webscraping with selenium and filtering using Streamlit**

# Project Overview
     This project is about to collect Datas with Webscraping tool Selenium from Redbus Bus infos like Travelsname, Bustype, Travel Duration,etc,...With the help of these Extracted Raw datas, 
     I have transformed into proper Dataframe and done Data Cleaning then loaded into SQL. I Created Streamlit-UI Interface to choose and make better decision in their travel. Also
     Users can apply filters query to choose their conviented Bus with lots of options.
     
# Architecture
    Python Script -> Pandas -> SQL -> Streamlit UI

# Tech Stack
   * Python 3.8+
   * Pandas
   * Pymysql
   * Streamlit

# Project Structure
```text
|
|---Scrapper.py
|---requirements.txt
|---README.md
```
# How To Run The Project

 **STEP-1**
 ```bash 
     git clone https://github.com/Ramk4222/Redbus-Bus-Info-Scrapping.git
     cd Redbus-Bus-Info-Scrapping
 ``` 
     
 **STEP-2**
 ```bash
     python -m venv upd
     source upd/bin/activate
  ```

 **STEP-3**
  ```bash
     pip install -r requirements.txt
  ```
**STEP-4**

```bash
   python Scrapper.py
```
```bash to Run Streamlit
   Streamlit Run Scrapper.py
```


# Future Enhancements
 * Integrate Kafka Streaming Real-time Data

# Author

Ramkumar Balusamy



    
     

    
 
      

   
