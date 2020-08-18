import pandas as pd
import numpy as np
import csv

teamdata16=pd.read_csv('./팀타자16.csv')
teamdata16=teamdata16[['GDAY_DS','T_ID','HIT','AB']]
teamdata16=teamdata16.sort_values(['GDAY_DS','T_ID'])
#team=['SK','KT','LT','HH','SS','LG','HT','WO','OB','NC']
hhteam1604 = open('./hhteam1604.csv', 'w',encoding='utf-8',newline='')
skteam1604 = open('./skteam1604.csv', 'w',encoding='utf-8',newline='')
ktteam1604 = open('./ktteam1604.csv', 'w',encoding='utf-8',newline='')
ltteam1604 = open('./ltteam1604.csv', 'w',encoding='utf-8',newline='')
ssteam1604 = open('./ssteam1604.csv', 'w',encoding='utf-8',newline='')
lgteam1604 = open('./lgteam1604.csv', 'w',encoding='utf-8',newline='')
htteam1604 = open('./htteam1604.csv', 'w',encoding='utf-8',newline='')
woteam1604 = open('./woteam1604.csv', 'w',encoding='utf-8',newline='')
obteam1604 = open('./obteam1604.csv', 'w',encoding='utf-8',newline='')
ncteam1604 = open('./ncteam1604.csv', 'w',encoding='utf-8',newline='')
wr=csv.writer(hhteam1604)
wr1=csv.writer(skteam1604)
wr2=csv.writer(ktteam1604)
wr3=csv.writer(ltteam1604)
wr4=csv.writer(ssteam1604)
wr5=csv.writer(lgteam1604)
wr6=csv.writer(htteam1604)
wr7=csv.writer(woteam1604)
wr8=csv.writer(obteam1604)
wr9=csv.writer(ncteam1604)

