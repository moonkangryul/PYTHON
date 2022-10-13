from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"

res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')
# ul@exchangeList > li > a.head > div
head = soup.select_one('ul#exchangeList > li > a.head > div')
print(head)

value = soup.select_one('span.value').string
print('value : ',value)

#exchangeList > li:nth-child(1) > a.head.usd > div

txt1 = soup.select_one('div.head_info')
print(txt1)
print(txt1.select('span')[0].string)
print(txt1.select('span')[1].string)
print(txt1.select('span')[2].string)
print(txt1.select('span')[3].string)

txt2 = head.select('span')
print(txt2)

for sp in txt2:
    print(sp.string)
#exchangeList > li.on > a.head.usd > div > span.value
price = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').string
print(price)

updown = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.blind').string
print(updown)