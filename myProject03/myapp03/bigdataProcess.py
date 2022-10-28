from bs4 import BeautifulSoup
import requests
from django.db import models
from django.shortcuts import render
import re
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
from myProject03.settings import STATIC_DIR
import os


def weather_crawing(last_date, weather):

    data = requests.get(
        'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108')

    html = data.text
    print(html)
    soup = BeautifulSoup(html, 'lxml')

    # 딕을 하나 만들고
    for i in soup.find_all('location'):
        # 키갑하나에 벨류가 13개 들어감
        weather[i.find('city').text] = []
        for j in i.find_all('data'):
            temp = []
            if (len(last_date) == 0) or (j.find('tmef').text > last_date[0]['tmef']):
                temp.append(j.find('tmef').text)
                temp.append(j.find('wf').text)
                temp.append(j.find('tmn').text)
                temp.append(j.find('tmx').text)
                weather[i.find('city').string].append(temp)
    weather[i.find('city').string].append(temp)


def weather_make_chart(result,wfs,dcounts):
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)

    high = []
    low = []
    xdata = []

    for row in result.values_list():
        high.append(row[5])
        low.append(row[4])
        xdata.append(row[2].split('-')[2])

    plt.cla()
    plt.figure(figsize=(10, 6))
    plt.plot(xdata, low, label='최저기온')
    plt.plot(xdata, high, label='최고기온')
    plt.legend()
    plt.savefig(os.path.join(
        STATIC_DIR, 'images\\weather_busan.png'), dpi=300)

    plt.cla()
    plt.bar(wfs, dcounts)
    plt.savefig(os.path.join(
        STATIC_DIR, 'images\\weather_bar.png'), dpi=300)

    plt.cla()
    plt.pie(dcounts, labels=wfs, autopct='%.1f%%')
    plt.savefig(os.path.join(
        STATIC_DIR, 'images\\weather_pie.png'), dpi=300)


# 여러개의 이미지를 넣을려고 딕 만듦
    image_dic = {
        'plot':  'weather_busan.png',
        'bar':  'weather_bar.png',
        'pie':  'weather_pie.png'
    }
    return image_dic




def melon_crawing(datas):
    header = {'User-Agent':'Mozilla/5.0' }
    req = requests.get('https://www.melon.com/chart/week/index.htm',headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')

    melon = soup.select_one('div > table > tbody')


    for chart in melon.select('tr'):
        rank = chart.select_one('span.rank').get_text().strip()
        Music = re.sub('\n','',chart.select_one('div.ellipsis.rank01 > span > a').get_text().strip())
        singer = re.sub('\n','',chart.select_one('div.ellipsis.rank02 > span > a').get_text().strip())
        album = chart.select_one('td:nth-child(7) > div > div > div > a').get_text()
 
        tmp ={'rank':rank,
              'Music':Music,
              'singer':singer,
              'album':album}
        datas.append(tmp)
    
    


  