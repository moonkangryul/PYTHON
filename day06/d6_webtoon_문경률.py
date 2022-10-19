from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd
import time

path = "C:\\PYTHONWORK\\chromedriver.exe"
driver = wd.Chrome(path)
driver.get('https://comic.naver.com/genre/bestChallenge')
time.sleep(1)

list = []
for j in range(1,10):
    week_callenge = driver.find_element(By.ID, 'content')
    callenge_list = week_callenge.find_elements(By.CSS_SELECTOR, 'tr td')
    for i in callenge_list:
        try:
            title = i.find_element(By.TAG_NAME, 'h6').text
            summary = i.find_element(By.CLASS_NAME, 'summary').text
            grade = i.find_element(By.TAG_NAME, 'strong').text
            list.append([title,summary,grade])
                
        except:
            continue
    print(list)         
    driver.find_element(By.CSS_SELECTOR,'#content > div.paginate > div > a.next').click()
    time.sleep(1)

webtoon_df = pd.DataFrame(list,columns=('이름','내용','평점'))
webtoon_df.to_csv('day06/webtoon.csv',encoding='utf-8-sig',mode='w',index=False)                   

