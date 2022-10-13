from operator import index
import pandas as pd

#survey.csv 읽어서 위에서 5개 출력

d = pd.read_csv('day03/survey.csv',encoding='utf-8')
print(d.head())

#평균
print(d.mean())

#수입 평균(반올림해서 소수점 1자리까지 표현)
print('수입의 평균 : ', round(d.income.mean(),1))
print('수입의 합계 : ', d.income.sum())
print('수입의 중앙값 : ', d.income.median())
print(d.income.describe())
print(d.sex.value_counts())

