from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import datetime
import time

def CoffeeBean_store(result):
    wd = webdriver.Chrome('C:\\PYTHONWORK\\chromedriver.exe')
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    #storeListUL > li:nth-child(1) > div.store_txt > p.name > span  
    for i in range(1,100):
        wd.get(CoffeeBean_URL)
        time.sleep(1)
        try:
            wd.execute_script('storePop2(%d)' %i)
            time.sleep(1)
            html = wd.page_source
            soup = BeautifulSoup(html,'html.parser')
            store_name_sp = soup.select('div.store_txt > h2')
            store_name = store_name_sp[0].string
            print(store_name)
            result([store_name])
            print(result)
        except:
            continue
    

result = []
CoffeeBean_store(result)