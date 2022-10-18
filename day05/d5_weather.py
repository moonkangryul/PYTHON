from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd

result = []

url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

tag_tbody = soup.select_one('tbody')
           
for weather in tag_tbody.select('tr'):
            tds = weather.select('td')

            
            sido = tds[0].string
            temp = tds[5].string
            w = tds[10].string

            result.append([sido,temp,w])

weather_df = pd.DataFrame(result, columns=('지역','기온','강수'))
print(weather_df)
weather_df.to_csv('day05/weather.csv',encoding='cp949',mode='w',index=False)