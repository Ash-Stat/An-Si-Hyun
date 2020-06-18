#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np #분석환경 구축


# In[3]:


customer=pd.read_csv('./customer.csv') #데이터파일 불러오기


# In[4]:


print(customer)#데이터자료의 개괄적인 탐색,  200개의 개체와 5개의 변수가 있다. 


# In[5]:


customer.index


# In[6]:


customer.columns #변수확인


# In[25]:


customer.CustomerID=customer.CustomerID.astype(str) #기초 통계량 확인전에 의미없는 변수는 문자로 바꿔주기.


# In[26]:


print(customer.mean()) #각 변수별 평균확인. 참고로 gender는 범주형이기 때문에 나타나지 않음.


# In[45]:


Age_Rank=customer['Age'].value_counts()[:10] #제일 많이 이용한 나이대 Top 10 보여주기


# In[46]:


for idx, (val,cnt) in enumerate(Age_Rank.iteritems(),1):
    print("Top",idx, ':', val, cnt)


# In[48]:


Annual_Rank=customer['Annual Income (k$)'].value_counts()[:10] #이용 고객의 연봉 Top10 나타내기, k$=1000$라는 뜻


# In[50]:


for idx, (val,cnt) in enumerate(Annual_Rank.iteritems(),1):
    print('Top', idx, ':', val, cnt)


# In[56]:


Spending_Rank=customer['Spending Score (1-100)'].value_counts()[:10]
for idx, (val,cnt) in enumerate(Spending_Rank.iteritems(),1):
    print('Top', idx, ':', val, cnt)
    #Spending Score은 손님들의 소비 습관이나 행태에 따른 점수를 부여한 것이다.
    #가장 많은 빈도를 보여준 점수 Top10을 출력해본다.


# In[57]:


print(customer.info()) #분석에 앞서 데이터 전처리를 위한 탐색과정. 결측값이 없었다.


# In[59]:


customer.describe() #전처리 단계에서 결측값이나 변수 변환작업이 필요없다고 판단하여  수치형 자료들의
                    #기초 통계량을 다시한번 확인해 본다.


# In[69]:


customer.var() #자료의 범주별 분산과 표준편차를 구해본다.


# In[70]:


customer.std()


# In[78]:


customer.cov() #범주간 공분산을 구해본다.


# In[79]:


customer.corr() #범주간 상관관계를 구해본다.


# In[100]:


gen=customer.Gender
gen


# In[169]:


gender=gen.replace('Male',0).replace('Female',1) #Male 과 Female을 0과 1로 나타내는 작업
age=customer.Age
#income=customer.Annual Income (k$)
#score=customer.Spending Score (1-100)


# In[171]:


income=customer['Annual Income (k$)']


# In[172]:


score=customer['Spending Score (1-100)']


# In[174]:


print(gender)
print(age)
print(income)
print(score)


# In[182]:


gender.cov(age) #성별과 나이의 상관관계, 통계적 의미는 없다.


# In[183]:


gender.cov(income) #성별과 수입의 관계, 통계적 의미는 없다.


# In[184]:


gender.cov(score) # 성별과 고객점수의 관계성, 어느정도 영향이 있다.


# In[185]:


gender.corr(score) #하지만 상관관계(변수간의 선형성)는 높지 않아 보인다.


# In[191]:


newdata=pd.DataFrame({'Sex' : gender, 'Age' : age, 'Income' : income, 'Score' : score})
#데이터 전처리를 마친후 다시 하나의 데이터셋으로 합쳐주는 작업


# In[192]:


newdata


# In[221]:


cov=newdata.cov() #새로만든 데이터 셋 간의 공분산과 상관관계를 막대차트로 나타내기 위하여 새로운 이름 설정


# In[220]:


corr=newdata.corr()


# In[195]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[223]:


cov.plot.bar()  #공분산의 바차트


# In[224]:


corr.plot.bar() #상관관계 바차트,변수간의 상관관계는 크게 높지 않고, 성별과 점수간의 영향이 어느정도 있을 뿐


# In[228]:


#PCA분석에 앞서서 필요한 모듈을 불러온후 정규화 작업을 실시한다.
from sklearn.preprocessing import StandardScaler
newdata_std=StandardScaler().fit_transform(newdata)
newdata_std #정규화작업


# In[229]:


Tnewdata=newdata_std.T
cov_mat=np.cov(Tnewdata)
print(cov_mat) #공분산 행렬을 만들어 준다.


# In[232]:


eigval, eigvec=np.linalg.eig(cov_mat)


# In[233]:


print('Eigenvectors \n%s' %eigvec)


# In[236]:


print('Eigenvalues \n%s' %eigval)


# In[237]:


eigval[0]/sum(eigval) #첫번째 고유값의 정보량의 크기가 33%이다.


# In[238]:


eigval[1]/sum(eigval) #두번째 고유값의 정보량의 크기가 26%정도이다.


# In[239]:


eigval[2]/sum(eigval) #세번째 고유값의 정보량의 크기가 23%이다.


# In[240]:


eigval[3]/sum(eigval)#네번째 고유값의 정보량의 크기가 16%이다.


