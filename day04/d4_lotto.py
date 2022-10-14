from bs4 import BeautifulSoup
import re
import requests

r = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin')
soup = BeautifulSoup(r.content, 'html.parser')

#findall
ballNum = soup.find_all('span', class_="ball")
print(ballNum)

for i in ballNum:
     print(i.get_text(), end = ' ')

links = soup.select('div.nums > .num p .ball_645')


for i in links:
     print(i.string, end =' ')


# for t in links:
#      if re.search('ball_645 lrg ball.\w+',t['span']): # . 임의의 문자 1개
#           print(t.get_text().strip())         # \w 순자와 문자
#                                               # + 1회 이상



# for i in range(len(rank)):
     # print((i+1),'위 : ',rank[i].get_text().strip())

     