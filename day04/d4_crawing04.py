from bs4 import BeautifulSoup
import re
import requests

r = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&date=20221011')
soup = BeautifulSoup(r.text, 'html.parser')

rank = soup.select('div.tit3')

for i in range(len(rank)):
    print((i+1),'위 : ',rank[i].get_text().strip())