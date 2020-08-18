import pandas as pd
import numpy as np
import csv

teamdata19=pd.read_csv('./팀타자19.csv')
teamdata19=teamdata19[['GDAY_DS','T_ID','HIT','AB']]
teamdata19=teamdata19.sort_values(['GDAY_DS','T_ID'])
#team=['SK','KT','LT','HH','SS','LG','HT','WO','OB','NC']
hhteam1904 = open('./hhteam1904.csv', 'w',encoding='utf-8',newline='')
skteam1904 = open('./skteam1904.csv', 'w',encoding='utf-8',newline='')
ktteam1904 = open('./ktteam1904.csv', 'w',encoding='utf-8',newline='')
ltteam1904 = open('./ltteam1904.csv', 'w',encoding='utf-8',newline='')
ssteam1904 = open('./ssteam1904.csv', 'w',encoding='utf-8',newline='')
lgteam1904 = open('./lgteam1904.csv', 'w',encoding='utf-8',newline='')
htteam1904 = open('./htteam1904.csv', 'w',encoding='utf-8',newline='')
woteam1904 = open('./woteam1904.csv', 'w',encoding='utf-8',newline='')
obteam1904 = open('./obteam1904.csv', 'w',encoding='utf-8',newline='')
ncteam1904 = open('./ncteam1904.csv', 'w',encoding='utf-8',newline='')
wr=csv.writer(hhteam1904)
wr1=csv.writer(skteam1904)
wr2=csv.writer(ktteam1904)
wr3=csv.writer(ltteam1904)
wr4=csv.writer(ssteam1904)
wr5=csv.writer(lgteam1904)
wr6=csv.writer(htteam1904)
wr7=csv.writer(woteam1904)
wr8=csv.writer(obteam1904)
wr9=csv.writer(ncteam1904)

