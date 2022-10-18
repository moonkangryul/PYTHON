from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt




df = pd.read_csv('day05/weather.csv',encoding='cp949',index_col='지역')
print(df)


#서울, 인천, 부산 데이터 출력
city_df = df.loc[['서울', '인천', '부산', '대전', '대구', '광주', '울산']]


# 한글폰트
font_name = mpl.font_manager.FontProperties(
    fname = 'c:/Windows/fonts/malgun.ttf').get_name()

mpl.rc('font', family = font_name)

ax = city_df.plot(kind ='bar',title='날씨',figsize=(12,7),legend=True,fontsize=12)
ax.set_xlabel('도시',fontsize=12)
ax.set_ylabel('기온/습도',fontsize=12)
ax.legend(['기온','습도'],fontsize=12)
plt.show()