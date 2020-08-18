import pandas as pd
import numpy as np
import csv

data16=pd.read_csv('./dataframe16.csv',index_col='경기날짜') #데이터프레임의 순서를 지우고 오직 인덱스로만 표시
data17=pd.read_csv('./dataframe17.csv',index_col='경기날짜')
data18=pd.read_csv('./dataframe18.csv',index_col='경기날짜')
data19=pd.read_csv('./dataframe19.csv',index_col='경기날짜')
data20=pd.read_csv('./dataframe20.csv',index_col='경기날짜')
dataframe=pd.concat([data16,data17,data18,data19,data20],axis=0, keys=['2016년','2017년','2018년','2019년','2020년'])

print(data16)

dataframe.to_csv('./totaldataframe.csv',encoding='utf-8')
dataframe.to_csv('./totaldataframexl.csv',encoding='ANSI')