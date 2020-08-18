import pandas as pd
import numpy as np
import csv

teamdata18=pd.read_csv('./팀타자18.csv')
teamdata18=teamdata18[['GDAY_DS','T_ID','HIT','AB']]
teamdata18=teamdata18.sort_values(['GDAY_DS','T_ID'])
#team=['SK','KT','LT','HH','SS','LG','HT','WO','OB','NC']
hhteam1804 = open('./hhteam1804.csv', 'w',encoding='utf-8',newline='')
skteam1804 = open('./skteam1804.csv', 'w',encoding='utf-8',newline='')
ktteam1804 = open('./ktteam1804.csv', 'w',encoding='utf-8',newline='')
ltteam1804 = open('./ltteam1804.csv', 'w',encoding='utf-8',newline='')
ssteam1804 = open('./ssteam1804.csv', 'w',encoding='utf-8',newline='')
lgteam1804 = open('./lgteam1804.csv', 'w',encoding='utf-8',newline='')
htteam1804 = open('./htteam1804.csv', 'w',encoding='utf-8',newline='')
woteam1804 = open('./woteam1804.csv', 'w',encoding='utf-8',newline='')
obteam1804 = open('./obteam1804.csv', 'w',encoding='utf-8',newline='')
ncteam1804 = open('./ncteam1804.csv', 'w',encoding='utf-8',newline='')
wr=csv.writer(hhteam1804)
wr1=csv.writer(skteam1804)
wr2=csv.writer(ktteam1804)
wr3=csv.writer(ltteam1804)
wr4=csv.writer(ssteam1804)
wr5=csv.writer(lgteam1804)
wr6=csv.writer(htteam1804)
wr7=csv.writer(woteam1804)
wr8=csv.writer(obteam1804)
wr9=csv.writer(ncteam1804)