wr.writerow(['4월 한화 타수','4월 한화 안타'])
for day in pd.date_range('2019-04-01', '2019-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr.writerow([daynum,hhab,hhhit])

hhteam1904.close()

wr1.writerow(['4월 SK 타수','4월 SK 안타'])
for day in pd.date_range('2019-04-01', '2019-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr1.writerow([skab,skhit])
skteam1904.close()

wr2.writerow(['4월 KT 타수','4월 KT 안타'])
for day in pd.date_range('2019-04-01', '2019-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr2.writerow([ktab,kthit])
ktteam1904.close()

wr3.writerow(['4월 롯데 타수','4월 롯데 안타'])
for day in pd.date_range('2019-04-01', '2019-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr3.writerow([ltab,lthit])
ltteam1904.close()

wr4.writerow(['4월 삼성 타수','4월 삼성 안타'])
for day in pd.date_range('2019-04-01', '2019-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr4.writerow([ssab,sshit])
ssteam1904.close()

wr5.writerow(['4월 엘지 타수','4월 엘지 안타'])
for day in pd.date_range('2019-04-01', '2019-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr5.writerow([lgab,lghit])
lgteam1904.close()

wr6.writerow(['4월 기아 타수','4월 기아 안타'])
for day in pd.date_range('2019-04-01', '2019-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr6.writerow([htab,hthit])
htteam1904.close()

wr7.writerow(['4월 키움 타수','4월 키움 안타'])
for day in pd.date_range('2019-04-01', '2019-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr7.writerow([woab,wohit])
woteam1904.close()

wr8.writerow(['4월 두산 타수','4월 두산 안타'])
for day in pd.date_range('2019-04-01', '2019-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr8.writerow([obab,obhit])
obteam1904.close()

wr9.writerow(['4월 넥센 타수','4월 넥센 안타'])
for day in pd.date_range('2019-04-01', '2019-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr9.writerow([ncab,nchit])
ncteam1904.close()

hhteam1905 = open('./hhteam1905.csv', 'w',encoding='utf-8',newline='')
skteam1905 = open('./skteam1905.csv', 'w',encoding='utf-8',newline='')
ktteam1905 = open('./ktteam1905.csv', 'w',encoding='utf-8',newline='')
ltteam1905 = open('./ltteam1905.csv', 'w',encoding='utf-8',newline='')
ssteam1905 = open('./ssteam1905.csv', 'w',encoding='utf-8',newline='')
lgteam1905 = open('./lgteam1905.csv', 'w',encoding='utf-8',newline='')
htteam1905 = open('./htteam1905.csv', 'w',encoding='utf-8',newline='')
woteam1905 = open('./woteam1905.csv', 'w',encoding='utf-8',newline='')
obteam1905 = open('./obteam1905.csv', 'w',encoding='utf-8',newline='')
ncteam1905 = open('./ncteam1905.csv', 'w',encoding='utf-8',newline='')
wr10=csv.writer(hhteam1905)
wr11=csv.writer(skteam1905)
wr12=csv.writer(ktteam1905)
wr13=csv.writer(ltteam1905)
wr14=csv.writer(ssteam1905)
wr15=csv.writer(lgteam1905)
wr16=csv.writer(htteam1905)
wr17=csv.writer(woteam1905)
wr18=csv.writer(obteam1905)
wr19=csv.writer(ncteam1905)

wr10.writerow(['5월 한화 타수','5월 한화 안타'])
for day in pd.date_range('2019-05-01', '2019-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr10.writerow([hhab,hhhit])
hhteam1905.close()

wr11.writerow(['5월 SK 타수','5월 SK 안타'])
for day in pd.date_range('2019-05-01', '2019-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr11.writerow([skab,skhit])
skteam1905.close()

wr12.writerow(['5월 KT 타수','5월 KT 안타'])
for day in pd.date_range('2019-05-01', '2019-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr12.writerow([ktab,kthit])
ktteam1905.close()

wr13.writerow(['5월 롯데 타수','5월 롯데 안타'])
for day in pd.date_range('2019-05-01', '2019-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr13.writerow([ltab,lthit])
ltteam1905.close()

wr14.writerow(['5월 삼성 타수','5월 삼성 안타'])
for day in pd.date_range('2019-05-01', '2019-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr14.writerow([ssab,sshit])
ssteam1905.close()

wr15.writerow(['5월 엘지 타수','5월 엘지 안타'])
for day in pd.date_range('2019-05-01', '2019-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr15.writerow([lgab,lghit])
lgteam1905.close()

wr16.writerow(['5월 기아 타수','5월 기아 안타'])
for day in pd.date_range('2019-05-01', '2019-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr16.writerow([htab,hthit])
htteam1905.close()

wr17.writerow(['5월 키움 타수','5월 키움 안타'])
for day in pd.date_range('2019-05-01', '2019-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr17.writerow([woab,wohit])
woteam1905.close()

wr18.writerow(['5월 두산 타수','5월 두산 안타'])
for day in pd.date_range('2019-05-01', '2019-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr18.writerow([obab,obhit])
obteam1905.close()

wr19.writerow(['5월 넥센 타수','5월 넥센 안타'])
for day in pd.date_range('2019-05-01', '2019-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr19.writerow([ncab,nchit])
ncteam1905.close()

hhteam1906 = open('./hhteam1906.csv', 'w',encoding='utf-8',newline='')
skteam1906 = open('./skteam1906.csv', 'w',encoding='utf-8',newline='')
ktteam1906 = open('./ktteam1906.csv', 'w',encoding='utf-8',newline='')
ltteam1906 = open('./ltteam1906.csv', 'w',encoding='utf-8',newline='')
ssteam1906 = open('./ssteam1906.csv', 'w',encoding='utf-8',newline='')
lgteam1906 = open('./lgteam1906.csv', 'w',encoding='utf-8',newline='')
htteam1906 = open('./htteam1906.csv', 'w',encoding='utf-8',newline='')
woteam1906 = open('./woteam1906.csv', 'w',encoding='utf-8',newline='')
obteam1906 = open('./obteam1906.csv', 'w',encoding='utf-8',newline='')
ncteam1906 = open('./ncteam1906.csv', 'w',encoding='utf-8',newline='')
wr20=csv.writer(hhteam1906)
wr21=csv.writer(skteam1906)
wr22=csv.writer(ktteam1906)
wr23=csv.writer(ltteam1906)
wr24=csv.writer(ssteam1906)
wr25=csv.writer(lgteam1906)
wr26=csv.writer(htteam1906)
wr27=csv.writer(woteam1906)
wr28=csv.writer(obteam1906)
wr29=csv.writer(ncteam1906)

wr20.writerow(['6월 한화 타수','6월 한화 안타'])
for day in pd.date_range('2019-06-01', '2019-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr20.writerow([hhab,hhhit])
hhteam1906.close()

wr21.writerow(['6월 SK 타수','6월 SK 안타'])
for day in pd.date_range('2019-06-01', '2019-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr21.writerow([skab,skhit])
skteam1906.close()

wr22.writerow(['6월 KT 타수','6월 KT 안타'])
for day in pd.date_range('2019-06-01', '2019-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr22.writerow([ktab,kthit])
ktteam1906.close()

wr23.writerow(['6월 롯데 타수','6월 롯데 안타'])
for day in pd.date_range('2019-06-01', '2019-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr23.writerow([ltab,lthit])
ltteam1906.close()

wr24.writerow(['6월 삼성 타수','6월 삼성 안타'])
for day in pd.date_range('2019-06-01', '2019-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr24.writerow([ssab,sshit])
ssteam1906.close()

wr25.writerow(['6월 엘지 타수','6월 엘지 안타'])
for day in pd.date_range('2019-06-01', '2019-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr25.writerow([lgab,lghit])
lgteam1906.close()

wr26.writerow(['6월 기아 타수','6월 기아 안타'])
for day in pd.date_range('2019-06-01', '2019-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr26.writerow([htab,hthit])
htteam1906.close()

wr27.writerow(['6월 키움 타수','6월 키움 안타'])
for day in pd.date_range('2019-06-01', '2019-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr27.writerow([woab,wohit])
woteam1906.close()

wr28.writerow(['6월 두산 타수','6월 두산 안타'])
for day in pd.date_range('2019-06-01', '2019-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr28.writerow([obab,obhit])
obteam1906.close()

wr29.writerow(['6월 넥센 타수','6월 넥센 안타'])
for day in pd.date_range('2019-06-01', '2019-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr29.writerow([ncab,nchit])
ncteam1906.close()

hhteam1907 = open('./hhteam1907.csv', 'w',encoding='utf-8',newline='')
skteam1907 = open('./skteam1907.csv', 'w',encoding='utf-8',newline='')
ktteam1907 = open('./ktteam1907.csv', 'w',encoding='utf-8',newline='')
ltteam1907 = open('./ltteam1907.csv', 'w',encoding='utf-8',newline='')
ssteam1907 = open('./ssteam1907.csv', 'w',encoding='utf-8',newline='')
lgteam1907 = open('./lgteam1907.csv', 'w',encoding='utf-8',newline='')
htteam1907 = open('./htteam1907.csv', 'w',encoding='utf-8',newline='')
woteam1907 = open('./woteam1907.csv', 'w',encoding='utf-8',newline='')
obteam1907 = open('./obteam1907.csv', 'w',encoding='utf-8',newline='')
ncteam1907 = open('./ncteam1907.csv', 'w',encoding='utf-8',newline='')
wr30=csv.writer(hhteam1907)
wr31=csv.writer(skteam1907)
wr32=csv.writer(ktteam1907)
wr33=csv.writer(ltteam1907)
wr34=csv.writer(ssteam1907)
wr35=csv.writer(lgteam1907)
wr36=csv.writer(htteam1907)
wr37=csv.writer(woteam1907)
wr38=csv.writer(obteam1907)
wr39=csv.writer(ncteam1907)

wr30.writerow(['7월 한화 타수','7월 한화 안타'])
for day in pd.date_range('2019-07-01', '2019-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr30.writerow([hhab,hhhit])
hhteam1907.close()

wr31.writerow(['7월 SK 타수','7월 SK 안타'])
for day in pd.date_range('2019-07-01', '2019-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr31.writerow([skab,skhit])
skteam1907.close()

wr32.writerow(['7월 KT 타수','7월 KT 안타'])
for day in pd.date_range('2019-07-01', '2019-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr32.writerow([ktab,kthit])
ktteam1907.close()

wr33.writerow(['7월 롯데 타수','7월 롯데 안타'])
for day in pd.date_range('2019-07-01', '2019-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr33.writerow([ltab,lthit])
ltteam1907.close()

wr34.writerow(['7월 삼성 타수','7월 삼성 안타'])
for day in pd.date_range('2019-07-01', '2019-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr34.writerow([ssab,sshit])
ssteam1907.close()

wr35.writerow(['7월 엘지 타수','7월 엘지 안타'])
for day in pd.date_range('2019-07-01', '2019-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr35.writerow([lgab,lghit])
lgteam1907.close()

wr36.writerow(['7월 기아 타수','7월 기아 안타'])
for day in pd.date_range('2019-07-01', '2019-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr36.writerow([htab,hthit])
htteam1907.close()

wr37.writerow(['7월 키움 타수','7월 키움 안타'])
for day in pd.date_range('2019-07-01', '2019-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr37.writerow([woab,wohit])
woteam1907.close()

wr38.writerow(['7월 두산 타수','7월 두산 안타'])
for day in pd.date_range('2019-07-01', '2019-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr38.writerow([obab,obhit])
obteam1907.close()

wr39.writerow(['7월 넥센 타수','7월 넥센 안타'])
for day in pd.date_range('2019-07-01', '2019-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr39.writerow([ncab,nchit])
ncteam1907.close()

hhteam1908 = open('./hhteam1908.csv', 'w',encoding='utf-8',newline='')
skteam1908 = open('./skteam1908.csv', 'w',encoding='utf-8',newline='')
ktteam1908 = open('./ktteam1908.csv', 'w',encoding='utf-8',newline='')
ltteam1908 = open('./ltteam1908.csv', 'w',encoding='utf-8',newline='')
ssteam1908 = open('./ssteam1908.csv', 'w',encoding='utf-8',newline='')
lgteam1908 = open('./lgteam1908.csv', 'w',encoding='utf-8',newline='')
htteam1908 = open('./htteam1908.csv', 'w',encoding='utf-8',newline='')
woteam1908 = open('./woteam1908.csv', 'w',encoding='utf-8',newline='')
obteam1908 = open('./obteam1908.csv', 'w',encoding='utf-8',newline='')
ncteam1908 = open('./ncteam1908.csv', 'w',encoding='utf-8',newline='')
wr40=csv.writer(hhteam1908)
wr41=csv.writer(skteam1908)
wr42=csv.writer(ktteam1908)
wr43=csv.writer(ltteam1908)
wr44=csv.writer(ssteam1908)
wr45=csv.writer(lgteam1908)
wr46=csv.writer(htteam1908)
wr47=csv.writer(woteam1908)
wr48=csv.writer(obteam1908)
wr49=csv.writer(ncteam1908)

wr40.writerow(['8월 한화 타수','8월 한화 안타'])
for day in pd.date_range('2019-08-01', '2019-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr40.writerow([hhab,hhhit])
hhteam1908.close()

wr41.writerow(['8월 SK 타수','8월 SK 안타'])
for day in pd.date_range('2019-08-01', '2019-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr41.writerow([skab,skhit])
skteam1908.close()

wr42.writerow(['8월 KT 타수','8월 KT 안타'])
for day in pd.date_range('2019-08-01', '2019-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr42.writerow([ktab,kthit])
ktteam1908.close()

wr43.writerow(['8월 롯데 타수','8월 롯데 안타'])
for day in pd.date_range('2019-08-01', '2019-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr43.writerow([ltab,lthit])
ltteam1908.close()

wr44.writerow(['8월 삼성 타수','8월 삼성 안타'])
for day in pd.date_range('2019-08-01', '2019-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr44.writerow([ssab,sshit])
ssteam1908.close()

wr45.writerow(['8월 엘지 타수','8월 엘지 안타'])
for day in pd.date_range('2019-08-01', '2019-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr45.writerow([lgab,lghit])
lgteam1908.close()

wr46.writerow(['8월 기아 타수','8월 기아 안타'])
for day in pd.date_range('2019-08-01', '2019-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr46.writerow([htab,hthit])
htteam1908.close()

wr47.writerow(['8월 키움 타수','8월 키움 안타'])
for day in pd.date_range('2019-08-01', '2019-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr47.writerow([woab,wohit])
woteam1908.close()

wr48.writerow(['8월 두산 타수','8월 두산 안타'])
for day in pd.date_range('2019-08-01', '2019-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr48.writerow([obab,obhit])
obteam1908.close()

wr49.writerow(['8월 넥센 타수','8월 넥센 안타'])
for day in pd.date_range('2019-08-01', '2019-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr49.writerow([ncab,nchit])
ncteam1908.close()

hhteam1909 = open('./hhteam1909.csv', 'w',encoding='utf-8',newline='')
skteam1909 = open('./skteam1909.csv', 'w',encoding='utf-8',newline='')
ktteam1909 = open('./ktteam1909.csv', 'w',encoding='utf-8',newline='')
ltteam1909 = open('./ltteam1909.csv', 'w',encoding='utf-8',newline='')
ssteam1909 = open('./ssteam1909.csv', 'w',encoding='utf-8',newline='')
lgteam1909 = open('./lgteam1909.csv', 'w',encoding='utf-8',newline='')
htteam1909 = open('./htteam1909.csv', 'w',encoding='utf-8',newline='')
woteam1909 = open('./woteam1909.csv', 'w',encoding='utf-8',newline='')
obteam1909 = open('./obteam1909.csv', 'w',encoding='utf-8',newline='')
ncteam1909 = open('./ncteam1909.csv', 'w',encoding='utf-8',newline='')
wr50=csv.writer(hhteam1909)
wr51=csv.writer(skteam1909)
wr52=csv.writer(ktteam1909)
wr53=csv.writer(ltteam1909)
wr54=csv.writer(ssteam1909)
wr55=csv.writer(lgteam1909)
wr56=csv.writer(htteam1909)
wr57=csv.writer(woteam1909)
wr58=csv.writer(obteam1909)
wr59=csv.writer(ncteam1909)

wr50.writerow(['9월 한화 타수','9월 한화 안타'])
for day in pd.date_range('2019-09-01', '2019-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr50.writerow([hhab,hhhit])
hhteam1909.close()

wr51.writerow(['9월 SK 타수','9월 SK 안타'])
for day in pd.date_range('2019-09-01', '2019-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr51.writerow([skab,skhit])
skteam1909.close()

wr52.writerow(['9월 KT 타수','9월 KT 안타'])
for day in pd.date_range('2019-09-01', '2019-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr52.writerow([ktab,kthit])
ktteam1909.close()

wr53.writerow(['9월 롯데 타수','9월 롯데 안타'])
for day in pd.date_range('2019-09-01', '2019-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr53.writerow([ltab,lthit])
ltteam1909.close()

wr54.writerow(['9월 삼성 타수','9월 삼성 안타'])
for day in pd.date_range('2019-09-01', '2019-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr54.writerow([ssab,sshit])
ssteam1909.close()

wr55.writerow(['9월 엘지 타수','9월 엘지 안타'])
for day in pd.date_range('2019-09-01', '2019-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr55.writerow([lgab,lghit])
lgteam1909.close()

wr56.writerow(['9월 기아 타수','9월 기아 안타'])
for day in pd.date_range('2019-09-01', '2019-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr56.writerow([htab,hthit])
htteam1909.close()

wr57.writerow(['9월 키움 타수','9월 키움 안타'])
for day in pd.date_range('2019-09-01', '2019-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr57.writerow([woab,wohit])
woteam1909.close()

wr58.writerow(['9월 두산 타수','9월 두산 안타'])
for day in pd.date_range('2019-09-01', '2019-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr58.writerow([obab,obhit])
obteam1909.close()

wr59.writerow(['9월 넥센 타수','9월 넥센 안타'])
for day in pd.date_range('2019-09-01', '2019-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata19[(teamdata19.GDAY_DS == daynum) & (teamdata19.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr59.writerow([ncab,nchit])
ncteam1909.close()
# 데이터 정렬 , 기본값이 오름차순이고 ,ascending=[0]을 추가하면 내림차순이 된다.

hhta=pd.read_csv('./hhteam1904.csv')
hhta=hhta.sum()
hhtata=hhta.iloc[1]/hhta.iloc[0]
hhtata=pd.Series([hhtata],index=['4월'])

skta=pd.read_csv('./skteam1904.csv')
skta=skta.sum()
sktata=skta.iloc[1]/skta.iloc[0]
sktata=pd.Series([sktata],index=['4월'])

ktta=pd.read_csv('./ktteam1904.csv')
ktta=ktta.sum()
kttata=ktta.iloc[1]/ktta.iloc[0]
kttata=pd.Series([kttata],index=['4월'])

ltta=pd.read_csv('./ltteam1904.csv')
ltta=ltta.sum()
lttata=ltta.iloc[1]/ltta.iloc[0]
lttata=pd.Series([lttata],index=['4월'])

ssta=pd.read_csv('./ssteam1904.csv')
ssta=ssta.sum()
sstata=ssta.iloc[1]/ssta.iloc[0]
sstata=pd.Series([sstata],index=['4월'])

lgta=pd.read_csv('./lgteam1904.csv')
lgta=lgta.sum()
lgtata=lgta.iloc[1]/lgta.iloc[0]
lgtata=pd.Series([lgtata],index=['4월'])

htta=pd.read_csv('./htteam1904.csv')
htta=htta.sum()
httata=htta.iloc[1]/htta.iloc[0]
httata=pd.Series([httata],index=['4월'])

wota=pd.read_csv('./woteam1904.csv')
wota=wota.sum()
wotata=wota.iloc[1]/wota.iloc[0]
wotata=pd.Series([wotata],index=['4월'])

obta=pd.read_csv('./obteam1904.csv')
obta=obta.sum()
obtata=obta.iloc[1]/obta.iloc[0]
obtata=pd.Series([obtata],index=['4월'])

ncta=pd.read_csv('./ncteam1904.csv')
ncta=ncta.sum()
nctata=ncta.iloc[1]/ncta.iloc[0]
nctata=pd.Series([nctata],index=['4월'])
data1904=pd.concat([hhtata,sktata,kttata,lttata,sstata,lgtata,httata,wotata,obtata,nctata],axis=1)
print(data1904)

hhta1=pd.read_csv('./hhteam1905.csv')
hhta1=hhta1.sum()
hhtata1=hhta1.iloc[1]/hhta1.iloc[0]
hhtata1=pd.Series([hhtata1],index=['5월'])

skta1=pd.read_csv('./skteam1905.csv')
skta1=skta1.sum()
sktata1=skta1.iloc[1]/skta1.iloc[0]
sktata1=pd.Series([sktata1],index=['5월'])

ktta1=pd.read_csv('./ktteam1905.csv')
ktta1=ktta1.sum()
kttata1=ktta1.iloc[1]/ktta1.iloc[0]
kttata1=pd.Series([kttata1],index=['5월'])

ltta1=pd.read_csv('./ltteam1905.csv')
ltta1=ltta1.sum()
lttata1=ltta1.iloc[1]/ltta1.iloc[0]
lttata1=pd.Series([lttata1],index=['5월'])

ssta1=pd.read_csv('./ssteam1905.csv')
ssta1=ssta1.sum()
sstata1=ssta1.iloc[1]/ssta1.iloc[0]
sstata1=pd.Series([sstata1],index=['5월'])

lgta1=pd.read_csv('./lgteam1905.csv')
lgta1=lgta1.sum()
lgtata1=lgta1.iloc[1]/lgta1.iloc[0]
lgtata1=pd.Series([lgtata1],index=['5월'])

htta1=pd.read_csv('./htteam1905.csv')
htta1=htta1.sum()
httata1=htta1.iloc[1]/htta1.iloc[0]
httata1=pd.Series([httata1],index=['5월'])

wota1=pd.read_csv('./woteam1905.csv')
wota1=wota1.sum()
wotata1=wota1.iloc[1]/wota1.iloc[0]
wotata1=pd.Series([wotata1],index=['5월'])

obta1=pd.read_csv('./obteam1905.csv')
obta1=obta1.sum()
obtata1=obta1.iloc[1]/obta1.iloc[0]
obtata1=pd.Series([obtata1],index=['5월'])

ncta1=pd.read_csv('./ncteam1905.csv')
ncta1=ncta1.sum()
nctata1=ncta1.iloc[1]/ncta1.iloc[0]
nctata1=pd.Series([nctata1],index=['5월'])
data1905=pd.concat([hhtata1,sktata1,kttata1,lttata1,sstata1,lgtata1,httata1,wotata1,obtata1,nctata1],axis=1)
print(data1905)

hhta2=pd.read_csv('./hhteam1906.csv')
hhta2=hhta2.sum()
hhtata2=hhta2.iloc[1]/hhta2.iloc[0]
hhtata2=pd.Series([hhtata2],index=['6월'])

skta2=pd.read_csv('./skteam1906.csv')
skta2=skta2.sum()
sktata2=skta2.iloc[1]/skta2.iloc[0]
sktata2=pd.Series([sktata2],index=['6월'])

ktta2=pd.read_csv('./ktteam1906.csv')
ktta2=ktta2.sum()
kttata2=ktta2.iloc[1]/ktta2.iloc[0]
kttata2=pd.Series([kttata2],index=['6월'])

ltta2=pd.read_csv('./ltteam1906.csv')
ltta2=ltta2.sum()
lttata2=ltta2.iloc[1]/ltta2.iloc[0]
lttata2=pd.Series([lttata2],index=['6월'])

ssta2=pd.read_csv('./ssteam1906.csv')
ssta2=ssta2.sum()
sstata2=ssta2.iloc[1]/ssta2.iloc[0]
sstata2=pd.Series([sstata2],index=['6월'])

lgta2=pd.read_csv('./lgteam1906.csv')
lgta2=lgta2.sum()
lgtata2=lgta2.iloc[1]/lgta2.iloc[0]
lgtata2=pd.Series([lgtata2],index=['6월'])

htta2=pd.read_csv('./htteam1906.csv')
htta2=htta2.sum()
httata2=htta2.iloc[1]/htta2.iloc[0]
httata2=pd.Series([httata2],index=['6월'])

wota2=pd.read_csv('./woteam1906.csv')
wota2=wota2.sum()
wotata2=wota2.iloc[1]/wota2.iloc[0]
wotata2=pd.Series([wotata2],index=['6월'])

obta2=pd.read_csv('./obteam1906.csv')
obta2=obta2.sum()
obtata2=obta2.iloc[1]/obta2.iloc[0]
obtata2=pd.Series([obtata2],index=['6월'])

ncta2=pd.read_csv('./ncteam1906.csv')
ncta2=ncta2.sum()
nctata2=ncta2.iloc[1]/ncta2.iloc[0]
nctata2=pd.Series([nctata2],index=['6월'])
data1906=pd.concat([hhtata2,sktata2,kttata2,lttata2,sstata2,lgtata2,httata2,wotata2,obtata2,nctata2],axis=1)
print(data1906)

hhta3=pd.read_csv('./hhteam1907.csv')
hhta3=hhta3.sum()
hhtata3=hhta3.iloc[1]/hhta3.iloc[0]
hhtata3=pd.Series([hhtata3],index=['7월'])

skta3=pd.read_csv('./skteam1907.csv')
skta3=skta3.sum()
sktata3=skta3.iloc[1]/skta3.iloc[0]
sktata3=pd.Series([sktata3],index=['7월'])

ktta3=pd.read_csv('./ktteam1907.csv')
ktta3=ktta3.sum()
kttata3=ktta3.iloc[1]/ktta3.iloc[0]
kttata3=pd.Series([kttata3],index=['7월'])

ltta3=pd.read_csv('./ltteam1907.csv')
ltta3=ltta3.sum()
lttata3=ltta3.iloc[1]/ltta3.iloc[0]
lttata3=pd.Series([lttata3],index=['7월'])

ssta3=pd.read_csv('./ssteam1907.csv')
ssta3=ssta3.sum()
sstata3=ssta3.iloc[1]/ssta3.iloc[0]
sstata3=pd.Series([sstata3],index=['7월'])

lgta3=pd.read_csv('./lgteam1907.csv')
lgta3=lgta3.sum()
lgtata3=lgta3.iloc[1]/lgta3.iloc[0]
lgtata3=pd.Series([lgtata3],index=['7월'])

htta3=pd.read_csv('./htteam1907.csv')
htta3=htta3.sum()
httata3=htta3.iloc[1]/htta3.iloc[0]
httata3=pd.Series([httata3],index=['7월'])

wota3=pd.read_csv('./woteam1907.csv')
wota3=wota3.sum()
wotata3=wota3.iloc[1]/wota3.iloc[0]
wotata3=pd.Series([wotata3],index=['7월'])

obta3=pd.read_csv('./obteam1907.csv')
obta3=obta3.sum()
obtata3=obta3.iloc[1]/obta3.iloc[0]
obtata3=pd.Series([obtata3],index=['7월'])

ncta3=pd.read_csv('./ncteam1907.csv')
ncta3=ncta3.sum()
nctata3=ncta3.iloc[1]/ncta3.iloc[0]
nctata3=pd.Series([nctata3],index=['7월'])
data1907=pd.concat([hhtata3,sktata3,kttata3,lttata3,sstata3,lgtata3,httata3,wotata3,obtata3,nctata3],axis=1)
print(data1907)

hhta4=pd.read_csv('./hhteam1908.csv')
hhta4=hhta4.sum()
hhtata4=hhta4.iloc[1]/hhta4.iloc[0]
hhtata4=pd.Series([hhtata4],index=['8월'])

skta4=pd.read_csv('./skteam1908.csv')
skta4=skta4.sum()
sktata4=skta4.iloc[1]/skta4.iloc[0]
sktata4=pd.Series([sktata4],index=['8월'])

ktta4=pd.read_csv('./ktteam1908.csv')
ktta4=ktta4.sum()
kttata4=ktta4.iloc[1]/ktta4.iloc[0]
kttata4=pd.Series([kttata4],index=['8월'])

ltta4=pd.read_csv('./ltteam1908.csv')
ltta4=ltta4.sum()
lttata4=ltta4.iloc[1]/ltta4.iloc[0]
lttata4=pd.Series([lttata4],index=['8월'])

ssta4=pd.read_csv('./ssteam1908.csv')
ssta4=ssta4.sum()
sstata4=ssta4.iloc[1]/ssta4.iloc[0]
sstata4=pd.Series([sstata4],index=['8월'])

lgta4=pd.read_csv('./lgteam1908.csv')
lgta4=lgta4.sum()
lgtata4=lgta4.iloc[1]/lgta4.iloc[0]
lgtata4=pd.Series([lgtata4],index=['8월'])

htta4=pd.read_csv('./htteam1908.csv')
htta4=htta4.sum()
httata4=htta4.iloc[1]/htta4.iloc[0]
httata4=pd.Series([httata4],index=['8월'])

wota4=pd.read_csv('./woteam1908.csv')
wota4=wota4.sum()
wotata4=wota4.iloc[1]/wota4.iloc[0]
wotata4=pd.Series([wotata4],index=['8월'])

obta4=pd.read_csv('./obteam1908.csv')
obta4=obta4.sum()
obtata4=obta4.iloc[1]/obta4.iloc[0]
obtata4=pd.Series([obtata4],index=['8월'])

ncta4=pd.read_csv('./ncteam1908.csv')
ncta4=ncta4.sum()
nctata4=ncta4.iloc[1]/ncta4.iloc[0]
nctata4=pd.Series([nctata4],index=['8월'])
data1908=pd.concat([hhtata4,sktata4,kttata4,lttata4,sstata4,lgtata4,httata4,wotata4,obtata4,nctata4],axis=1)
print(data1908)

hhta5=pd.read_csv('./hhteam1909.csv')
hhta5=hhta5.sum()
hhtata5=hhta5.iloc[1]/hhta5.iloc[0]
hhtata5=pd.Series([hhtata5],index=['9월'])

skta5=pd.read_csv('./skteam1909.csv')
skta5=skta5.sum()
sktata5=skta5.iloc[1]/skta5.iloc[0]
sktata5=pd.Series([sktata5],index=['9월'])

ktta5=pd.read_csv('./ktteam1909.csv')
ktta5=ktta5.sum()
kttata5=ktta5.iloc[1]/ktta5.iloc[0]
kttata5=pd.Series([kttata5],index=['9월'])

ltta5=pd.read_csv('./ltteam1909.csv')
ltta5=ltta5.sum()
lttata5=ltta5.iloc[1]/ltta5.iloc[0]
lttata5=pd.Series([lttata5],index=['9월'])

ssta5=pd.read_csv('./ssteam1909.csv')
ssta5=ssta5.sum()
sstata5=ssta5.iloc[1]/ssta5.iloc[0]
sstata5=pd.Series([sstata5],index=['9월'])

lgta5=pd.read_csv('./lgteam1909.csv')
lgta5=lgta5.sum()
lgtata5=lgta5.iloc[1]/lgta5.iloc[0]
lgtata5=pd.Series([lgtata5],index=['9월'])

htta5=pd.read_csv('./htteam1909.csv')
htta5=htta5.sum()
httata5=htta5.iloc[1]/htta5.iloc[0]
httata5=pd.Series([httata5],index=['9월'])

wota5=pd.read_csv('./woteam1909.csv')
wota5=wota5.sum()
wotata5=wota5.iloc[1]/wota5.iloc[0]
wotata5=pd.Series([wotata5],index=['9월'])

obta5=pd.read_csv('./obteam1909.csv')
obta5=obta5.sum()
obtata5=obta5.iloc[1]/obta5.iloc[0]
obtata5=pd.Series([obtata5],index=['9월'])

ncta5=pd.read_csv('./ncteam1909.csv')
ncta5=ncta5.sum()
nctata5=ncta5.iloc[1]/ncta5.iloc[0]
nctata5=pd.Series([nctata5],index=['9월'])
data1909=pd.concat([hhtata5,sktata5,kttata5,lttata5,sstata5,lgtata5,httata5,wotata5,obtata5,nctata5],axis=1)
print(data1909)

dataset19=pd.concat([data1904,data1905,data1906,data1907,data1908,data1909],axis=0)
dataset19=dataset19.rename(columns={0:'한화',1:'SK',2:'KT',3:'롯데',4:'삼성',5:'엘지',6:'기아',7:'키움',8:'두산',9:'넥센'})
print(dataset19)
dataset19.to_csv('./dataframe19.csv',index_label='경기날짜')