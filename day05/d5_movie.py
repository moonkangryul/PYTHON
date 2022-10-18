from bs4 import BeautifulSoup
import requests

url = 'https://movie.daum.net/ranking/reservation'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
#mainContent > div > div.box_ranking > ol
movie = soup.select('ol div.thumb_cont')

datas =[]

for i in movie:
    name = i.select_one('a.link_txt').get_text().strip()
    grade = i.select_one('span.txt_grade').get_text().strip()
    num = i.select_one('span.txt_num').get_text().strip()
    datas.append([name,grade,num])
    
    print('제목: ', name)
    print('평점: ', grade )
    print('예매율: ', num ,'\n')