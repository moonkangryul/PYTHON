import csv
import re
import pandas as pd

f = open('popSeoul.csv','r')
reader = csv.reader(f)
# print(reader)

output = []

# for i in reader:/
    # output.append(i)
    # print(output)
    # for j in i:
        
# 숫자만 읽어와서 , 를 제거하고 float 형태로 변환하여 output에 추가


for i in reader:
    temp = []
    for j in i:
        try:
            if re.search('\d',j):
                temp.append(float(re.sub(',','', j)))
            else:
                temp.append(j)
        except:
            pass
    output.append(temp)
print(output)


# 구 한국인 외국인 외국인 비율

ko_fo = []
for i in output:
    try:
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        if foreign > 5:
            ko_fo.append([i[0],i[1],i[2],foreign])
    except:
        pass
    
print(ko_fo)