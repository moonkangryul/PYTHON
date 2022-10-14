from bs4 import BeautifulSoup
import requests

r = requests.get('https://search.shopping.naver.com/book/search/category?bookTabType=NEW_BOOK&catId=50005542&pageIndex=1&pageSize=40')
soup = BeautifulSoup(r.text, 'html.parser')

#book_list > ul > li:nth-child(1) > div > a.bookListItem_info_top__VgpiO.linkAnchor > div.bookListItem_text_area__hF892 > div.bookListItem_title__X7f9_ > span > span
rank = soup.select('div.bookListItem_title__X7f9_')
print(rank)

for i in range(len(rank)):
     print((i+1),'위 : ',rank[i].get_text().strip())