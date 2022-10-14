from asyncio import trsock
from bs4 import BeautifulSoup
import re
import requests
from openpyxl import Workbook


r = requests.get('https://finance.naver.com/')
soup = BeautifulSoup(r.content, 'html.parser')
#container > div.aside > div > div.aside_area.aside_popular > table > tbody
finance = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular > table > tbody')

trs = finance.select('tr')

datas = []
for i in trs:
    name = i.select_one('th > a').get_text().strip()
    price = i.select_one('td').get_text().strip()
    direction = i.select_one('td > img')['alt']
    ch_updown = i.select_one('td > span').get_text().strip()
    datas.append([name,price,direction,ch_updown])

print(datas)

write_wb = Workbook()
write_ws = write_wb.create_sheet('결과')

for data in datas:
    write_ws.append(data)

write_wb.save(r'financeWork.xlsx')