# In[249]:


import sklearn.datasets
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt #요인분석을 위하여 anaconda 프롬프트 에서 pip install factor_analyzer를 해준다.


# In[425]:


datafactor=FactorAnalyzer(n_factors=2, rotation='varimax')#요인을 2개정도로 설정해본다.


# In[448]:


import sklearn
from sklearn.decomposition import FactorAnalysis
from sklearn import datasets
datafactor=FactorAnalysis().fit(newdata_std)
factormat=pd.DataFrame(datafactor.components_,columns = newdata.columns)
Tfactormat=factormat.T
Tfactormat #성별과 나이, 수입과 점수의 요인으로 나누어 볼 수 있을 것 같다.
           #즉, 네개의 변수를 사람의 내적 성질(나이, 성별)과 외적 성질(수입, 고객점수)로 나눌 수 있다.


# In[430]:


load=datafactor.loadings_


# In[431]:


val,vec=datafactor.get_eigenvalues()


# In[432]:


xvals=range(1, newdata.shape[1]+1)


# In[433]:


plt.scatter(xvals, val)
plt.plot(xvals, val)
plt.title('Scree plot')
plt.xlabel('Factor')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()
#고유값을 1이상 갖는것이 두개 있었다. ->요인이 두개


# In[265]:


from sklearn.cluster import KMeans #군집분석을 위한 환경 구축


# In[269]:


cluster= KMeans(n_clusters=2)
y_cluster=cluster.fit_predict(newdata_std)


# In[270]:


y_cluster #2개의 군집화를 했을때 


# In[276]:


cluster=KMeans(n_clusters=3)
y_cluster=cluster.fit_predict(newdata_std)
y_cluster


# In[277]:


cluster=KMeans(n_clusters=4)
y_cluster=cluster.fit_predict(newdata_std)
y_cluster     


# In[300]:


cluster=KMeans(n_clusters=5)
y_cluster=cluster.fit_predict(newdata_std)
y_cluster


# In[301]:


cluster=KMeans(n_clusters=6)
y_cluster=cluster.fit_predict(newdata_std)
y_cluster #자료의 수를 균등하게 나뉠때 까지 군집을 나누어 본다.


# In[312]:


group=y_cluster


# In[320]:


plt.hist(group)
plt.ylabel('counts')
plt.title('Histogram of Cluster')
plt.show() 


# In[359]:


grouping=pd.DataFrame({'Cluster' : group}) #각 군집별 데이터셋을 만들어 본다.


# In[376]:


group_zero=grouping[grouping<1].dropna() #군집 0~5까지 데이터셋을 나누기
group_zero


# In[378]:


group_one=grouping[grouping==1].dropna()
group_one


# In[380]:


group_two=grouping[grouping==2].dropna()
group_three=grouping[grouping==3].dropna()
group_four=grouping[grouping==4].dropna()
group_five=grouping[grouping==5].dropna()


# In[389]:


group_zero.head(10) #이제 각 군집의 10개의 개체를 뽑아본다.


# In[390]:


group_one.head(10)


# In[392]:


group_two.head(10)


# In[393]:


group_three.head(10)


# In[394]:


group_four.head(10)


# In[396]:


group_five.head(10)


# In[401]:


zero=newdata.iloc[[0,1,15,17,21,23,25,27,33,41]] #추출한 10개에 해당하는 고객 정보를 다시 탐색한다.
zero


# In[403]:


one=newdata.iloc[[6,12,22,24,26,28,34,36,38,40]]
one


# In[405]:


two=newdata.iloc[[126,130,134,138,144,146,150,156,158,162]]
two


# In[407]:


three=newdata.iloc[[2,3,4,5,7,9,11,13,16,19]]
three


# In[409]:


four=newdata.iloc[[8,10,14,18,20,30,32,42,53,55]]
four


# In[411]:


five=newdata.iloc[[122,125,133,135,139,143,147,153,155,157]]
five


# In[414]:


zero.describe() #추출한 10개의 군집별 기초통계량 확인


# In[412]:


one.describe()


# In[413]:


two.describe()


# In[415]:


three.describe()


# In[416]:


four.describe()


# In[417]:


five.describe()


# In[ ]:


#군집 0의 경우 남성 20대 초반이며, 평균 2400만원 정도의 연봉(1달러당 1000원 가정) 이며 고객점수가 준수했다.
#군집 1의 경우 여성 40대 후반이며, 평균 3000만원에 가까운 연봉이고, 고객점수가 상당히 낮았다.
#군집 2의 경우 남성 30대 초반이며, 평균 7500만원에 가까운 연봉임에도 불구하고, 고객 점수가 제일 낮았다.
#군집 3의 경우 여성 20대 후반이며, 평균 1800만원에 가까운 연봉이고, 고객점수가 군집간 평균 이상이었다.
#군집 4의 경우 남성 50대 초반이며, 평균  3000만원에 가까운 연봉이고, 고객점수가 낮았다.
#군집 5의 경우 여성 30대 초반이며, 평균 7450만원에 가까운 연봉이고, 고객점수가 제일 높았다.

