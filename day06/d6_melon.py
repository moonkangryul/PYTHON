from selenium import webdriver as wd
from bs4 import BeautifulSoup
import requests

header = {'User-Agent':'Mozilla/5.0' }
req = requests.get('https://www.melon.com/chart/week/index.htm',headers=header)
soup = BeautifulSoup(req.text, 'html.parser')

melon = soup.select_one('div > table > tbody')

datas = []

#lst50 > td:nth-child(7) > div > div > div > a
for chart in melon.select('tr'):
    num = chart.select_one('span.rank').get_text().strip()
    name = chart.select_one('div.ellipsis.rank01 > span > a').get_text().strip()
    singer = chart.select_one('div.ellipsis.rank02 > span > a').get_text().strip()
    w = chart.select_one('td:nth-child(7) > div > div > div > a').get_text()
    datas.append([num,name,singer,w])

for i in datas:
    print(i)