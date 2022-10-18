from selenium import webdriver as wd
from bs4 import BeautifulSoup
import pandas as pd

path = "C:\\PYTHONWORK\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-longging'])
driver = wd.Chrome(path, options=options)
driver.get('https://www.youtube.com/c/paikscuisine/videos')

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

all_videos = soup.find_all(id='dismissible')
datas = []

for video in all_videos:
    title = video.find(id='video-title').text
    video_time = video.find('span',class_="style-scope ytd-thumbnail-overlay-time-status-renderer").text
    video_num = video.find('span',{'class':'style-scope ytd-grid-video-renderer'}).text
    datas.append([title,video_time,video_num])
print(datas)

youtube_df = pd.DataFrame(datas , columns=('제목','시간','조회수'))
print(youtube_df)
youtube_df.to_csv('day05/youtube.csv',encoding='utf-8-sig',mode='w',index=True)