from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

path = "C:\\PYTHONWORK\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-longging'])
driver = wd.Chrome(path, options=options)
driver.get('https://www.youtube.com/c/paikscuisine/videos')

all_videos = driver.find_elements(By.ID, 'dismissible')
print(all_videos)

time.sleep(2)
datas = []

#제목 재생시간 조회수
for video in all_videos:
    title = video.find_element(By.ID, 'video-title').text
    video_time = video.find_element(By.CLASS_NAME,"style-scope ytd-thumbnail-overlay-time-status-renderer").text
    video_num = video.find_element(By.CSS_SELECTOR,'span.ytd-grid-video-renderer').text
    print(title)
    print(video_num)
    print(video_time,'\n')
    
    
    datas.append([title,video_time,video_num])
print(datas)