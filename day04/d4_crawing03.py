from bs4 import BeautifulSoup
import re
import requests

r = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&date=20221011')
soup = BeautifulSoup(r.text, 'html.parser')

# txt = r.text #텍스트 형식으로 데이터 추출
# print(txt)

# bin = r.content #바이너리 형식으로 데이터 추출
# print(bin)


#old_content > table > tbody > tr:nth-child(3) > td.title > div > a
rank = soup.select('#old_content > table > tbody > tr > td.title > div > a')
for i in rank:
    print(i.string)

# html = """
#     <ul>
#     <li><a href="hoge.html">hoge</li>
#     <li><a href="https://example.com/fuga">fuga*</li>
#     <li><a href="https://example.com/foo>foo*</li>
#     <li><a href="shttps://example.com/foobbb>foobbb*</li>
#     <li><a href="https://example.com/aaa>aaa</li>
#     </ul>
# """



lis = soup.find_all(href=re.compile(r'https://'))
# print(lis)

# lis1 = soup.find_all(href=re.compile(r'^https://'))
# print(lis1)


# for e in lis1:
#     print(e.attrs['href'])