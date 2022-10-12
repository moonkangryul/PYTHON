from operator import index
from unicodedata import name

print("hello")

a = 0
print(a)
print(type (a))

b = 'hello world'
print(b)
print(type (b))


c = "\'ㅎㅇㅎㅇ\'"
print(c)

print(b+c)

print(b*3)

# b[1] = 'C' 오류발생!! 문자열은 바꿀 수 없다
print('-----------------------------\n')
print(b)
print(b[0])
print(b[-1])

e= '반갑습니다'
print(e)
print(e[0:1])
print(e.find('반'))
print(e.find('안'))  # 값이 없으면 -1 리턴
print(e.find('니'))

print(e.index('반'))
# print(e.index('안')) # 값이 없으면 오류


bb = '            ,     l      '
print(bb.lstrip())
print(bb.rstrip())
print(bb.strip())

aa = 'Now is aa bb cc'
print(aa.split())

# 리스트 (list)
l = list()
print(l,type(l))
lst = [1,2,3]
print(lst,type(lst))

l2 = [1,2,3,4,5,6,7,8,9,10,11,12]
#l2 유형 확인
print(type(l2))
#l2 첫번째 값 출력
print(l2[0])
print(len(l2),'list 길이')
print(l2[-1],'l2의 마지막 값 출력')
print(l2[len(l2)-1],'l2의 마지막 값 출력')
#l2 의 첫번째 값을 99로 수정
l2[0] = 99
print(l2)

l2[1] = [1,2,3]
print(l2)
print(len(l2))

l2[2]= '문자'
print(l2)

l2[2] = 3
print(l2)

l2.append(999)
l2.remove(5)
print(l2,'\n\n')



a1 = [1,2,3]
b1 = ['life' ,'is', 'too', 'short']
c1 = [1,2,'life','is']
d1 = [1,2,[3,4],['life','is']]

print(a1,'\n',b1,'\n',c1,'\n',d1,'\n')


print(d1[0])
print(d1[3][1])
print(d1[0:3])
d1.insert(2,'aa')
print(d1)

#튜플(tuple) 리스트처럼 수정 불가
t=tuple()
print(t,type(t))
t1=(1,2,3)
print(t1,type(t1))

t4 = (1,2,(3,4),('life','is'))
print(t4)

#dict
d = dict()
print(d,type(d))
d1 = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(d1,type(d1))
print(d1.keys())
print(d1.items())


hong = {
    'name' : 'Hong',
    'phone' : '01011112222',
    'birth' : '0814'
}

hong[1] = 'a'
hong['pet'] = 'dog'
print(hong)
print(hong['pet'])

print(hong.keys())

print(list(hong.keys()))

del hong[1]
print(hong.keys())

hong.clear()
print(hong)


#set 중복하지 않는 값만 출력
s1 = {1,2,3,4,4,4,4}
print(s1,type(s1))
s2 = set([1,2,3,4])
print(s1,type(s2))
#리스트 ,튜플 , 딕셔너리, set