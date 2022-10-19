from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

path = "C:\\PYTHONWORK\\chromedriver.exe"
driver = wd.Chrome(path)
driver.get('http://tour.interpark.com/?mbn=tour&mln=tour_tour')
time.sleep(1)

input = driver.find_element(By.ID,'SearchGNBText')
input.send_keys('제주도')
search_btn = driver.execute_script('searchBarModule.ClickForSearch()')
time.sleep(1)

morebtn = driver.find_element(By.CSS_SELECTOR, 'div.searchAllBox.domesticHotel.col1 > div > button')
morebtn.click()
time.sleep(1)
#boxList > li:nth-child(9) > div > div.productInfo > div:nth-child(2) > div:nth-child(1) > a > h5
list = []
for j in range(1,15):
    driver.find_element(By.CSS_SELECTOR,f'div.pageNumBox > button.nextBtn').click()
    time.sleep(1)
    product_list = driver.find_elements(By.CLASS_NAME, 'boxItem')
    for i in product_list:
        try:
            title = i.find_element(By.TAG_NAME, 'h5').text
            price = i.find_element(By.TAG_NAME, 'strong').text
            grade = i.find_element(By.CSS_SELECTOR, 'div.productInfo > div:nth-child(3) > div:nth-child(2) > p.info').text.split('평점')[1]
            list.append([title,price,grade])    
        except:
            continue
print(list)

hotel_df = pd.DataFrame(list,columns=('이름','가격','평점'))
hotel_df.to_csv('day06/travel.csv',encoding='utf-8-sig',mode='w',index=False)                   

