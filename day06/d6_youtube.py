
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = "C:\\PYTHONWORK\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-longging'])
driver = wd.Chrome(path, options=options)
driver.get('https://www.youtube.com/c/paikscuisine/videos')

all_videos = driver.find_elements(By.ID,'dismissible')
body_tag = driver.find_element(By.TAG_NAME, 'body')

body_tag.send_keys(Keys.END) #스크롤이 1번 진행된다

#화면 길이 확인하기
# Document.documentElement.scrollHeight: 화면 길이
print(driver.execute_script('return document.documentElement.scrollHeight'))

while True:
    last_height =driver.execute_script('return document.documentElement.scrollHeight')

    for i in range(10):
        body_tag.send_keys(Keys.END)
        time.sleep(1)
    new_height = driver.execute_script('return document.documentElement.scrollHeight')

    if last_height == new_height:
        print('화면 길이 같아서 반복 종료')
        break