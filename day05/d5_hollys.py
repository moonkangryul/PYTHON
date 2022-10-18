from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd

result = []

def hollys_store(result):
    for i in range(1,6):
        url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d' %i
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        #contents > div.content > fieldset > div.tableType01 > table > tbody
        tag_tbody = soup.select_one('tbody')
        
        for store in tag_tbody.select('tr'):
            tds = store.select('td')
            sido = tds[0].string
            name = tds[1].string
            address = tds[3].string
            phone = tds[5].string
            result.append([sido,name,address,phone])
    return

hollys_store(result)

hollys_df = pd.DataFrame(result, columns=('store','sido','address','phone'))
print(hollys_df)
hollys_df.to_csv('day05/hollys.csv',encoding='cp949',mode='w',index=True)