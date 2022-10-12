
import numpy as np
import pandas as pd

# print(np.__version__)

ar4 = np.array([1,2,3,4,5,6]).reshape(3,2)
print(ar4)

ar5 = np.zeros((2,3))
print(ar5)

ar1 = np.array([1,2,3,4,5,6])
ar8 = ar1+10
print(ar8)

ar9 = ar1*10
print(ar9)


data1 = [10,20,30,40,50]
print(data1)
data2 = ['10!','20!','30!','40!','50!']
print(data2)
sr1 = pd.Series(data1)
print(sr1)
sr2 = pd.Series(data2)
print(sr2)

data_dic={
    'year':[2018,2019,2020],
    'sales':[350,600,700]
}

print(data_dic)
df1 = pd.DataFrame(data_dic)
print(df1)

df2 = pd.DataFrame([
    [89.2, 92.5, 90.8],[82.2,90.5,96.8]
],index=['중간고사','기말고사'],columns=['국어','영어','수학'])
print(df2)
print('-----------------------------')
print(df2.head())
print(df2.head(1))
print('-----------------------------')

print(df2.tail())
print(df2.tail(1))
print('-----------------------------')
print(df2['국어'])
print(df2.영어)
print('-----------------------------')

# df2.to_csv('c:/test/score.csv',header='False')
df3 = pd.read_csv('c:/test/score.csv',encoding='utf-8')
print(df3)


