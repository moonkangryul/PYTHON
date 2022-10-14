from bs4 import BeautifulSoup
import re
import requests

r = requests.get('https://news.daum.net/economic/')
soup = BeautifulSoup(r.content, 'html.parser')

# links = soup.select('a[href]')
# # print(links)

# for t in links:
#      if re.search('https://v.\w+',t['href']): # . 임의의 문자 1개
#           print(t.get_text().strip())         # \w 순자와 문자
#                                               # + 1회 이상


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

links = soup.find_all(href=re.compile(r'https://'))
# print(links)

for t in links:
          print(t.get_text().strip())

print('~'*50)


# for i in range(len(rank)):
     # print((i+1),'위 : ',rank[i].get_text().strip())
