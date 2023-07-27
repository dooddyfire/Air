from bs4 import BeautifulSoup 
import requests 
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pyperclip

import time

url = "http://air4thai.pcd.go.th/webV3/#/Report"
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

#data-v-6daa256b

driver.get(url)

soup = BeautifulSoup(driver.page_source,'html.parser')

card_lis = soup.find_all('div',{'class':'card'})
aqi_lis = []
pm25_lis = []
pm10_lis = []
title_lis = []

for i in card_lis: 
    aqi = i.find('p',{'class':'aqiFace-Text-small'}).text 
    print("AQI : ",aqi)

    title = i.find('label',{'class':'station-small'}).text
    print(title)
    title_lis.append(title)

    pm_lis = [ det.text for det in i.find('div',{'class':'row'}).find_all('strong')][3:]
    

    if len(pm_lis) == 1: 
        pm25 = pm_lis[0]
        pm10 = ""
        print('PM 2.5 : ',pm25)
        print('PM 10 : ',pm10)

    
    else: 
        pm25 = ""
        pm10 = pm_lis[1]
        print('PM 2.5 : ',pm25)
        print("PM 10 : ",pm10)
    
    aqi_lis.append(aqi)
    pm25_lis.append(pm25)
    pm10_lis.append(pm10)

df = pd.DataFrame()
df['Station'] = title_lis 
df['AQI'] = aqi_lis 
df['PM2.5'] = pm25_lis 
df['PM10'] = pm10_lis

df.to_excel('station.xlsx')
    

