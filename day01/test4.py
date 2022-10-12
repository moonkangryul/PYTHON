import re

text = "<title>지금은 문자열 연습입니다..</title>"

print(text[0:7])
print(text.find('문'))
print(text.find('파'))
#print(text.index('파'))


text1 = "       <title>지금은 문자열 연습입니다..</title>       "
text2 = ";"

print(text1.strip(),text2)
print(text1.lstrip(),text2)
print(text1.rstrip(),text2)
print(text1.replace('title','div'))
print(text1.replace('<title>',''))

text3 = ('111<head>안녕하세요</head>22')
body = re.search('<head.*/head>',text3)
print(body)

body = body.group()
print(body)

#[0-9] [a-z]
#ab*c : abc, abbc ,abbbbc, abbbbbbc // * <- 값이 0이상
# *(0이상), +(1이상), ?(0이상1이하)
print("-------------------------------------------")
text4 = ('<head>안녕하세요....<title>지금은 문자열 연습입니다..</title></head>')
d = re.search('<title.*/title>',text4)
d = d.  group()
print(d)

print("-------------------------------------------")

d = re.sub('<.+?>','',text4)
print(d)











#여긴 #내 자리
#삭제 금지
#오늘 점심은 샐러드
#언니 뭐 먹고 싶어요 #돼지국밥