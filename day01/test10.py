import pandas as pd

#1번
str = '20201231Thursday'
print(str[:4])
print(str[4:8])
print(str[8:])

#2번
a = ['쓰','레','기','통']
a.reverse()
print(a)

#3번
dic = {
    'year': 2020,  
    'mm': 12, 
    'dd' :31, 
    'day':'Thursday',
    'weather':'snow'
    }
print(dic.keys())
print(dic.values())

#5번
i=0
for i in range(1,6):
    for j in range(i):
        print('*',end ='')
    print()


#6번
def avg(*a):
    sum=0
    for i in a:
        sum += i
    return sum/len(a)

print(avg(5,3,12,9))
print(avg(2.4, 3.2, 7.3))
print(avg(10,5))


df2 = pd.DataFrame([
    [500, 450, 520, 610],
    [690, 700, 820, 900],
    [1100, 1030, 1200, 1380],
    [1500, 1650, 1700, 1850],
    [1990, 2020, 2300, 2420],
    [1020, 1600, 2200, 2550]
], index=['2015','2016','2017','2018','2019','2020'], columns=['1분기','2분기','3분기','4분기'])
df2.to_csv('C:\PYTHONWORK\score2.csv', header='False',encoding='utf8')

df2 = pd.read_csv('C:\PYTHONWORK\score2.csv',encoding='utf-8')
print(df2)