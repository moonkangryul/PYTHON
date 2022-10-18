from bs4 import BeautifulSoup
import requests


codes = ['252670','251340']
datas = []

for code in codes:
    url = 'https://finance.naver.com/item/main.naver?code='+ code
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    name = soup.select_one('div.wrap_company > h2').get_text().strip()
    price = soup.select_one('em.no_up span').get_text().strip()
    
    datas.append([name,price])
print(datas, end= ' ')

 