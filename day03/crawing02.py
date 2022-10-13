import imp
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)
print(res)

soup = BeautifulSoup(res, 'html.parser')
# title = soup.channel.title.string
# print(title)
title = soup.find('title').string
print(title)

wf = soup.find('wf').string
print(wf)