wr.writerow(['4월 한화 타수','4월 한화 안타'])
for day in pd.date_range('2018-04-01', '2018-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr.writerow([daynum,hhab,hhhit])

hhteam1804.close()

wr1.writerow(['4월 SK 타수','4월 SK 안타'])
for day in pd.date_range('2018-04-01', '2018-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr1.writerow([skab,skhit])
skteam1804.close()

wr2.writerow(['4월 KT 타수','4월 KT 안타'])
for day in pd.date_range('2018-04-01', '2018-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr2.writerow([ktab,kthit])
ktteam1804.close()

wr3.writerow(['4월 롯데 타수','4월 롯데 안타'])
for day in pd.date_range('2018-04-01', '2018-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr3.writerow([ltab,lthit])
ltteam1804.close()

wr4.writerow(['4월 삼성 타수','4월 삼성 안타'])
for day in pd.date_range('2018-04-01', '2018-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr4.writerow([ssab,sshit])
ssteam1804.close()

wr5.writerow(['4월 엘지 타수','4월 엘지 안타'])
for day in pd.date_range('2018-04-01', '2018-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr5.writerow([lgab,lghit])
lgteam1804.close()

wr6.writerow(['4월 기아 타수','4월 기아 안타'])
for day in pd.date_range('2018-04-01', '2018-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr6.writerow([htab,hthit])
htteam1804.close()

wr7.writerow(['4월 키움 타수','4월 키움 안타'])
for day in pd.date_range('2018-04-01', '2018-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr7.writerow([woab,wohit])
woteam1804.close()

wr8.writerow(['4월 두산 타수','4월 두산 안타'])
for day in pd.date_range('2018-04-01', '2018-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr8.writerow([obab,obhit])
obteam1804.close()

wr9.writerow(['4월 넥센 타수','4월 넥센 안타'])
for day in pd.date_range('2018-04-01', '2018-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr9.writerow([ncab,nchit])
ncteam1804.close()

hhteam1805 = open('./hhteam1805.csv', 'w',encoding='utf-8',newline='')
skteam1805 = open('./skteam1805.csv', 'w',encoding='utf-8',newline='')
ktteam1805 = open('./ktteam1805.csv', 'w',encoding='utf-8',newline='')
ltteam1805 = open('./ltteam1805.csv', 'w',encoding='utf-8',newline='')
ssteam1805 = open('./ssteam1805.csv', 'w',encoding='utf-8',newline='')
lgteam1805 = open('./lgteam1805.csv', 'w',encoding='utf-8',newline='')
htteam1805 = open('./htteam1805.csv', 'w',encoding='utf-8',newline='')
woteam1805 = open('./woteam1805.csv', 'w',encoding='utf-8',newline='')
obteam1805 = open('./obteam1805.csv', 'w',encoding='utf-8',newline='')
ncteam1805 = open('./ncteam1805.csv', 'w',encoding='utf-8',newline='')
wr10=csv.writer(hhteam1805)
wr11=csv.writer(skteam1805)
wr12=csv.writer(ktteam1805)
wr13=csv.writer(ltteam1805)
wr14=csv.writer(ssteam1805)
wr15=csv.writer(lgteam1805)
wr16=csv.writer(htteam1805)
wr17=csv.writer(woteam1805)
wr18=csv.writer(obteam1805)
wr19=csv.writer(ncteam1805)

wr10.writerow(['5월 한화 타수','5월 한화 안타'])
for day in pd.date_range('2018-05-01', '2018-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr10.writerow([hhab,hhhit])
hhteam1805.close()

wr11.writerow(['5월 SK 타수','5월 SK 안타'])
for day in pd.date_range('2018-05-01', '2018-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr11.writerow([skab,skhit])
skteam1805.close()

wr12.writerow(['5월 KT 타수','5월 KT 안타'])
for day in pd.date_range('2018-05-01', '2018-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr12.writerow([ktab,kthit])
ktteam1805.close()

wr13.writerow(['5월 롯데 타수','5월 롯데 안타'])
for day in pd.date_range('2018-05-01', '2018-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr13.writerow([ltab,lthit])
ltteam1805.close()

wr14.writerow(['5월 삼성 타수','5월 삼성 안타'])
for day in pd.date_range('2018-05-01', '2018-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr14.writerow([ssab,sshit])
ssteam1805.close()

wr15.writerow(['5월 엘지 타수','5월 엘지 안타'])
for day in pd.date_range('2018-05-01', '2018-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr15.writerow([lgab,lghit])
lgteam1805.close()

wr16.writerow(['5월 기아 타수','5월 기아 안타'])
for day in pd.date_range('2018-05-01', '2018-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr16.writerow([htab,hthit])
htteam1805.close()

wr17.writerow(['5월 키움 타수','5월 키움 안타'])
for day in pd.date_range('2018-05-01', '2018-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr17.writerow([woab,wohit])
woteam1805.close()

wr18.writerow(['5월 두산 타수','5월 두산 안타'])
for day in pd.date_range('2018-05-01', '2018-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr18.writerow([obab,obhit])
obteam1805.close()

wr19.writerow(['5월 넥센 타수','5월 넥센 안타'])
for day in pd.date_range('2018-05-01', '2018-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr19.writerow([ncab,nchit])
ncteam1805.close()

hhteam1806 = open('./hhteam1806.csv', 'w',encoding='utf-8',newline='')
skteam1806 = open('./skteam1806.csv', 'w',encoding='utf-8',newline='')
ktteam1806 = open('./ktteam1806.csv', 'w',encoding='utf-8',newline='')
ltteam1806 = open('./ltteam1806.csv', 'w',encoding='utf-8',newline='')
ssteam1806 = open('./ssteam1806.csv', 'w',encoding='utf-8',newline='')
lgteam1806 = open('./lgteam1806.csv', 'w',encoding='utf-8',newline='')
htteam1806 = open('./htteam1806.csv', 'w',encoding='utf-8',newline='')
woteam1806 = open('./woteam1806.csv', 'w',encoding='utf-8',newline='')
obteam1806 = open('./obteam1806.csv', 'w',encoding='utf-8',newline='')
ncteam1806 = open('./ncteam1806.csv', 'w',encoding='utf-8',newline='')
wr20=csv.writer(hhteam1806)
wr21=csv.writer(skteam1806)
wr22=csv.writer(ktteam1806)
wr23=csv.writer(ltteam1806)
wr24=csv.writer(ssteam1806)
wr25=csv.writer(lgteam1806)
wr26=csv.writer(htteam1806)
wr27=csv.writer(woteam1806)
wr28=csv.writer(obteam1806)
wr29=csv.writer(ncteam1806)

wr20.writerow(['6월 한화 타수','6월 한화 안타'])
for day in pd.date_range('2018-06-01', '2018-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr20.writerow([hhab,hhhit])
hhteam1806.close()

wr21.writerow(['6월 SK 타수','6월 SK 안타'])
for day in pd.date_range('2018-06-01', '2018-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr21.writerow([skab,skhit])
skteam1806.close()

wr22.writerow(['6월 KT 타수','6월 KT 안타'])
for day in pd.date_range('2018-06-01', '2018-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr22.writerow([ktab,kthit])
ktteam1806.close()

wr23.writerow(['6월 롯데 타수','6월 롯데 안타'])
for day in pd.date_range('2018-06-01', '2018-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr23.writerow([ltab,lthit])
ltteam1806.close()

wr24.writerow(['6월 삼성 타수','6월 삼성 안타'])
for day in pd.date_range('2018-06-01', '2018-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr24.writerow([ssab,sshit])
ssteam1806.close()

wr25.writerow(['6월 엘지 타수','6월 엘지 안타'])
for day in pd.date_range('2018-06-01', '2018-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr25.writerow([lgab,lghit])
lgteam1806.close()

wr26.writerow(['6월 기아 타수','6월 기아 안타'])
for day in pd.date_range('2018-06-01', '2018-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr26.writerow([htab,hthit])
htteam1806.close()

wr27.writerow(['6월 키움 타수','6월 키움 안타'])
for day in pd.date_range('2018-06-01', '2018-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr27.writerow([woab,wohit])
woteam1806.close()

wr28.writerow(['6월 두산 타수','6월 두산 안타'])
for day in pd.date_range('2018-06-01', '2018-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr28.writerow([obab,obhit])
obteam1806.close()

wr29.writerow(['6월 넥센 타수','6월 넥센 안타'])
for day in pd.date_range('2018-06-01', '2018-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr29.writerow([ncab,nchit])
ncteam1806.close()

hhteam1807 = open('./hhteam1807.csv', 'w',encoding='utf-8',newline='')
skteam1807 = open('./skteam1807.csv', 'w',encoding='utf-8',newline='')
ktteam1807 = open('./ktteam1807.csv', 'w',encoding='utf-8',newline='')
ltteam1807 = open('./ltteam1807.csv', 'w',encoding='utf-8',newline='')
ssteam1807 = open('./ssteam1807.csv', 'w',encoding='utf-8',newline='')
lgteam1807 = open('./lgteam1807.csv', 'w',encoding='utf-8',newline='')
htteam1807 = open('./htteam1807.csv', 'w',encoding='utf-8',newline='')
woteam1807 = open('./woteam1807.csv', 'w',encoding='utf-8',newline='')
obteam1807 = open('./obteam1807.csv', 'w',encoding='utf-8',newline='')
ncteam1807 = open('./ncteam1807.csv', 'w',encoding='utf-8',newline='')
wr30=csv.writer(hhteam1807)
wr31=csv.writer(skteam1807)
wr32=csv.writer(ktteam1807)
wr33=csv.writer(ltteam1807)
wr34=csv.writer(ssteam1807)
wr35=csv.writer(lgteam1807)
wr36=csv.writer(htteam1807)
wr37=csv.writer(woteam1807)
wr38=csv.writer(obteam1807)
wr39=csv.writer(ncteam1807)

wr30.writerow(['7월 한화 타수','7월 한화 안타'])
for day in pd.date_range('2018-07-01', '2018-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr30.writerow([hhab,hhhit])
hhteam1807.close()

wr31.writerow(['7월 SK 타수','7월 SK 안타'])
for day in pd.date_range('2018-07-01', '2018-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr31.writerow([skab,skhit])
skteam1807.close()

wr32.writerow(['7월 KT 타수','7월 KT 안타'])
for day in pd.date_range('2018-07-01', '2018-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr32.writerow([ktab,kthit])
ktteam1807.close()

wr33.writerow(['7월 롯데 타수','7월 롯데 안타'])
for day in pd.date_range('2018-07-01', '2018-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr33.writerow([ltab,lthit])
ltteam1807.close()

wr34.writerow(['7월 삼성 타수','7월 삼성 안타'])
for day in pd.date_range('2018-07-01', '2018-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr34.writerow([ssab,sshit])
ssteam1807.close()

wr35.writerow(['7월 엘지 타수','7월 엘지 안타'])
for day in pd.date_range('2018-07-01', '2018-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr35.writerow([lgab,lghit])
lgteam1807.close()

wr36.writerow(['7월 기아 타수','7월 기아 안타'])
for day in pd.date_range('2018-07-01', '2018-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr36.writerow([htab,hthit])
htteam1807.close()

wr37.writerow(['7월 키움 타수','7월 키움 안타'])
for day in pd.date_range('2018-07-01', '2018-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr37.writerow([woab,wohit])
woteam1807.close()

wr38.writerow(['7월 두산 타수','7월 두산 안타'])
for day in pd.date_range('2018-07-01', '2018-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr38.writerow([obab,obhit])
obteam1807.close()

wr39.writerow(['7월 넥센 타수','7월 넥센 안타'])
for day in pd.date_range('2018-07-01', '2018-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr39.writerow([ncab,nchit])
ncteam1807.close()

hhteam1808 = open('./hhteam1808.csv', 'w',encoding='utf-8',newline='')
skteam1808 = open('./skteam1808.csv', 'w',encoding='utf-8',newline='')
ktteam1808 = open('./ktteam1808.csv', 'w',encoding='utf-8',newline='')
ltteam1808 = open('./ltteam1808.csv', 'w',encoding='utf-8',newline='')
ssteam1808 = open('./ssteam1808.csv', 'w',encoding='utf-8',newline='')
lgteam1808 = open('./lgteam1808.csv', 'w',encoding='utf-8',newline='')
htteam1808 = open('./htteam1808.csv', 'w',encoding='utf-8',newline='')
woteam1808 = open('./woteam1808.csv', 'w',encoding='utf-8',newline='')
obteam1808 = open('./obteam1808.csv', 'w',encoding='utf-8',newline='')
ncteam1808 = open('./ncteam1808.csv', 'w',encoding='utf-8',newline='')
wr40=csv.writer(hhteam1808)
wr41=csv.writer(skteam1808)
wr42=csv.writer(ktteam1808)
wr43=csv.writer(ltteam1808)
wr44=csv.writer(ssteam1808)
wr45=csv.writer(lgteam1808)
wr46=csv.writer(htteam1808)
wr47=csv.writer(woteam1808)
wr48=csv.writer(obteam1808)
wr49=csv.writer(ncteam1808)

wr40.writerow(['8월 한화 타수','8월 한화 안타'])
for day in pd.date_range('2018-08-01', '2018-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr40.writerow([hhab,hhhit])
hhteam1808.close()

wr41.writerow(['8월 SK 타수','8월 SK 안타'])
for day in pd.date_range('2018-08-01', '2018-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr41.writerow([skab,skhit])
skteam1808.close()

wr42.writerow(['8월 KT 타수','8월 KT 안타'])
for day in pd.date_range('2018-08-01', '2018-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr42.writerow([ktab,kthit])
ktteam1808.close()

wr43.writerow(['8월 롯데 타수','8월 롯데 안타'])
for day in pd.date_range('2018-08-01', '2018-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr43.writerow([ltab,lthit])
ltteam1808.close()

wr44.writerow(['8월 삼성 타수','8월 삼성 안타'])
for day in pd.date_range('2018-08-01', '2018-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr44.writerow([ssab,sshit])
ssteam1808.close()

wr45.writerow(['8월 엘지 타수','8월 엘지 안타'])
for day in pd.date_range('2018-08-01', '2018-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr45.writerow([lgab,lghit])
lgteam1808.close()

wr46.writerow(['8월 기아 타수','8월 기아 안타'])
for day in pd.date_range('2018-08-01', '2018-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr46.writerow([htab,hthit])
htteam1808.close()

wr47.writerow(['8월 키움 타수','8월 키움 안타'])
for day in pd.date_range('2018-08-01', '2018-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr47.writerow([woab,wohit])
woteam1808.close()

wr48.writerow(['8월 두산 타수','8월 두산 안타'])
for day in pd.date_range('2018-08-01', '2018-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr48.writerow([obab,obhit])
obteam1808.close()

wr49.writerow(['8월 넥센 타수','8월 넥센 안타'])
for day in pd.date_range('2018-08-01', '2018-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr49.writerow([ncab,nchit])
ncteam1808.close()

hhteam1809 = open('./hhteam1809.csv', 'w',encoding='utf-8',newline='')
skteam1809 = open('./skteam1809.csv', 'w',encoding='utf-8',newline='')
ktteam1809 = open('./ktteam1809.csv', 'w',encoding='utf-8',newline='')
ltteam1809 = open('./ltteam1809.csv', 'w',encoding='utf-8',newline='')
ssteam1809 = open('./ssteam1809.csv', 'w',encoding='utf-8',newline='')
lgteam1809 = open('./lgteam1809.csv', 'w',encoding='utf-8',newline='')
htteam1809 = open('./htteam1809.csv', 'w',encoding='utf-8',newline='')
woteam1809 = open('./woteam1809.csv', 'w',encoding='utf-8',newline='')
obteam1809 = open('./obteam1809.csv', 'w',encoding='utf-8',newline='')
ncteam1809 = open('./ncteam1809.csv', 'w',encoding='utf-8',newline='')
wr50=csv.writer(hhteam1809)
wr51=csv.writer(skteam1809)
wr52=csv.writer(ktteam1809)
wr53=csv.writer(ltteam1809)
wr54=csv.writer(ssteam1809)
wr55=csv.writer(lgteam1809)
wr56=csv.writer(htteam1809)
wr57=csv.writer(woteam1809)
wr58=csv.writer(obteam1809)
wr59=csv.writer(ncteam1809)

wr50.writerow(['9월 한화 타수','9월 한화 안타'])
for day in pd.date_range('2018-09-01', '2018-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr50.writerow([hhab,hhhit])
hhteam1809.close()

wr51.writerow(['9월 SK 타수','9월 SK 안타'])
for day in pd.date_range('2018-09-01', '2018-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr51.writerow([skab,skhit])
skteam1809.close()

wr52.writerow(['9월 KT 타수','9월 KT 안타'])
for day in pd.date_range('2018-09-01', '2018-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr52.writerow([ktab,kthit])
ktteam1809.close()

wr53.writerow(['9월 롯데 타수','9월 롯데 안타'])
for day in pd.date_range('2018-09-01', '2018-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr53.writerow([ltab,lthit])
ltteam1809.close()

wr54.writerow(['9월 삼성 타수','9월 삼성 안타'])
for day in pd.date_range('2018-09-01', '2018-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr54.writerow([ssab,sshit])
ssteam1809.close()

wr55.writerow(['9월 엘지 타수','9월 엘지 안타'])
for day in pd.date_range('2018-09-01', '2018-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr55.writerow([lgab,lghit])
lgteam1809.close()

wr56.writerow(['9월 기아 타수','9월 기아 안타'])
for day in pd.date_range('2018-09-01', '2018-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr56.writerow([htab,hthit])
htteam1809.close()

wr57.writerow(['9월 키움 타수','9월 키움 안타'])
for day in pd.date_range('2018-09-01', '2018-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr57.writerow([woab,wohit])
woteam1809.close()

wr58.writerow(['9월 두산 타수','9월 두산 안타'])
for day in pd.date_range('2018-09-01', '2018-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr58.writerow([obab,obhit])
obteam1809.close()

wr59.writerow(['9월 넥센 타수','9월 넥센 안타'])
for day in pd.date_range('2018-09-01', '2018-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr59.writerow([ncab,nchit])
ncteam1809.close()
# 데이터 정렬 , 기본값이 오름차순이고 ,ascending=[0]을 추가하면 내림차순이 된다.

hhteam1810 = open('./hhteam1810.csv', 'w',encoding='utf-8',newline='')
skteam1810 = open('./skteam1810.csv', 'w',encoding='utf-8',newline='')
ktteam1810 = open('./ktteam1810.csv', 'w',encoding='utf-8',newline='')
ltteam1810 = open('./ltteam1810.csv', 'w',encoding='utf-8',newline='')
ssteam1810 = open('./ssteam1810.csv', 'w',encoding='utf-8',newline='')
lgteam1810 = open('./lgteam1810.csv', 'w',encoding='utf-8',newline='')
htteam1810 = open('./htteam1810.csv', 'w',encoding='utf-8',newline='')
woteam1810 = open('./woteam1810.csv', 'w',encoding='utf-8',newline='')
obteam1810 = open('./obteam1810.csv', 'w',encoding='utf-8',newline='')
ncteam1810 = open('./ncteam1810.csv', 'w',encoding='utf-8',newline='')
wr60=csv.writer(hhteam1810)
wr61=csv.writer(skteam1810)
wr62=csv.writer(ktteam1810)
wr63=csv.writer(ltteam1810)
wr64=csv.writer(ssteam1810)
wr65=csv.writer(lgteam1810)
wr66=csv.writer(htteam1810)
wr67=csv.writer(woteam1810)
wr68=csv.writer(obteam1810)
wr69=csv.writer(ncteam1810)

wr60.writerow(['10월 한화 타수','10월 한화 안타'])
for day in pd.date_range('2018-10-01', '2018-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr60.writerow([hhab,hhhit])
hhteam1810.close()

wr61.writerow(['10월 SK 타수','10월 SK 안타'])
for day in pd.date_range('2018-10-01', '2018-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr61.writerow([skab,skhit])
skteam1810.close()

wr62.writerow(['10월 KT 타수','10월 KT 안타'])
for day in pd.date_range('2018-10-01', '2018-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr62.writerow([ktab,kthit])
ktteam1810.close()

wr63.writerow(['10월 롯데 타수','10월 롯데 안타'])
for day in pd.date_range('2018-10-01', '2018-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr63.writerow([ltab,lthit])
ltteam1810.close()

wr64.writerow(['10월 삼성 타수','10월 삼성 안타'])
for day in pd.date_range('2018-10-01', '2018-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr64.writerow([ssab,sshit])
ssteam1810.close()

wr65.writerow(['10월 엘지 타수','10월 엘지 안타'])
for day in pd.date_range('2018-10-01', '2018-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr65.writerow([lgab,lghit])
lgteam1810.close()

wr66.writerow(['10월 기아 타수','10월 기아 안타'])
for day in pd.date_range('2018-10-01', '2018-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr66.writerow([htab,hthit])
htteam1810.close()

wr67.writerow(['10월 키움 타수','10월 키움 안타'])
for day in pd.date_range('2018-10-01', '2018-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr67.writerow([woab,wohit])
woteam1810.close()

wr68.writerow(['10월 두산 타수','10월 두산 안타'])
for day in pd.date_range('2018-10-01', '2018-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr68.writerow([obab,obhit])
obteam1810.close()

wr69.writerow(['10월 넥센 타수','10월 넥센 안타'])
for day in pd.date_range('2018-10-01', '2018-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata18[(teamdata18.GDAY_DS == daynum) & (teamdata18.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr69.writerow([ncab,nchit])
ncteam1810.close()

hhta=pd.read_csv('./hhteam1804.csv')
hhta=hhta.sum()
hhtata=hhta.iloc[1]/hhta.iloc[0]
hhtata=pd.Series([hhtata],index=['4월'])

skta=pd.read_csv('./skteam1804.csv')
skta=skta.sum()
sktata=skta.iloc[1]/skta.iloc[0]
sktata=pd.Series([sktata],index=['4월'])

ktta=pd.read_csv('./ktteam1804.csv')
ktta=ktta.sum()
kttata=ktta.iloc[1]/ktta.iloc[0]
kttata=pd.Series([kttata],index=['4월'])

ltta=pd.read_csv('./ltteam1804.csv')
ltta=ltta.sum()
lttata=ltta.iloc[1]/ltta.iloc[0]
lttata=pd.Series([lttata],index=['4월'])

ssta=pd.read_csv('./ssteam1804.csv')
ssta=ssta.sum()
sstata=ssta.iloc[1]/ssta.iloc[0]
sstata=pd.Series([sstata],index=['4월'])

lgta=pd.read_csv('./lgteam1804.csv')
lgta=lgta.sum()
lgtata=lgta.iloc[1]/lgta.iloc[0]
lgtata=pd.Series([lgtata],index=['4월'])

htta=pd.read_csv('./htteam1804.csv')
htta=htta.sum()
httata=htta.iloc[1]/htta.iloc[0]
httata=pd.Series([httata],index=['4월'])

wota=pd.read_csv('./woteam1804.csv')
wota=wota.sum()
wotata=wota.iloc[1]/wota.iloc[0]
wotata=pd.Series([wotata],index=['4월'])

obta=pd.read_csv('./obteam1804.csv')
obta=obta.sum()
obtata=obta.iloc[1]/obta.iloc[0]
obtata=pd.Series([obtata],index=['4월'])

ncta=pd.read_csv('./ncteam1804.csv')
ncta=ncta.sum()
nctata=ncta.iloc[1]/ncta.iloc[0]
nctata=pd.Series([nctata],index=['4월'])
data1804=pd.concat([hhtata,sktata,kttata,lttata,sstata,lgtata,httata,wotata,obtata,nctata],axis=1)
print(data1804)

hhta1=pd.read_csv('./hhteam1805.csv')
hhta1=hhta1.sum()
hhtata1=hhta1.iloc[1]/hhta1.iloc[0]
hhtata1=pd.Series([hhtata1],index=['5월'])

skta1=pd.read_csv('./skteam1805.csv')
skta1=skta1.sum()
sktata1=skta1.iloc[1]/skta1.iloc[0]
sktata1=pd.Series([sktata1],index=['5월'])

ktta1=pd.read_csv('./ktteam1805.csv')
ktta1=ktta1.sum()
kttata1=ktta1.iloc[1]/ktta1.iloc[0]
kttata1=pd.Series([kttata1],index=['5월'])

ltta1=pd.read_csv('./ltteam1805.csv')
ltta1=ltta1.sum()
lttata1=ltta1.iloc[1]/ltta1.iloc[0]
lttata1=pd.Series([lttata1],index=['5월'])

ssta1=pd.read_csv('./ssteam1805.csv')
ssta1=ssta1.sum()
sstata1=ssta1.iloc[1]/ssta1.iloc[0]
sstata1=pd.Series([sstata1],index=['5월'])

lgta1=pd.read_csv('./lgteam1805.csv')
lgta1=lgta1.sum()
lgtata1=lgta1.iloc[1]/lgta1.iloc[0]
lgtata1=pd.Series([lgtata1],index=['5월'])

htta1=pd.read_csv('./htteam1805.csv')
htta1=htta1.sum()
httata1=htta1.iloc[1]/htta1.iloc[0]
httata1=pd.Series([httata1],index=['5월'])

wota1=pd.read_csv('./woteam1805.csv')
wota1=wota1.sum()
wotata1=wota1.iloc[1]/wota1.iloc[0]
wotata1=pd.Series([wotata1],index=['5월'])

obta1=pd.read_csv('./obteam1805.csv')
obta1=obta1.sum()
obtata1=obta1.iloc[1]/obta1.iloc[0]
obtata1=pd.Series([obtata1],index=['5월'])

ncta1=pd.read_csv('./ncteam1805.csv')
ncta1=ncta1.sum()
nctata1=ncta1.iloc[1]/ncta1.iloc[0]
nctata1=pd.Series([nctata1],index=['5월'])
data1805=pd.concat([hhtata1,sktata1,kttata1,lttata1,sstata1,lgtata1,httata1,wotata1,obtata1,nctata1],axis=1)
print(data1805)

hhta2=pd.read_csv('./hhteam1806.csv')
hhta2=hhta2.sum()
hhtata2=hhta2.iloc[1]/hhta2.iloc[0]
hhtata2=pd.Series([hhtata2],index=['6월'])

skta2=pd.read_csv('./skteam1806.csv')
skta2=skta2.sum()
sktata2=skta2.iloc[1]/skta2.iloc[0]
sktata2=pd.Series([sktata2],index=['6월'])

ktta2=pd.read_csv('./ktteam1806.csv')
ktta2=ktta2.sum()
kttata2=ktta2.iloc[1]/ktta2.iloc[0]
kttata2=pd.Series([kttata2],index=['6월'])

ltta2=pd.read_csv('./ltteam1806.csv')
ltta2=ltta2.sum()
lttata2=ltta2.iloc[1]/ltta2.iloc[0]
lttata2=pd.Series([lttata2],index=['6월'])

ssta2=pd.read_csv('./ssteam1806.csv')
ssta2=ssta2.sum()
sstata2=ssta2.iloc[1]/ssta2.iloc[0]
sstata2=pd.Series([sstata2],index=['6월'])

lgta2=pd.read_csv('./lgteam1806.csv')
lgta2=lgta2.sum()
lgtata2=lgta2.iloc[1]/lgta2.iloc[0]
lgtata2=pd.Series([lgtata2],index=['6월'])

htta2=pd.read_csv('./htteam1806.csv')
htta2=htta2.sum()
httata2=htta2.iloc[1]/htta2.iloc[0]
httata2=pd.Series([httata2],index=['6월'])

wota2=pd.read_csv('./woteam1806.csv')
wota2=wota2.sum()
wotata2=wota2.iloc[1]/wota2.iloc[0]
wotata2=pd.Series([wotata2],index=['6월'])

obta2=pd.read_csv('./obteam1806.csv')
obta2=obta2.sum()
obtata2=obta2.iloc[1]/obta2.iloc[0]
obtata2=pd.Series([obtata2],index=['6월'])

ncta2=pd.read_csv('./ncteam1806.csv')
ncta2=ncta2.sum()
nctata2=ncta2.iloc[1]/ncta2.iloc[0]
nctata2=pd.Series([nctata2],index=['6월'])
data1806=pd.concat([hhtata2,sktata2,kttata2,lttata2,sstata2,lgtata2,httata2,wotata2,obtata2,nctata2],axis=1)
print(data1806)

hhta3=pd.read_csv('./hhteam1807.csv')
hhta3=hhta3.sum()
hhtata3=hhta3.iloc[1]/hhta3.iloc[0]
hhtata3=pd.Series([hhtata3],index=['7월'])

skta3=pd.read_csv('./skteam1807.csv')
skta3=skta3.sum()
sktata3=skta3.iloc[1]/skta3.iloc[0]
sktata3=pd.Series([sktata3],index=['7월'])

ktta3=pd.read_csv('./ktteam1807.csv')
ktta3=ktta3.sum()
kttata3=ktta3.iloc[1]/ktta3.iloc[0]
kttata3=pd.Series([kttata3],index=['7월'])

ltta3=pd.read_csv('./ltteam1807.csv')
ltta3=ltta3.sum()
lttata3=ltta3.iloc[1]/ltta3.iloc[0]
lttata3=pd.Series([lttata3],index=['7월'])

ssta3=pd.read_csv('./ssteam1807.csv')
ssta3=ssta3.sum()
sstata3=ssta3.iloc[1]/ssta3.iloc[0]
sstata3=pd.Series([sstata3],index=['7월'])

lgta3=pd.read_csv('./lgteam1807.csv')
lgta3=lgta3.sum()
lgtata3=lgta3.iloc[1]/lgta3.iloc[0]
lgtata3=pd.Series([lgtata3],index=['7월'])

htta3=pd.read_csv('./htteam1807.csv')
htta3=htta3.sum()
httata3=htta3.iloc[1]/htta3.iloc[0]
httata3=pd.Series([httata3],index=['7월'])

wota3=pd.read_csv('./woteam1807.csv')
wota3=wota3.sum()
wotata3=wota3.iloc[1]/wota3.iloc[0]
wotata3=pd.Series([wotata3],index=['7월'])

obta3=pd.read_csv('./obteam1807.csv')
obta3=obta3.sum()
obtata3=obta3.iloc[1]/obta3.iloc[0]
obtata3=pd.Series([obtata3],index=['7월'])

ncta3=pd.read_csv('./ncteam1807.csv')
ncta3=ncta3.sum()
nctata3=ncta3.iloc[1]/ncta3.iloc[0]
nctata3=pd.Series([nctata3],index=['7월'])
data1807=pd.concat([hhtata3,sktata3,kttata3,lttata3,sstata3,lgtata3,httata3,wotata3,obtata3,nctata3],axis=1)
print(data1807)

hhta4=pd.read_csv('./hhteam1808.csv')
hhta4=hhta4.sum()
hhtata4=hhta4.iloc[1]/hhta4.iloc[0]
hhtata4=pd.Series([hhtata4],index=['8월'])

skta4=pd.read_csv('./skteam1808.csv')
skta4=skta4.sum()
sktata4=skta4.iloc[1]/skta4.iloc[0]
sktata4=pd.Series([sktata4],index=['8월'])

ktta4=pd.read_csv('./ktteam1808.csv')
ktta4=ktta4.sum()
kttata4=ktta4.iloc[1]/ktta4.iloc[0]
kttata4=pd.Series([kttata4],index=['8월'])

ltta4=pd.read_csv('./ltteam1808.csv')
ltta4=ltta4.sum()
lttata4=ltta4.iloc[1]/ltta4.iloc[0]
lttata4=pd.Series([lttata4],index=['8월'])

ssta4=pd.read_csv('./ssteam1808.csv')
ssta4=ssta4.sum()
sstata4=ssta4.iloc[1]/ssta4.iloc[0]
sstata4=pd.Series([sstata4],index=['8월'])

lgta4=pd.read_csv('./lgteam1808.csv')
lgta4=lgta4.sum()
lgtata4=lgta4.iloc[1]/lgta4.iloc[0]
lgtata4=pd.Series([lgtata4],index=['8월'])

htta4=pd.read_csv('./htteam1808.csv')
htta4=htta4.sum()
httata4=htta4.iloc[1]/htta4.iloc[0]
httata4=pd.Series([httata4],index=['8월'])

wota4=pd.read_csv('./woteam1808.csv')
wota4=wota4.sum()
wotata4=wota4.iloc[1]/wota4.iloc[0]
wotata4=pd.Series([wotata4],index=['8월'])

obta4=pd.read_csv('./obteam1808.csv')
obta4=obta4.sum()
obtata4=obta4.iloc[1]/obta4.iloc[0]
obtata4=pd.Series([obtata4],index=['8월'])

ncta4=pd.read_csv('./ncteam1808.csv')
ncta4=ncta4.sum()
nctata4=ncta4.iloc[1]/ncta4.iloc[0]
nctata4=pd.Series([nctata4],index=['8월'])
data1808=pd.concat([hhtata4,sktata4,kttata4,lttata4,sstata4,lgtata4,httata4,wotata4,obtata4,nctata4],axis=1)
print(data1808)

hhta5=pd.read_csv('./hhteam1809.csv')
hhta5=hhta5.sum()
hhtata5=hhta5.iloc[1]/hhta5.iloc[0]
hhtata5=pd.Series([hhtata5],index=['9월'])

skta5=pd.read_csv('./skteam1809.csv')
skta5=skta5.sum()
sktata5=skta5.iloc[1]/skta5.iloc[0]
sktata5=pd.Series([sktata5],index=['9월'])

ktta5=pd.read_csv('./ktteam1809.csv')
ktta5=ktta5.sum()
kttata5=ktta5.iloc[1]/ktta5.iloc[0]
kttata5=pd.Series([kttata5],index=['9월'])

ltta5=pd.read_csv('./ltteam1809.csv')
ltta5=ltta5.sum()
lttata5=ltta5.iloc[1]/ltta5.iloc[0]
lttata5=pd.Series([lttata5],index=['9월'])

ssta5=pd.read_csv('./ssteam1809.csv')
ssta5=ssta5.sum()
sstata5=ssta5.iloc[1]/ssta5.iloc[0]
sstata5=pd.Series([sstata5],index=['9월'])

lgta5=pd.read_csv('./lgteam1809.csv')
lgta5=lgta5.sum()
lgtata5=lgta5.iloc[1]/lgta5.iloc[0]
lgtata5=pd.Series([lgtata5],index=['9월'])

htta5=pd.read_csv('./htteam1809.csv')
htta5=htta5.sum()
httata5=htta5.iloc[1]/htta5.iloc[0]
httata5=pd.Series([httata5],index=['9월'])

wota5=pd.read_csv('./woteam1809.csv')
wota5=wota5.sum()
wotata5=wota5.iloc[1]/wota5.iloc[0]
wotata5=pd.Series([wotata5],index=['9월'])

obta5=pd.read_csv('./obteam1809.csv')
obta5=obta5.sum()
obtata5=obta5.iloc[1]/obta5.iloc[0]
obtata5=pd.Series([obtata5],index=['9월'])

ncta5=pd.read_csv('./ncteam1809.csv')
ncta5=ncta5.sum()
nctata5=ncta5.iloc[1]/ncta5.iloc[0]
nctata5=pd.Series([nctata5],index=['9월'])
data1809=pd.concat([hhtata5,sktata5,kttata5,lttata5,sstata5,lgtata5,httata5,wotata5,obtata5,nctata5],axis=1)
print(data1809)

hhta6=pd.read_csv('./hhteam1810.csv')
hhta6=hhta6.sum()
hhtata6=hhta6.iloc[1]/hhta6.iloc[0]
hhtata6=pd.Series([hhtata6],index=['10월'])

skta6=pd.read_csv('./skteam1810.csv')
skta6=skta6.sum()
sktata6=skta6.iloc[1]/skta6.iloc[0]
sktata6=pd.Series([sktata6],index=['10월'])

ktta6=pd.read_csv('./ktteam1810.csv')
ktta6=ktta6.sum()
kttata6=ktta6.iloc[1]/ktta6.iloc[0]
kttata6=pd.Series([kttata6],index=['10월'])

ltta6=pd.read_csv('./ltteam1810.csv')
ltta6=ltta6.sum()
lttata6=ltta6.iloc[1]/ltta6.iloc[0]
lttata6=pd.Series([lttata6],index=['10월'])

ssta6=pd.read_csv('./ssteam1810.csv')
ssta6=ssta6.sum()
sstata6=ssta6.iloc[1]/ssta6.iloc[0]
sstata6=pd.Series([sstata6],index=['10월'])

lgta6=pd.read_csv('./lgteam1810.csv')
lgta6=lgta6.sum()
lgtata6=lgta6.iloc[1]/lgta6.iloc[0]
lgtata6=pd.Series([lgtata6],index=['10월'])

htta6=pd.read_csv('./htteam1810.csv')
htta6=htta6.sum()
httata6=htta6.iloc[1]/htta6.iloc[0]
httata6=pd.Series([httata6],index=['10월'])

wota6=pd.read_csv('./woteam1810.csv')
wota6=wota6.sum()
wotata6=wota6.iloc[1]/wota6.iloc[0]
wotata6=pd.Series([wotata6],index=['10월'])

obta6=pd.read_csv('./obteam1810.csv')
obta6=obta6.sum()
obtata6=obta6.iloc[1]/obta6.iloc[0]
obtata6=pd.Series([obtata6],index=['10월'])

ncta6=pd.read_csv('./ncteam1810.csv')
ncta6=ncta6.sum()
nctata6=ncta6.iloc[1]/ncta6.iloc[0]
nctata6=pd.Series([nctata6],index=['10월'])
data1810=pd.concat([hhtata6,sktata6,kttata6,lttata6,sstata6,lgtata6,httata6,wotata6,obtata6,nctata6],axis=1)
print(data1810)

dataset18=pd.concat([data1804,data1805,data1806,data1807,data1808,data1809,data1810],axis=0)
dataset18=dataset18.rename(columns={0:'한화',1:'SK',2:'KT',3:'롯데',4:'삼성',5:'엘지',6:'기아',7:'키움',8:'두산',9:'넥센'})
print(dataset18)
dataset18.to_csv('./dataframe18.csv',index_label='경기날짜')