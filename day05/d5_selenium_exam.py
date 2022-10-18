import re
from selenium import webdriver as wd
from bs4 import BeautifulSoup
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

path = "C:\\PYTHONWORK\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-longging'])
driver = wd.Chrome(path, options=options)
driver.get('https://www.youtube.com/c/paikscuisine/videos')

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

all_videos = soup.find_all(id='dismissible')

dict_youtubu = {'100만이상': 0,'50만이상' : 0,'10만이상' : 0 }
                    
for video in all_videos:
    video_num = video.find('span',{'class':'style-scope ytd-grid-video-renderer'}).text

    num = float(re.sub(r'[\uAC00-\uD7A3]','',video_num))

    if num > 100:
         dict_youtubu['100만이상'] += 1
    elif num > 50:
         dict_youtubu['50만이상'] += 1
    elif num > 10:
         dict_youtubu['10만이상'] += 1

print(dict_youtubu)
   

# 한글폰트
font_name = mpl.font_manager.FontProperties(
    fname = 'c:/Windows/fonts/malgun.ttf').get_name()

mpl.rc('font', family = font_name)
figure = plt.figure()
axes = figure.add_subplot(111) #(행,열,순서)
axes.pie(dict_youtubu.values(),labels=dict_youtubu.keys(), autopct='%.1f%%')
plt.show()