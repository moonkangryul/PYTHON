import usecsv,re,csv

ap = usecsv.opencsv('day03/apt_201910.csv')
apt = usecsv.switchcsv(ap)


print(apt[:3])
print(len(apt))

for i in apt[:6]:
    print(i[0],i[4],i[-4])

# 강원도에 120m² 이상 3억 이하 검색하기 시군구 단지명 가격 출력

new_list=['시군구','단지명','가격']

for i in apt:
    try:
        if i[5] >= 120 and i[-4] <= 30000 and re.match('강원',i[0]):
            new_list.append([i[0],i[5],i[-4]])
    except:
        pass
    
print(new_list)

with open('apt11.csv','w',newline = '') as f:
    a = csv.writer(f,delimiter=',')
    a.writerows(new_list)