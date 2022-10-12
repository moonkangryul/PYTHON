import codecs
import re

f = codecs.open('friends101.txt','r',encoding = 'utf-8')
script101 = f.read()
print(script101[:100])
lines = re.findall(r'Monica:.+',script101)
# print(lines)
print(type(lines))
All = re.findall(r'All:.+',script101)
print(All)

print(All[-1])
print(len(All))

char = re.compile(r'[A-Z][a-z]+:')
print(re.findall(char,script101))
names = re.findall(char,script101)
print(len(set(names)))

setType = set(re.findall(char,script101))
print(type(setType))


for i in setType:
    if len(i)>7:
        print("==:",i)


character = list(setType)
print(type(character))
print(character)

character_list = []
for i in character:
    character_list += [i[:-1]]
print(character_list)

character_list2 = []
for i in character:
        character_list2.append(re.sub(':','',i))
print(character_list2,end=' ')
print()
a = '제 이메일 주소는 greate@naver.com'
a += '오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr 라는 메일을 사용합니다.'
print(a)

a1 = re.findall(r'[a-z]+@[a-z.]+',a)
print(a1)

words = ['apple','cat','brave','drama','asise','blow','coat','above']
a3 = []
for i in words:
    a3 += re.findall(r'a.+',i)
print(a3)

for i in words:
    m = re.search(r'a[a-z]+',i)
    if m:
        print(m.group(), end=' ')
print()

for i in words:
     m = re.match(r"a\D+",i)
     if m:
        print(m.group())


exam1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2022년 입니다.'
print(re.findall(r'\d+년',exam1))