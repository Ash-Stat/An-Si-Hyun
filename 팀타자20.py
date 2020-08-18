import pandas as pd
import numpy as np
import csv

teamdata20=pd.read_csv('./팀타자20.csv')
teamdata20=teamdata20[['GDAY_DS','T_ID','HIT','AB']]
teamdata20=teamdata20.sort_values(['GDAY_DS','T_ID'])
#team=['SK','KT','LT','HH','SS','LG','HT','WO','OB','NC']

hhteam2005 = open('./hhteam2005.csv', 'w',encoding='utf-8',newline='')
skteam2005 = open('./skteam2005.csv', 'w',encoding='utf-8',newline='')
ktteam2005 = open('./ktteam2005.csv', 'w',encoding='utf-8',newline='')
ltteam2005 = open('./ltteam2005.csv', 'w',encoding='utf-8',newline='')
ssteam2005 = open('./ssteam2005.csv', 'w',encoding='utf-8',newline='')
lgteam2005 = open('./lgteam2005.csv', 'w',encoding='utf-8',newline='')
htteam2005 = open('./htteam2005.csv', 'w',encoding='utf-8',newline='')
woteam2005 = open('./woteam2005.csv', 'w',encoding='utf-8',newline='')
obteam2005 = open('./obteam2005.csv', 'w',encoding='utf-8',newline='')
ncteam2005 = open('./ncteam2005.csv', 'w',encoding='utf-8',newline='')
wr10=csv.writer(hhteam2005)
wr11=csv.writer(skteam2005)
wr12=csv.writer(ktteam2005)
wr13=csv.writer(ltteam2005)
wr14=csv.writer(ssteam2005)
wr15=csv.writer(lgteam2005)
wr16=csv.writer(htteam2005)
wr17=csv.writer(woteam2005)
wr18=csv.writer(obteam2005)
wr19=csv.writer(ncteam2005)