wr.writerow(['4월 한화 타수','4월 한화 안타'])
for day in pd.date_range('2016-04-01', '2016-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr.writerow([daynum,hhab,hhhit])

hhteam1604.close()

wr1.writerow(['4월 SK 타수','4월 SK 안타'])
for day in pd.date_range('2016-04-01', '2016-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr1.writerow([skab,skhit])
skteam1604.close()

wr2.writerow(['4월 KT 타수','4월 KT 안타'])
for day in pd.date_range('2016-04-01', '2016-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr2.writerow([ktab,kthit])
ktteam1604.close()

wr3.writerow(['4월 롯데 타수','4월 롯데 안타'])
for day in pd.date_range('2016-04-01', '2016-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr3.writerow([ltab,lthit])
ltteam1604.close()

wr4.writerow(['4월 삼성 타수','4월 삼성 안타'])
for day in pd.date_range('2016-04-01', '2016-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr4.writerow([ssab,sshit])
ssteam1604.close()

wr5.writerow(['4월 엘지 타수','4월 엘지 안타'])
for day in pd.date_range('2016-04-01', '2016-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr5.writerow([lgab,lghit])
lgteam1604.close()

wr6.writerow(['4월 기아 타수','4월 기아 안타'])
for day in pd.date_range('2016-04-01', '2016-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr6.writerow([htab,hthit])
htteam1604.close()

wr7.writerow(['4월 키움 타수','4월 키움 안타'])
for day in pd.date_range('2016-04-01', '2016-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr7.writerow([woab,wohit])
woteam1604.close()

wr8.writerow(['4월 두산 타수','4월 두산 안타'])
for day in pd.date_range('2016-04-01', '2016-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr8.writerow([obab,obhit])
obteam1604.close()

wr9.writerow(['4월 넥센 타수','4월 넥센 안타'])
for day in pd.date_range('2016-04-01', '2016-04-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr9.writerow([ncab,nchit])
ncteam1604.close()

hhteam1605 = open('./hhteam1605.csv', 'w',encoding='utf-8',newline='')
skteam1605 = open('./skteam1605.csv', 'w',encoding='utf-8',newline='')
ktteam1605 = open('./ktteam1605.csv', 'w',encoding='utf-8',newline='')
ltteam1605 = open('./ltteam1605.csv', 'w',encoding='utf-8',newline='')
ssteam1605 = open('./ssteam1605.csv', 'w',encoding='utf-8',newline='')
lgteam1605 = open('./lgteam1605.csv', 'w',encoding='utf-8',newline='')
htteam1605 = open('./htteam1605.csv', 'w',encoding='utf-8',newline='')
woteam1605 = open('./woteam1605.csv', 'w',encoding='utf-8',newline='')
obteam1605 = open('./obteam1605.csv', 'w',encoding='utf-8',newline='')
ncteam1605 = open('./ncteam1605.csv', 'w',encoding='utf-8',newline='')
wr10=csv.writer(hhteam1605)
wr11=csv.writer(skteam1605)
wr12=csv.writer(ktteam1605)
wr13=csv.writer(ltteam1605)
wr14=csv.writer(ssteam1605)
wr15=csv.writer(lgteam1605)
wr16=csv.writer(htteam1605)
wr17=csv.writer(woteam1605)
wr18=csv.writer(obteam1605)
wr19=csv.writer(ncteam1605)

wr10.writerow(['5월 한화 타수','5월 한화 안타'])
for day in pd.date_range('2016-05-01', '2016-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr10.writerow([hhab,hhhit])
hhteam1605.close()

wr11.writerow(['5월 SK 타수','5월 SK 안타'])
for day in pd.date_range('2016-05-01', '2016-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr11.writerow([skab,skhit])
skteam1605.close()

wr12.writerow(['5월 KT 타수','5월 KT 안타'])
for day in pd.date_range('2016-05-01', '2016-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr12.writerow([ktab,kthit])
ktteam1605.close()

wr13.writerow(['5월 롯데 타수','5월 롯데 안타'])
for day in pd.date_range('2016-05-01', '2016-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr13.writerow([ltab,lthit])
ltteam1605.close()

wr14.writerow(['5월 삼성 타수','5월 삼성 안타'])
for day in pd.date_range('2016-05-01', '2016-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr14.writerow([ssab,sshit])
ssteam1605.close()

wr15.writerow(['5월 엘지 타수','5월 엘지 안타'])
for day in pd.date_range('2016-05-01', '2016-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr15.writerow([lgab,lghit])
lgteam1605.close()

wr16.writerow(['5월 기아 타수','5월 기아 안타'])
for day in pd.date_range('2016-05-01', '2016-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr16.writerow([htab,hthit])
htteam1605.close()

wr17.writerow(['5월 키움 타수','5월 키움 안타'])
for day in pd.date_range('2016-05-01', '2016-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr17.writerow([woab,wohit])
woteam1605.close()

wr18.writerow(['5월 두산 타수','5월 두산 안타'])
for day in pd.date_range('2016-05-01', '2016-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr18.writerow([obab,obhit])
obteam1605.close()

wr19.writerow(['5월 넥센 타수','5월 넥센 안타'])
for day in pd.date_range('2016-05-01', '2016-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr19.writerow([ncab,nchit])
ncteam1605.close()

hhteam1606 = open('./hhteam1606.csv', 'w',encoding='utf-8',newline='')
skteam1606 = open('./skteam1606.csv', 'w',encoding='utf-8',newline='')
ktteam1606 = open('./ktteam1606.csv', 'w',encoding='utf-8',newline='')
ltteam1606 = open('./ltteam1606.csv', 'w',encoding='utf-8',newline='')
ssteam1606 = open('./ssteam1606.csv', 'w',encoding='utf-8',newline='')
lgteam1606 = open('./lgteam1606.csv', 'w',encoding='utf-8',newline='')
htteam1606 = open('./htteam1606.csv', 'w',encoding='utf-8',newline='')
woteam1606 = open('./woteam1606.csv', 'w',encoding='utf-8',newline='')
obteam1606 = open('./obteam1606.csv', 'w',encoding='utf-8',newline='')
ncteam1606 = open('./ncteam1606.csv', 'w',encoding='utf-8',newline='')
wr20=csv.writer(hhteam1606)
wr21=csv.writer(skteam1606)
wr22=csv.writer(ktteam1606)
wr23=csv.writer(ltteam1606)
wr24=csv.writer(ssteam1606)
wr25=csv.writer(lgteam1606)
wr26=csv.writer(htteam1606)
wr27=csv.writer(woteam1606)
wr28=csv.writer(obteam1606)
wr29=csv.writer(ncteam1606)

wr20.writerow(['6월 한화 타수','6월 한화 안타'])
for day in pd.date_range('2016-06-01', '2016-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr20.writerow([hhab,hhhit])
hhteam1606.close()

wr21.writerow(['6월 SK 타수','6월 SK 안타'])
for day in pd.date_range('2016-06-01', '2016-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr21.writerow([skab,skhit])
skteam1606.close()

wr22.writerow(['6월 KT 타수','6월 KT 안타'])
for day in pd.date_range('2016-06-01', '2016-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr22.writerow([ktab,kthit])
ktteam1606.close()

wr23.writerow(['6월 롯데 타수','6월 롯데 안타'])
for day in pd.date_range('2016-06-01', '2016-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr23.writerow([ltab,lthit])
ltteam1606.close()

wr24.writerow(['6월 삼성 타수','6월 삼성 안타'])
for day in pd.date_range('2016-06-01', '2016-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr24.writerow([ssab,sshit])
ssteam1606.close()

wr25.writerow(['6월 엘지 타수','6월 엘지 안타'])
for day in pd.date_range('2016-06-01', '2016-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr25.writerow([lgab,lghit])
lgteam1606.close()

wr26.writerow(['6월 기아 타수','6월 기아 안타'])
for day in pd.date_range('2016-06-01', '2016-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr26.writerow([htab,hthit])
htteam1606.close()

wr27.writerow(['6월 키움 타수','6월 키움 안타'])
for day in pd.date_range('2016-06-01', '2016-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr27.writerow([woab,wohit])
woteam1606.close()

wr28.writerow(['6월 두산 타수','6월 두산 안타'])
for day in pd.date_range('2016-06-01', '2016-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr28.writerow([obab,obhit])
obteam1606.close()

wr29.writerow(['6월 넥센 타수','6월 넥센 안타'])
for day in pd.date_range('2016-06-01', '2016-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr29.writerow([ncab,nchit])
ncteam1606.close()

hhteam1607 = open('./hhteam1607.csv', 'w',encoding='utf-8',newline='')
skteam1607 = open('./skteam1607.csv', 'w',encoding='utf-8',newline='')
ktteam1607 = open('./ktteam1607.csv', 'w',encoding='utf-8',newline='')
ltteam1607 = open('./ltteam1607.csv', 'w',encoding='utf-8',newline='')
ssteam1607 = open('./ssteam1607.csv', 'w',encoding='utf-8',newline='')
lgteam1607 = open('./lgteam1607.csv', 'w',encoding='utf-8',newline='')
htteam1607 = open('./htteam1607.csv', 'w',encoding='utf-8',newline='')
woteam1607 = open('./woteam1607.csv', 'w',encoding='utf-8',newline='')
obteam1607 = open('./obteam1607.csv', 'w',encoding='utf-8',newline='')
ncteam1607 = open('./ncteam1607.csv', 'w',encoding='utf-8',newline='')
wr30=csv.writer(hhteam1607)
wr31=csv.writer(skteam1607)
wr32=csv.writer(ktteam1607)
wr33=csv.writer(ltteam1607)
wr34=csv.writer(ssteam1607)
wr35=csv.writer(lgteam1607)
wr36=csv.writer(htteam1607)
wr37=csv.writer(woteam1607)
wr38=csv.writer(obteam1607)
wr39=csv.writer(ncteam1607)

wr30.writerow(['7월 한화 타수','7월 한화 안타'])
for day in pd.date_range('2016-07-01', '2016-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr30.writerow([hhab,hhhit])
hhteam1607.close()

wr31.writerow(['7월 SK 타수','7월 SK 안타'])
for day in pd.date_range('2016-07-01', '2016-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr31.writerow([skab,skhit])
skteam1607.close()

wr32.writerow(['7월 KT 타수','7월 KT 안타'])
for day in pd.date_range('2016-07-01', '2016-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr32.writerow([ktab,kthit])
ktteam1607.close()

wr33.writerow(['7월 롯데 타수','7월 롯데 안타'])
for day in pd.date_range('2016-07-01', '2016-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr33.writerow([ltab,lthit])
ltteam1607.close()

wr34.writerow(['7월 삼성 타수','7월 삼성 안타'])
for day in pd.date_range('2016-07-01', '2016-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr34.writerow([ssab,sshit])
ssteam1607.close()

wr35.writerow(['7월 엘지 타수','7월 엘지 안타'])
for day in pd.date_range('2016-07-01', '2016-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr35.writerow([lgab,lghit])
lgteam1607.close()

wr36.writerow(['7월 기아 타수','7월 기아 안타'])
for day in pd.date_range('2016-07-01', '2016-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr36.writerow([htab,hthit])
htteam1607.close()

wr37.writerow(['7월 키움 타수','7월 키움 안타'])
for day in pd.date_range('2016-07-01', '2016-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr37.writerow([woab,wohit])
woteam1607.close()

wr38.writerow(['7월 두산 타수','7월 두산 안타'])
for day in pd.date_range('2016-07-01', '2016-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr38.writerow([obab,obhit])
obteam1607.close()

wr39.writerow(['7월 넥센 타수','7월 넥센 안타'])
for day in pd.date_range('2016-07-01', '2016-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr39.writerow([ncab,nchit])
ncteam1607.close()

hhteam1608 = open('./hhteam1608.csv', 'w',encoding='utf-8',newline='')
skteam1608 = open('./skteam1608.csv', 'w',encoding='utf-8',newline='')
ktteam1608 = open('./ktteam1608.csv', 'w',encoding='utf-8',newline='')
ltteam1608 = open('./ltteam1608.csv', 'w',encoding='utf-8',newline='')
ssteam1608 = open('./ssteam1608.csv', 'w',encoding='utf-8',newline='')
lgteam1608 = open('./lgteam1608.csv', 'w',encoding='utf-8',newline='')
htteam1608 = open('./htteam1608.csv', 'w',encoding='utf-8',newline='')
woteam1608 = open('./woteam1608.csv', 'w',encoding='utf-8',newline='')
obteam1608 = open('./obteam1608.csv', 'w',encoding='utf-8',newline='')
ncteam1608 = open('./ncteam1608.csv', 'w',encoding='utf-8',newline='')
wr40=csv.writer(hhteam1608)
wr41=csv.writer(skteam1608)
wr42=csv.writer(ktteam1608)
wr43=csv.writer(ltteam1608)
wr44=csv.writer(ssteam1608)
wr45=csv.writer(lgteam1608)
wr46=csv.writer(htteam1608)
wr47=csv.writer(woteam1608)
wr48=csv.writer(obteam1608)
wr49=csv.writer(ncteam1608)

wr40.writerow(['8월 한화 타수','8월 한화 안타'])
for day in pd.date_range('2016-08-01', '2016-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr40.writerow([hhab,hhhit])
hhteam1608.close()

wr41.writerow(['8월 SK 타수','8월 SK 안타'])
for day in pd.date_range('2016-08-01', '2016-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr41.writerow([skab,skhit])
skteam1608.close()

wr42.writerow(['8월 KT 타수','8월 KT 안타'])
for day in pd.date_range('2016-08-01', '2016-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr42.writerow([ktab,kthit])
ktteam1608.close()

wr43.writerow(['8월 롯데 타수','8월 롯데 안타'])
for day in pd.date_range('2016-08-01', '2016-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr43.writerow([ltab,lthit])
ltteam1608.close()

wr44.writerow(['8월 삼성 타수','8월 삼성 안타'])
for day in pd.date_range('2016-08-01', '2016-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr44.writerow([ssab,sshit])
ssteam1608.close()

wr45.writerow(['8월 엘지 타수','8월 엘지 안타'])
for day in pd.date_range('2016-08-01', '2016-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr45.writerow([lgab,lghit])
lgteam1608.close()

wr46.writerow(['8월 기아 타수','8월 기아 안타'])
for day in pd.date_range('2016-08-01', '2016-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr46.writerow([htab,hthit])
htteam1608.close()

wr47.writerow(['8월 키움 타수','8월 키움 안타'])
for day in pd.date_range('2016-08-01', '2016-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr47.writerow([woab,wohit])
woteam1608.close()

wr48.writerow(['8월 두산 타수','8월 두산 안타'])
for day in pd.date_range('2016-08-01', '2016-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr48.writerow([obab,obhit])
obteam1608.close()

wr49.writerow(['8월 넥센 타수','8월 넥센 안타'])
for day in pd.date_range('2016-08-01', '2016-08-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr49.writerow([ncab,nchit])
ncteam1608.close()

hhteam1609 = open('./hhteam1609.csv', 'w',encoding='utf-8',newline='')
skteam1609 = open('./skteam1609.csv', 'w',encoding='utf-8',newline='')
ktteam1609 = open('./ktteam1609.csv', 'w',encoding='utf-8',newline='')
ltteam1609 = open('./ltteam1609.csv', 'w',encoding='utf-8',newline='')
ssteam1609 = open('./ssteam1609.csv', 'w',encoding='utf-8',newline='')
lgteam1609 = open('./lgteam1609.csv', 'w',encoding='utf-8',newline='')
htteam1609 = open('./htteam1609.csv', 'w',encoding='utf-8',newline='')
woteam1609 = open('./woteam1609.csv', 'w',encoding='utf-8',newline='')
obteam1609 = open('./obteam1609.csv', 'w',encoding='utf-8',newline='')
ncteam1609 = open('./ncteam1609.csv', 'w',encoding='utf-8',newline='')
wr50=csv.writer(hhteam1609)
wr51=csv.writer(skteam1609)
wr52=csv.writer(ktteam1609)
wr53=csv.writer(ltteam1609)
wr54=csv.writer(ssteam1609)
wr55=csv.writer(lgteam1609)
wr56=csv.writer(htteam1609)
wr57=csv.writer(woteam1609)
wr58=csv.writer(obteam1609)
wr59=csv.writer(ncteam1609)

wr50.writerow(['9월 한화 타수','9월 한화 안타'])
for day in pd.date_range('2016-09-01', '2016-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr50.writerow([hhab,hhhit])
hhteam1609.close()

wr51.writerow(['9월 SK 타수','9월 SK 안타'])
for day in pd.date_range('2016-09-01', '2016-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr51.writerow([skab,skhit])
skteam1609.close()

wr52.writerow(['9월 KT 타수','9월 KT 안타'])
for day in pd.date_range('2016-09-01', '2016-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr52.writerow([ktab,kthit])
ktteam1609.close()

wr53.writerow(['9월 롯데 타수','9월 롯데 안타'])
for day in pd.date_range('2016-09-01', '2016-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr53.writerow([ltab,lthit])
ltteam1609.close()

wr54.writerow(['9월 삼성 타수','9월 삼성 안타'])
for day in pd.date_range('2016-09-01', '2016-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr54.writerow([ssab,sshit])
ssteam1609.close()

wr55.writerow(['9월 엘지 타수','9월 엘지 안타'])
for day in pd.date_range('2016-09-01', '2016-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr55.writerow([lgab,lghit])
lgteam1609.close()

wr56.writerow(['9월 기아 타수','9월 기아 안타'])
for day in pd.date_range('2016-09-01', '2016-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr56.writerow([htab,hthit])
htteam1609.close()

wr57.writerow(['9월 키움 타수','9월 키움 안타'])
for day in pd.date_range('2016-09-01', '2016-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr57.writerow([woab,wohit])
woteam1609.close()

wr58.writerow(['9월 두산 타수','9월 두산 안타'])
for day in pd.date_range('2016-09-01', '2016-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr58.writerow([obab,obhit])
obteam1609.close()

wr59.writerow(['9월 넥센 타수','9월 넥센 안타'])
for day in pd.date_range('2016-09-01', '2016-09-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr59.writerow([ncab,nchit])
ncteam1609.close()
# 데이터 정렬 , 기본값이 오름차순이고 ,ascending=[0]을 추가하면 내림차순이 된다.

hhteam1610 = open('./hhteam1610.csv', 'w',encoding='utf-8',newline='')
skteam1610 = open('./skteam1610.csv', 'w',encoding='utf-8',newline='')
ktteam1610 = open('./ktteam1610.csv', 'w',encoding='utf-8',newline='')
ltteam1610 = open('./ltteam1610.csv', 'w',encoding='utf-8',newline='')
ssteam1610 = open('./ssteam1610.csv', 'w',encoding='utf-8',newline='')
lgteam1610 = open('./lgteam1610.csv', 'w',encoding='utf-8',newline='')
htteam1610 = open('./htteam1610.csv', 'w',encoding='utf-8',newline='')
woteam1610 = open('./woteam1610.csv', 'w',encoding='utf-8',newline='')
obteam1610 = open('./obteam1610.csv', 'w',encoding='utf-8',newline='')
ncteam1610 = open('./ncteam1610.csv', 'w',encoding='utf-8',newline='')
wr60=csv.writer(hhteam1610)
wr61=csv.writer(skteam1610)
wr62=csv.writer(ktteam1610)
wr63=csv.writer(ltteam1610)
wr64=csv.writer(ssteam1610)
wr65=csv.writer(lgteam1610)
wr66=csv.writer(htteam1610)
wr67=csv.writer(woteam1610)
wr68=csv.writer(obteam1610)
wr69=csv.writer(ncteam1610)

wr60.writerow(['10월 한화 타수','10월 한화 안타'])
for day in pd.date_range('2016-10-01', '2016-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr60.writerow([hhab,hhhit])
hhteam1610.close()

wr61.writerow(['10월 SK 타수','10월 SK 안타'])
for day in pd.date_range('2016-10-01', '2016-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr61.writerow([skab,skhit])
skteam1610.close()

wr62.writerow(['10월 KT 타수','10월 KT 안타'])
for day in pd.date_range('2016-10-01', '2016-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr62.writerow([ktab,kthit])
ktteam1610.close()

wr63.writerow(['10월 롯데 타수','10월 롯데 안타'])
for day in pd.date_range('2016-10-01', '2016-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr63.writerow([ltab,lthit])
ltteam1610.close()

wr64.writerow(['10월 삼성 타수','10월 삼성 안타'])
for day in pd.date_range('2016-10-01', '2016-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr64.writerow([ssab,sshit])
ssteam1610.close()

wr65.writerow(['10월 엘지 타수','10월 엘지 안타'])
for day in pd.date_range('2016-10-01', '2016-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr65.writerow([lgab,lghit])
lgteam1610.close()

wr66.writerow(['10월 기아 타수','10월 기아 안타'])
for day in pd.date_range('2016-10-01', '2016-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr66.writerow([htab,hthit])
htteam1610.close()

wr67.writerow(['10월 키움 타수','10월 키움 안타'])
for day in pd.date_range('2016-10-01', '2016-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr67.writerow([woab,wohit])
woteam1610.close()

wr68.writerow(['10월 두산 타수','10월 두산 안타'])
for day in pd.date_range('2016-10-01', '2016-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr68.writerow([obab,obhit])
obteam1610.close()

wr69.writerow(['10월 넥센 타수','10월 넥센 안타'])
for day in pd.date_range('2016-10-01', '2016-10-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata16[(teamdata16.GDAY_DS == daynum) & (teamdata16.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr69.writerow([ncab,nchit])
ncteam1610.close()

hhta=pd.read_csv('./hhteam1604.csv')
hhta=hhta.sum()
hhtata=hhta.iloc[1]/hhta.iloc[0]
hhtata=pd.Series([hhtata],index=['4월'])

skta=pd.read_csv('./skteam1604.csv')
skta=skta.sum()
sktata=skta.iloc[1]/skta.iloc[0]
sktata=pd.Series([sktata],index=['4월'])

ktta=pd.read_csv('./ktteam1604.csv')
ktta=ktta.sum()
kttata=ktta.iloc[1]/ktta.iloc[0]
kttata=pd.Series([kttata],index=['4월'])

ltta=pd.read_csv('./ltteam1604.csv')
ltta=ltta.sum()
lttata=ltta.iloc[1]/ltta.iloc[0]
lttata=pd.Series([lttata],index=['4월'])

ssta=pd.read_csv('./ssteam1604.csv')
ssta=ssta.sum()
sstata=ssta.iloc[1]/ssta.iloc[0]
sstata=pd.Series([sstata],index=['4월'])

lgta=pd.read_csv('./lgteam1604.csv')
lgta=lgta.sum()
lgtata=lgta.iloc[1]/lgta.iloc[0]
lgtata=pd.Series([lgtata],index=['4월'])

htta=pd.read_csv('./htteam1604.csv')
htta=htta.sum()
httata=htta.iloc[1]/htta.iloc[0]
httata=pd.Series([httata],index=['4월'])

wota=pd.read_csv('./woteam1604.csv')
wota=wota.sum()
wotata=wota.iloc[1]/wota.iloc[0]
wotata=pd.Series([wotata],index=['4월'])

obta=pd.read_csv('./obteam1604.csv')
obta=obta.sum()
obtata=obta.iloc[1]/obta.iloc[0]
obtata=pd.Series([obtata],index=['4월'])

ncta=pd.read_csv('./ncteam1604.csv')
ncta=ncta.sum()
nctata=ncta.iloc[1]/ncta.iloc[0]
nctata=pd.Series([nctata],index=['4월'])
data1604=pd.concat([hhtata,sktata,kttata,lttata,sstata,lgtata,httata,wotata,obtata,nctata],axis=1)
print(data1604)

hhta1=pd.read_csv('./hhteam1605.csv')
hhta1=hhta1.sum()
hhtata1=hhta1.iloc[1]/hhta1.iloc[0]
hhtata1=pd.Series([hhtata1],index=['5월'])

skta1=pd.read_csv('./skteam1605.csv')
skta1=skta1.sum()
sktata1=skta1.iloc[1]/skta1.iloc[0]
sktata1=pd.Series([sktata1],index=['5월'])

ktta1=pd.read_csv('./ktteam1605.csv')
ktta1=ktta1.sum()
kttata1=ktta1.iloc[1]/ktta1.iloc[0]
kttata1=pd.Series([kttata1],index=['5월'])

ltta1=pd.read_csv('./ltteam1605.csv')
ltta1=ltta1.sum()
lttata1=ltta1.iloc[1]/ltta1.iloc[0]
lttata1=pd.Series([lttata1],index=['5월'])

ssta1=pd.read_csv('./ssteam1605.csv')
ssta1=ssta1.sum()
sstata1=ssta1.iloc[1]/ssta1.iloc[0]
sstata1=pd.Series([sstata1],index=['5월'])

lgta1=pd.read_csv('./lgteam1605.csv')
lgta1=lgta1.sum()
lgtata1=lgta1.iloc[1]/lgta1.iloc[0]
lgtata1=pd.Series([lgtata1],index=['5월'])

htta1=pd.read_csv('./htteam1605.csv')
htta1=htta1.sum()
httata1=htta1.iloc[1]/htta1.iloc[0]
httata1=pd.Series([httata1],index=['5월'])

wota1=pd.read_csv('./woteam1605.csv')
wota1=wota1.sum()
wotata1=wota1.iloc[1]/wota1.iloc[0]
wotata1=pd.Series([wotata1],index=['5월'])

obta1=pd.read_csv('./obteam1605.csv')
obta1=obta1.sum()
obtata1=obta1.iloc[1]/obta1.iloc[0]
obtata1=pd.Series([obtata1],index=['5월'])

ncta1=pd.read_csv('./ncteam1605.csv')
ncta1=ncta1.sum()
nctata1=ncta1.iloc[1]/ncta1.iloc[0]
nctata1=pd.Series([nctata1],index=['5월'])
data1605=pd.concat([hhtata1,sktata1,kttata1,lttata1,sstata1,lgtata1,httata1,wotata1,obtata1,nctata1],axis=1)
print(data1605)

hhta2=pd.read_csv('./hhteam1606.csv')
hhta2=hhta2.sum()
hhtata2=hhta2.iloc[1]/hhta2.iloc[0]
hhtata2=pd.Series([hhtata2],index=['6월'])

skta2=pd.read_csv('./skteam1606.csv')
skta2=skta2.sum()
sktata2=skta2.iloc[1]/skta2.iloc[0]
sktata2=pd.Series([sktata2],index=['6월'])

ktta2=pd.read_csv('./ktteam1606.csv')
ktta2=ktta2.sum()
kttata2=ktta2.iloc[1]/ktta2.iloc[0]
kttata2=pd.Series([kttata2],index=['6월'])

ltta2=pd.read_csv('./ltteam1606.csv')
ltta2=ltta2.sum()
lttata2=ltta2.iloc[1]/ltta2.iloc[0]
lttata2=pd.Series([lttata2],index=['6월'])

ssta2=pd.read_csv('./ssteam1606.csv')
ssta2=ssta2.sum()
sstata2=ssta2.iloc[1]/ssta2.iloc[0]
sstata2=pd.Series([sstata2],index=['6월'])

lgta2=pd.read_csv('./lgteam1606.csv')
lgta2=lgta2.sum()
lgtata2=lgta2.iloc[1]/lgta2.iloc[0]
lgtata2=pd.Series([lgtata2],index=['6월'])

htta2=pd.read_csv('./htteam1606.csv')
htta2=htta2.sum()
httata2=htta2.iloc[1]/htta2.iloc[0]
httata2=pd.Series([httata2],index=['6월'])

wota2=pd.read_csv('./woteam1606.csv')
wota2=wota2.sum()
wotata2=wota2.iloc[1]/wota2.iloc[0]
wotata2=pd.Series([wotata2],index=['6월'])

obta2=pd.read_csv('./obteam1606.csv')
obta2=obta2.sum()
obtata2=obta2.iloc[1]/obta2.iloc[0]
obtata2=pd.Series([obtata2],index=['6월'])

ncta2=pd.read_csv('./ncteam1606.csv')
ncta2=ncta2.sum()
nctata2=ncta2.iloc[1]/ncta2.iloc[0]
nctata2=pd.Series([nctata2],index=['6월'])
data1606=pd.concat([hhtata2,sktata2,kttata2,lttata2,sstata2,lgtata2,httata2,wotata2,obtata2,nctata2],axis=1)
print(data1606)

hhta3=pd.read_csv('./hhteam1607.csv')
hhta3=hhta3.sum()
hhtata3=hhta3.iloc[1]/hhta3.iloc[0]
hhtata3=pd.Series([hhtata3],index=['7월'])

skta3=pd.read_csv('./skteam1607.csv')
skta3=skta3.sum()
sktata3=skta3.iloc[1]/skta3.iloc[0]
sktata3=pd.Series([sktata3],index=['7월'])

ktta3=pd.read_csv('./ktteam1607.csv')
ktta3=ktta3.sum()
kttata3=ktta3.iloc[1]/ktta3.iloc[0]
kttata3=pd.Series([kttata3],index=['7월'])

ltta3=pd.read_csv('./ltteam1607.csv')
ltta3=ltta3.sum()
lttata3=ltta3.iloc[1]/ltta3.iloc[0]
lttata3=pd.Series([lttata3],index=['7월'])

ssta3=pd.read_csv('./ssteam1607.csv')
ssta3=ssta3.sum()
sstata3=ssta3.iloc[1]/ssta3.iloc[0]
sstata3=pd.Series([sstata3],index=['7월'])

lgta3=pd.read_csv('./lgteam1607.csv')
lgta3=lgta3.sum()
lgtata3=lgta3.iloc[1]/lgta3.iloc[0]
lgtata3=pd.Series([lgtata3],index=['7월'])

htta3=pd.read_csv('./htteam1607.csv')
htta3=htta3.sum()
httata3=htta3.iloc[1]/htta3.iloc[0]
httata3=pd.Series([httata3],index=['7월'])

wota3=pd.read_csv('./woteam1607.csv')
wota3=wota3.sum()
wotata3=wota3.iloc[1]/wota3.iloc[0]
wotata3=pd.Series([wotata3],index=['7월'])

obta3=pd.read_csv('./obteam1607.csv')
obta3=obta3.sum()
obtata3=obta3.iloc[1]/obta3.iloc[0]
obtata3=pd.Series([obtata3],index=['7월'])

ncta3=pd.read_csv('./ncteam1607.csv')
ncta3=ncta3.sum()
nctata3=ncta3.iloc[1]/ncta3.iloc[0]
nctata3=pd.Series([nctata3],index=['7월'])
data1607=pd.concat([hhtata3,sktata3,kttata3,lttata3,sstata3,lgtata3,httata3,wotata3,obtata3,nctata3],axis=1)
print(data1607)

hhta4=pd.read_csv('./hhteam1608.csv')
hhta4=hhta4.sum()
hhtata4=hhta4.iloc[1]/hhta4.iloc[0]
hhtata4=pd.Series([hhtata4],index=['8월'])

skta4=pd.read_csv('./skteam1608.csv')
skta4=skta4.sum()
sktata4=skta4.iloc[1]/skta4.iloc[0]
sktata4=pd.Series([sktata4],index=['8월'])

ktta4=pd.read_csv('./ktteam1608.csv')
ktta4=ktta4.sum()
kttata4=ktta4.iloc[1]/ktta4.iloc[0]
kttata4=pd.Series([kttata4],index=['8월'])

ltta4=pd.read_csv('./ltteam1608.csv')
ltta4=ltta4.sum()
lttata4=ltta4.iloc[1]/ltta4.iloc[0]
lttata4=pd.Series([lttata4],index=['8월'])

ssta4=pd.read_csv('./ssteam1608.csv')
ssta4=ssta4.sum()
sstata4=ssta4.iloc[1]/ssta4.iloc[0]
sstata4=pd.Series([sstata4],index=['8월'])

lgta4=pd.read_csv('./lgteam1608.csv')
lgta4=lgta4.sum()
lgtata4=lgta4.iloc[1]/lgta4.iloc[0]
lgtata4=pd.Series([lgtata4],index=['8월'])

htta4=pd.read_csv('./htteam1608.csv')
htta4=htta4.sum()
httata4=htta4.iloc[1]/htta4.iloc[0]
httata4=pd.Series([httata4],index=['8월'])

wota4=pd.read_csv('./woteam1608.csv')
wota4=wota4.sum()
wotata4=wota4.iloc[1]/wota4.iloc[0]
wotata4=pd.Series([wotata4],index=['8월'])

obta4=pd.read_csv('./obteam1608.csv')
obta4=obta4.sum()
obtata4=obta4.iloc[1]/obta4.iloc[0]
obtata4=pd.Series([obtata4],index=['8월'])

ncta4=pd.read_csv('./ncteam1608.csv')
ncta4=ncta4.sum()
nctata4=ncta4.iloc[1]/ncta4.iloc[0]
nctata4=pd.Series([nctata4],index=['8월'])
data1608=pd.concat([hhtata4,sktata4,kttata4,lttata4,sstata4,lgtata4,httata4,wotata4,obtata4,nctata4],axis=1)
print(data1608)

hhta5=pd.read_csv('./hhteam1609.csv')
hhta5=hhta5.sum()
hhtata5=hhta5.iloc[1]/hhta5.iloc[0]
hhtata5=pd.Series([hhtata5],index=['9월'])

skta5=pd.read_csv('./skteam1609.csv')
skta5=skta5.sum()
sktata5=skta5.iloc[1]/skta5.iloc[0]
sktata5=pd.Series([sktata5],index=['9월'])

ktta5=pd.read_csv('./ktteam1609.csv')
ktta5=ktta5.sum()
kttata5=ktta5.iloc[1]/ktta5.iloc[0]
kttata5=pd.Series([kttata5],index=['9월'])

ltta5=pd.read_csv('./ltteam1609.csv')
ltta5=ltta5.sum()
lttata5=ltta5.iloc[1]/ltta5.iloc[0]
lttata5=pd.Series([lttata5],index=['9월'])

ssta5=pd.read_csv('./ssteam1609.csv')
ssta5=ssta5.sum()
sstata5=ssta5.iloc[1]/ssta5.iloc[0]
sstata5=pd.Series([sstata5],index=['9월'])

lgta5=pd.read_csv('./lgteam1609.csv')
lgta5=lgta5.sum()
lgtata5=lgta5.iloc[1]/lgta5.iloc[0]
lgtata5=pd.Series([lgtata5],index=['9월'])

htta5=pd.read_csv('./htteam1609.csv')
htta5=htta5.sum()
httata5=htta5.iloc[1]/htta5.iloc[0]
httata5=pd.Series([httata5],index=['9월'])

wota5=pd.read_csv('./woteam1609.csv')
wota5=wota5.sum()
wotata5=wota5.iloc[1]/wota5.iloc[0]
wotata5=pd.Series([wotata5],index=['9월'])

obta5=pd.read_csv('./obteam1609.csv')
obta5=obta5.sum()
obtata5=obta5.iloc[1]/obta5.iloc[0]
obtata5=pd.Series([obtata5],index=['9월'])

ncta5=pd.read_csv('./ncteam1609.csv')
ncta5=ncta5.sum()
nctata5=ncta5.iloc[1]/ncta5.iloc[0]
nctata5=pd.Series([nctata5],index=['9월'])
data1609=pd.concat([hhtata5,sktata5,kttata5,lttata5,sstata5,lgtata5,httata5,wotata5,obtata5,nctata5],axis=1)
print(data1609)

hhta6=pd.read_csv('./hhteam1610.csv')
hhta6=hhta6.sum()
hhtata6=hhta6.iloc[1]/hhta6.iloc[0]
hhtata6=pd.Series([hhtata6],index=['10월'])

skta6=pd.read_csv('./skteam1610.csv')
skta6=skta6.sum()
sktata6=skta6.iloc[1]/skta6.iloc[0]
sktata6=pd.Series([sktata6],index=['10월'])

ktta6=pd.read_csv('./ktteam1610.csv')
ktta6=ktta6.sum()
kttata6=ktta6.iloc[1]/ktta6.iloc[0]
kttata6=pd.Series([kttata6],index=['10월'])

ltta6=pd.read_csv('./ltteam1610.csv')
ltta6=ltta6.sum()
lttata6=ltta6.iloc[1]/ltta6.iloc[0]
lttata6=pd.Series([lttata6],index=['10월'])

ssta6=pd.read_csv('./ssteam1610.csv')
ssta6=ssta6.sum()
sstata6=ssta6.iloc[1]/ssta6.iloc[0]
sstata6=pd.Series([sstata6],index=['10월'])

lgta6=pd.read_csv('./lgteam1610.csv')
lgta6=lgta6.sum()
lgtata6=lgta6.iloc[1]/lgta6.iloc[0]
lgtata6=pd.Series([lgtata6],index=['10월'])

htta6=pd.read_csv('./htteam1610.csv')
htta6=htta6.sum()
httata6=htta6.iloc[1]/htta6.iloc[0]
httata6=pd.Series([httata6],index=['10월'])

wota6=pd.read_csv('./woteam1610.csv')
wota6=wota6.sum()
wotata6=wota6.iloc[1]/wota6.iloc[0]
wotata6=pd.Series([wotata6],index=['10월'])

obta6=pd.read_csv('./obteam1610.csv')
obta6=obta6.sum()
obtata6=obta6.iloc[1]/obta6.iloc[0]
obtata6=pd.Series([obtata6],index=['10월'])

ncta6=pd.read_csv('./ncteam1610.csv')
ncta6=ncta6.sum()
nctata6=ncta6.iloc[1]/ncta6.iloc[0]
nctata6=pd.Series([nctata6],index=['10월'])
data1610=pd.concat([hhtata6,sktata6,kttata6,lttata6,sstata6,lgtata6,httata6,wotata6,obtata6,nctata6],axis=1)
print(data1610)

dataset16=pd.concat([data1604,data1605,data1606,data1607,data1608,data1609,data1610],axis=0)
dataset16=dataset16.rename(columns={0:'한화',1:'SK',2:'KT',3:'롯데',4:'삼성',5:'엘지',6:'기아',7:'키움',8:'두산',9:'넥센'})
print(dataset16)
#team=['SK','KT','LT','HH','SS','LG','HT','WO','OB','NC']

dataset16.to_csv('./dataframe16.csv',index_label='경기날짜')

