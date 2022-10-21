import pymysql
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd

dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = '1234'

conn = pymysql.connect( host = dbURL, port = dbPort, 
                        user = dbUser, passwd = dbPass,
                        db = 'bigdb', charset = 'utf8', use_unicode = True,
                        cursorclass=pymysql.cursors.DictCursor)

#서울 날씨 그래프
select_data = "select * from forecast where city='서울'" 
cur = conn.cursor()
cur.execute(select_data)
result = cur.fetchall()
# 한글폰트
font_name = font_manager.FontProperties(
    fname = 'c:/Windows/fonts/malgun.ttf').get_name()
matplotlib.rc('font', family = font_name)

weather_df = pd.DataFrame(result)
print(weather_df)

plt.plot(pd.to_numeric((weather_df['tmn'])),label='최저')
plt.plot(pd.to_numeric((weather_df['tmax'])),label='최고')
   
plt.legend()
plt.show()