wr10.writerow(['5월 한화 타수','5월 한화 안타'])
for day in pd.date_range('2020-05-01', '2020-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr10.writerow([hhab,hhhit])
hhteam2005.close()

wr11.writerow(['5월 SK 타수','5월 SK 안타'])
for day in pd.date_range('2020-05-01', '2020-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr11.writerow([skab,skhit])
skteam2005.close()

wr12.writerow(['5월 KT 타수','5월 KT 안타'])
for day in pd.date_range('2020-05-01', '2020-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr12.writerow([ktab,kthit])
ktteam2005.close()

wr13.writerow(['5월 롯데 타수','5월 롯데 안타'])
for day in pd.date_range('2020-05-01', '2020-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr13.writerow([ltab,lthit])
ltteam2005.close()

wr14.writerow(['5월 삼성 타수','5월 삼성 안타'])
for day in pd.date_range('2020-05-01', '2020-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr14.writerow([ssab,sshit])
ssteam2005.close()

wr15.writerow(['5월 엘지 타수','5월 엘지 안타'])
for day in pd.date_range('2020-05-01', '2020-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr15.writerow([lgab,lghit])
lgteam2005.close()

wr16.writerow(['5월 기아 타수','5월 기아 안타'])
for day in pd.date_range('2020-05-01', '2020-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr16.writerow([htab,hthit])
htteam2005.close()

wr17.writerow(['5월 키움 타수','5월 키움 안타'])
for day in pd.date_range('2020-05-01', '2020-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr17.writerow([woab,wohit])
woteam2005.close()

wr18.writerow(['5월 두산 타수','5월 두산 안타'])
for day in pd.date_range('2020-05-01', '2020-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr18.writerow([obab,obhit])
obteam2005.close()

wr19.writerow(['5월 넥센 타수','5월 넥센 안타'])
for day in pd.date_range('2020-05-01', '2020-05-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr19.writerow([ncab,nchit])
ncteam2005.close()

hhteam2006 = open('./hhteam2006.csv', 'w',encoding='utf-8',newline='')
skteam2006 = open('./skteam2006.csv', 'w',encoding='utf-8',newline='')
ktteam2006 = open('./ktteam2006.csv', 'w',encoding='utf-8',newline='')
ltteam2006 = open('./ltteam2006.csv', 'w',encoding='utf-8',newline='')
ssteam2006 = open('./ssteam2006.csv', 'w',encoding='utf-8',newline='')
lgteam2006 = open('./lgteam2006.csv', 'w',encoding='utf-8',newline='')
htteam2006 = open('./htteam2006.csv', 'w',encoding='utf-8',newline='')
woteam2006 = open('./woteam2006.csv', 'w',encoding='utf-8',newline='')
obteam2006 = open('./obteam2006.csv', 'w',encoding='utf-8',newline='')
ncteam2006 = open('./ncteam2006.csv', 'w',encoding='utf-8',newline='')
wr20=csv.writer(hhteam2006)
wr21=csv.writer(skteam2006)
wr22=csv.writer(ktteam2006)
wr23=csv.writer(ltteam2006)
wr24=csv.writer(ssteam2006)
wr25=csv.writer(lgteam2006)
wr26=csv.writer(htteam2006)
wr27=csv.writer(woteam2006)
wr28=csv.writer(obteam2006)
wr29=csv.writer(ncteam2006)

wr20.writerow(['6월 한화 타수','6월 한화 안타'])
for day in pd.date_range('2020-06-01', '2020-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr20.writerow([hhab,hhhit])
hhteam2006.close()

wr21.writerow(['6월 SK 타수','6월 SK 안타'])
for day in pd.date_range('2020-06-01', '2020-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr21.writerow([skab,skhit])
skteam2006.close()

wr22.writerow(['6월 KT 타수','6월 KT 안타'])
for day in pd.date_range('2020-06-01', '2020-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr22.writerow([ktab,kthit])
ktteam2006.close()

wr23.writerow(['6월 롯데 타수','6월 롯데 안타'])
for day in pd.date_range('2020-06-01', '2020-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr23.writerow([ltab,lthit])
ltteam2006.close()

wr24.writerow(['6월 삼성 타수','6월 삼성 안타'])
for day in pd.date_range('2020-06-01', '2020-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr24.writerow([ssab,sshit])
ssteam2006.close()

wr25.writerow(['6월 엘지 타수','6월 엘지 안타'])
for day in pd.date_range('2020-06-01', '2020-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr25.writerow([lgab,lghit])
lgteam2006.close()

wr26.writerow(['6월 기아 타수','6월 기아 안타'])
for day in pd.date_range('2020-06-01', '2020-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr26.writerow([htab,hthit])
htteam2006.close()

wr27.writerow(['6월 키움 타수','6월 키움 안타'])
for day in pd.date_range('2020-06-01', '2020-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr27.writerow([woab,wohit])
woteam2006.close()

wr28.writerow(['6월 두산 타수','6월 두산 안타'])
for day in pd.date_range('2020-06-01', '2020-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr28.writerow([obab,obhit])
obteam2006.close()

wr29.writerow(['6월 넥센 타수','6월 넥센 안타'])
for day in pd.date_range('2020-06-01', '2020-06-30'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr29.writerow([ncab,nchit])
ncteam2006.close()

hhteam2007 = open('./hhteam2007.csv', 'w',encoding='utf-8',newline='')
skteam2007 = open('./skteam2007.csv', 'w',encoding='utf-8',newline='')
ktteam2007 = open('./ktteam2007.csv', 'w',encoding='utf-8',newline='')
ltteam2007 = open('./ltteam2007.csv', 'w',encoding='utf-8',newline='')
ssteam2007 = open('./ssteam2007.csv', 'w',encoding='utf-8',newline='')
lgteam2007 = open('./lgteam2007.csv', 'w',encoding='utf-8',newline='')
htteam2007 = open('./htteam2007.csv', 'w',encoding='utf-8',newline='')
woteam2007 = open('./woteam2007.csv', 'w',encoding='utf-8',newline='')
obteam2007 = open('./obteam2007.csv', 'w',encoding='utf-8',newline='')
ncteam2007 = open('./ncteam2007.csv', 'w',encoding='utf-8',newline='')
wr30=csv.writer(hhteam2007)
wr31=csv.writer(skteam2007)
wr32=csv.writer(ktteam2007)
wr33=csv.writer(ltteam2007)
wr34=csv.writer(ssteam2007)
wr35=csv.writer(lgteam2007)
wr36=csv.writer(htteam2007)
wr37=csv.writer(woteam2007)
wr38=csv.writer(obteam2007)
wr39=csv.writer(ncteam2007)

wr30.writerow(['7월 한화 타수','7월 한화 안타'])
for day in pd.date_range('2020-07-01', '2020-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    hh = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'HH')]
    hhab=hh.AB.sum()
    hhhit=hh.HIT.sum()
    wr30.writerow([hhab,hhhit])
hhteam2007.close()

wr31.writerow(['7월 SK 타수','7월 SK 안타'])
for day in pd.date_range('2020-07-01', '2020-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    sk = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'SK')]
    skab=sk.AB.sum()
    skhit=sk.HIT.sum()
    wr31.writerow([skab,skhit])
skteam2007.close()

wr32.writerow(['7월 KT 타수','7월 KT 안타'])
for day in pd.date_range('2020-07-01', '2020-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    kt = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'KT')]
    ktab=kt.AB.sum()
    kthit=kt.HIT.sum()
    wr32.writerow([ktab,kthit])
ktteam2007.close()

wr33.writerow(['7월 롯데 타수','7월 롯데 안타'])
for day in pd.date_range('2020-07-01', '2020-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lt = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'LT')]
    ltab=lt.AB.sum()
    lthit=lt.HIT.sum()
    wr33.writerow([ltab,lthit])
ltteam2007.close()

wr34.writerow(['7월 삼성 타수','7월 삼성 안타'])
for day in pd.date_range('2020-07-01', '2020-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ss = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'SS')]
    ssab=ss.AB.sum()
    sshit=ss.HIT.sum()
    wr34.writerow([ssab,sshit])
ssteam2007.close()

wr35.writerow(['7월 엘지 타수','7월 엘지 안타'])
for day in pd.date_range('2020-07-01', '2020-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    lg = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'LG')]
    lgab=lg.AB.sum()
    lghit=lg.HIT.sum()
    wr35.writerow([lgab,lghit])
lgteam2007.close()

wr36.writerow(['7월 기아 타수','7월 기아 안타'])
for day in pd.date_range('2020-07-01', '2020-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ht = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'HT')]
    htab=ht.AB.sum()
    hthit=ht.HIT.sum()
    wr36.writerow([htab,hthit])
htteam2007.close()

wr37.writerow(['7월 키움 타수','7월 키움 안타'])
for day in pd.date_range('2020-07-01', '2020-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    wo = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'WO')]
    woab=wo.AB.sum()
    wohit=wo.HIT.sum()
    wr37.writerow([woab,wohit])
woteam2007.close()

wr38.writerow(['7월 두산 타수','7월 두산 안타'])
for day in pd.date_range('2020-07-01', '2020-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    ob = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'OB')]
    obab=ob.AB.sum()
    obhit=ob.HIT.sum()
    wr38.writerow([obab,obhit])
obteam2007.close()

wr39.writerow(['7월 넥센 타수','7월 넥센 안타'])
for day in pd.date_range('2020-07-01', '2020-07-31'):
    daynum = day.year * 10000 + day.month * 100 + day.day
    nc = teamdata20[(teamdata20.GDAY_DS == daynum) & (teamdata20.T_ID == 'NC')]
    ncab=nc.AB.sum()
    nchit=nc.HIT.sum()
    wr39.writerow([ncab,nchit])
ncteam2007.close()

hhta1=pd.read_csv('./hhteam2005.csv')
hhta1=hhta1.sum()
hhtata1=hhta1.iloc[1]/hhta1.iloc[0]
hhtata1=pd.Series([hhtata1],index=['5월'])

skta1=pd.read_csv('./skteam2005.csv')
skta1=skta1.sum()
sktata1=skta1.iloc[1]/skta1.iloc[0]
sktata1=pd.Series([sktata1],index=['5월'])

ktta1=pd.read_csv('./ktteam2005.csv')
ktta1=ktta1.sum()
kttata1=ktta1.iloc[1]/ktta1.iloc[0]
kttata1=pd.Series([kttata1],index=['5월'])

ltta1=pd.read_csv('./ltteam2005.csv')
ltta1=ltta1.sum()
lttata1=ltta1.iloc[1]/ltta1.iloc[0]
lttata1=pd.Series([lttata1],index=['5월'])

ssta1=pd.read_csv('./ssteam2005.csv')
ssta1=ssta1.sum()
sstata1=ssta1.iloc[1]/ssta1.iloc[0]
sstata1=pd.Series([sstata1],index=['5월'])

lgta1=pd.read_csv('./lgteam2005.csv')
lgta1=lgta1.sum()
lgtata1=lgta1.iloc[1]/lgta1.iloc[0]
lgtata1=pd.Series([lgtata1],index=['5월'])

htta1=pd.read_csv('./htteam2005.csv')
htta1=htta1.sum()
httata1=htta1.iloc[1]/htta1.iloc[0]
httata1=pd.Series([httata1],index=['5월'])

wota1=pd.read_csv('./woteam2005.csv')
wota1=wota1.sum()
wotata1=wota1.iloc[1]/wota1.iloc[0]
wotata1=pd.Series([wotata1],index=['5월'])

obta1=pd.read_csv('./obteam2005.csv')
obta1=obta1.sum()
obtata1=obta1.iloc[1]/obta1.iloc[0]
obtata1=pd.Series([obtata1],index=['5월'])

ncta1=pd.read_csv('./ncteam2005.csv')
ncta1=ncta1.sum()
nctata1=ncta1.iloc[1]/ncta1.iloc[0]
nctata1=pd.Series([nctata1],index=['5월'])
data2005=pd.concat([hhtata1,sktata1,kttata1,lttata1,sstata1,lgtata1,httata1,wotata1,obtata1,nctata1],axis=1)
print(data2005)

hhta2=pd.read_csv('./hhteam2006.csv')
hhta2=hhta2.sum()
hhtata2=hhta2.iloc[1]/hhta2.iloc[0]
hhtata2=pd.Series([hhtata2],index=['6월'])

skta2=pd.read_csv('./skteam2006.csv')
skta2=skta2.sum()
sktata2=skta2.iloc[1]/skta2.iloc[0]
sktata2=pd.Series([sktata2],index=['6월'])

ktta2=pd.read_csv('./ktteam2006.csv')
ktta2=ktta2.sum()
kttata2=ktta2.iloc[1]/ktta2.iloc[0]
kttata2=pd.Series([kttata2],index=['6월'])

ltta2=pd.read_csv('./ltteam2006.csv')
ltta2=ltta2.sum()
lttata2=ltta2.iloc[1]/ltta2.iloc[0]
lttata2=pd.Series([lttata2],index=['6월'])

ssta2=pd.read_csv('./ssteam2006.csv')
ssta2=ssta2.sum()
sstata2=ssta2.iloc[1]/ssta2.iloc[0]
sstata2=pd.Series([sstata2],index=['6월'])

lgta2=pd.read_csv('./lgteam2006.csv')
lgta2=lgta2.sum()
lgtata2=lgta2.iloc[1]/lgta2.iloc[0]
lgtata2=pd.Series([lgtata2],index=['6월'])

htta2=pd.read_csv('./htteam2006.csv')
htta2=htta2.sum()
httata2=htta2.iloc[1]/htta2.iloc[0]
httata2=pd.Series([httata2],index=['6월'])

wota2=pd.read_csv('./woteam2006.csv')
wota2=wota2.sum()
wotata2=wota2.iloc[1]/wota2.iloc[0]
wotata2=pd.Series([wotata2],index=['6월'])

obta2=pd.read_csv('./obteam2006.csv')
obta2=obta2.sum()
obtata2=obta2.iloc[1]/obta2.iloc[0]
obtata2=pd.Series([obtata2],index=['6월'])

ncta2=pd.read_csv('./ncteam2006.csv')
ncta2=ncta2.sum()
nctata2=ncta2.iloc[1]/ncta2.iloc[0]
nctata2=pd.Series([nctata2],index=['6월'])
data2006=pd.concat([hhtata2,sktata2,kttata2,lttata2,sstata2,lgtata2,httata2,wotata2,obtata2,nctata2],axis=1)
print(data2006)

hhta3=pd.read_csv('./hhteam2007.csv')
hhta3=hhta3.sum()
hhtata3=hhta3.iloc[1]/hhta3.iloc[0]
hhtata3=pd.Series([hhtata3],index=['7월'])

skta3=pd.read_csv('./skteam2007.csv')
skta3=skta3.sum()
sktata3=skta3.iloc[1]/skta3.iloc[0]
sktata3=pd.Series([sktata3],index=['7월'])

ktta3=pd.read_csv('./ktteam2007.csv')
ktta3=ktta3.sum()
kttata3=ktta3.iloc[1]/ktta3.iloc[0]
kttata3=pd.Series([kttata3],index=['7월'])

ltta3=pd.read_csv('./ltteam2007.csv')
ltta3=ltta3.sum()
lttata3=ltta3.iloc[1]/ltta3.iloc[0]
lttata3=pd.Series([lttata3],index=['7월'])

ssta3=pd.read_csv('./ssteam2007.csv')
ssta3=ssta3.sum()
sstata3=ssta3.iloc[1]/ssta3.iloc[0]
sstata3=pd.Series([sstata3],index=['7월'])

lgta3=pd.read_csv('./lgteam2007.csv')
lgta3=lgta3.sum()
lgtata3=lgta3.iloc[1]/lgta3.iloc[0]
lgtata3=pd.Series([lgtata3],index=['7월'])

htta3=pd.read_csv('./htteam2007.csv')
htta3=htta3.sum()
httata3=htta3.iloc[1]/htta3.iloc[0]
httata3=pd.Series([httata3],index=['7월'])

wota3=pd.read_csv('./woteam2007.csv')
wota3=wota3.sum()
wotata3=wota3.iloc[1]/wota3.iloc[0]
wotata3=pd.Series([wotata3],index=['7월'])

obta3=pd.read_csv('./obteam2007.csv')
obta3=obta3.sum()
obtata3=obta3.iloc[1]/obta3.iloc[0]
obtata3=pd.Series([obtata3],index=['7월'])

ncta3=pd.read_csv('./ncteam2007.csv')
ncta3=ncta3.sum()
nctata3=ncta3.iloc[1]/ncta3.iloc[0]
nctata3=pd.Series([nctata3],index=['7월'])
data2007=pd.concat([hhtata3,sktata3,kttata3,lttata3,sstata3,lgtata3,httata3,wotata3,obtata3,nctata3],axis=1)
print(data2007)


dataset20=pd.concat([data2005,data2006,data2007],axis=0)
dataset20=dataset20.rename(columns={0:'한화',1:'SK',2:'KT',3:'롯데',4:'삼성',5:'엘지',6:'기아',7:'키움',8:'두산',9:'넥센'})
print(dataset20)
dataset20.to_csv('./dataframe20.csv',index_label='경기날짜')

