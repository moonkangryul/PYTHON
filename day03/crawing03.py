from bs4 import BeautifulSoup

html = """
    <html><body>
    <h1>위키북스 도서2</h1>
        <div id = "meigen">
            <h1>위키북스 도서</h1>
            <ul class = "items">
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인의 정석</li>
            </ul>
        </div>
        <div>
            <h1>위키북스 도서</h1>
            ...
        </div>
    </body></html>

"""
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.find('h1').string
print(h1)

h1_1 = soup.select_one('h1').string
print(h1_1)

h1_2 = soup.select_one('div > h1').string
print(h1_2)

h1_3 = soup.select_one('div#meigen > h1').string
print(h1_3)

li = soup.select('ul.items > li')
print(li)

for i in li:
    print(i.string)