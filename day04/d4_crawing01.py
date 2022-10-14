from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li a
#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a

#후손 : li a
#자식 : li > b > a
wiki_list = soup.select('#mw-content-text > div.mw-parser-output > ul > li a')
print(wiki_list)

for i in wiki_list:
    print(i.string)