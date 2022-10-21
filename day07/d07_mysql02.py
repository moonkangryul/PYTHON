import pymysql
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = '1234'

conn = pymysql.connect( host = dbURL, port = dbPort, 
                        user = dbUser, passwd = dbPass,
                        db = 'bigdb', charset = 'utf8', use_unicode = True)

#부산 날씨
#select_data = "select * from forecast where city='부산' order by tmef desc" 
# cur = conn.cursor()
# cur.execute(select_data)
# result = cur.fetchall()

# datas = []
# for row in result:
#     datas.append([row[2],row[4],row[5]])

# print(datas)
# #부산 최저기온 최고기온
# select_data2 = "select max(tmax),min(tmn) from forecast where city='부산'" 
# cur.execute(select_data2)
# result2 = cur.fetchone()
# print(result2)

# # for row in result:
# #     datas.append([row[5],row[3],row[4]])
# # print(datas)

#서울 날씨 그래프
select_data = "select * from forecast where city='부산'" 
cur = conn.cursor()
cur.execute(select_data)
result = cur.fetchall()
# 한글폰트
font_name = font_manager.FontProperties(
    fname = 'c:/Windows/fonts/malgun.ttf').get_name()
matplotlib.rc('font', family = font_name)

high = []
low = []
xdata = []
whState = []

#num,city,wf,tmn,tmax,tmef
for row in result:
    high.append(float(row[4])) #최고
    low.append(float(row[3])) #최저
    whState.append(row[2]) #날씨 상태
    xdata.append(row[5].split('-')[2]) #가로축

plt.figure(figsize=(15,6)) #그래프 크기
plt.plot(xdata,low,label='최저')
plt.plot(xdata,high,label='최고')
plt.title(result[0][5].split('-')[1]+"월") #타이틀

plt.legend()
plt.show()


#bar
select_data1 = "select wf, count(*) from forecast where city='부산' group by wf"
cur = conn.cursor()
cur.execute(select_data1)
result1 = cur.fetchall()

whData = []
whDataCount = []

for row in result1:
    whData.append(row[0])
    whDataCount.append(row[1])

plt.bar(whData,whDataCount)
plt.show()

#pie
plt.pie(whDataCount,labels=whData,autopct='%.1f%%')
plt.show()
