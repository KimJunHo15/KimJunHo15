#!/usr/bin/env python
# coding: utf-8

# ### NumPy
# 
# ### Pandas
# - 행과 열로 구성된 표 형식의 데이터지원
# 
# ### Matplotlib

# ##### NumPy
# 
# - 빠르고 효율적인 벡터 산술연산
# 
# - 반복문 없이 배열 연산 가능

# In[1]:


import numpy as np


# np.ndarray = n차원 배열 클래스
# 
# - 동일한 자료형을 가지는 값들이 배열 형태로 존재함
# 
# - list와 array list는 다르다

# In[3]:


l1 = [1,2,3,4,5]


# In[5]:


arr=np.array(l1)


# In[7]:


print(arr)


# In[8]:


arr2= np.array([[1,2,3],[4,5,6]])


# In[9]:


print(arr2)


# In[10]:


np.array([[[1,2,3],[4,5,6]]])


# In[11]:


arr2


# ### shape : 크기 확인

# In[12]:


arr2.shape


# 2행 3열

# ### size : 개수 확인

# In[13]:


arr2.size


# 현재가지고 있는 데이터 수 = shape의 행 * 열 의 값

# ### dtype : 타입 확인

# In[14]:


arr2.dtype


# 여기서 32 는 2의 32승

# In[20]:


2**32


# int32 =  -2147483648 <= x <= 2147483647 에 해당하는 숫자만 있다.

# ### ndim : 차원 확인

# In[21]:


arr2.ndim


# In[58]:


l1 =[1,2,3,4,5]


# In[59]:


num = int(l1[0]+1)
for i in range(0,len(l1)) :
    l1[i] = num
    num+=1


# In[61]:


for i in range(0,len(l1)) :
    l1[i] = l1[i]+1


# In[60]:


l1


# In[62]:


arr


# In[63]:


arr+1


# ### np.zeros, np.ones

# In[64]:


arr_zeros = np.zeros((3,4))
arr_zeros


# In[65]:


arr_zeros.shape


# In[79]:


arr_ones = np.ones((3,4))
arr_ones = arr_type.astype("int64")
arr_ones


# ### 내가 지정한 값으로 생성하기

# In[73]:


arr_full = np.full((5,5),7)
arr_full


# ### 배열생성하기 (크기 지정)

# In[75]:


arr = np.arange(1,51)
arr


# In[76]:


arr = np.arange(1,51,10)
arr


# ### type지정 배열 생성

# In[77]:


arr_type = np.array([1.2,2.3,3.4],dtype=np.int64)
arr_type


# In[78]:


arr_type = arr_type.astype("float64")
arr_type


# In[80]:


arr_type.dtype


# In[87]:


arr = np.random.rand(2,3)
arr


# In[88]:


arr = np.random.randint(2,10)
arr


# In[91]:


arr = np.random.randint(2,10, size=(2,3))
arr


# 175.2,180.3,175,169.2,185.2,188.0,177.6,178.2,177,179.0
# 65.6,88.0,79.2,69.3,55.0,71.2,73.0,68.9,74.0,82.0

# ### array 연산

# In[92]:


ar = np.array([1,2,3])


# In[94]:


ar+ar


# In[95]:


ar*ar


# ### txt 파일 불러오기

# In[189]:


data = np.loadtxt("./data/height_weight.txt",delimiter=",")


# In[190]:


data


# BMI = 몸무게 / 키 * 키

# In[191]:


h =data[0]/100


# In[192]:


data[1]


# In[193]:


data[1] / (h*h)


# In[194]:


arr = np.array([[1,2,3],[4,5,6,]])


# In[202]:


arr[1,2]


# In[204]:


arr1= np.arange(10)
arr1


# In[205]:


arr1[3:8]


# In[206]:


arr1[3:8] =12


# In[207]:


arr1


# In[208]:


arr2 = np.arange(50).reshape(5,10)
arr2


# -1을 적으면 안적은쪽을 기준으로 자동적으로 맞춰짐

# In[221]:


arr2 = np.arange(50).reshape(-1,10)
arr2


# In[212]:


arr3 = np.arange(25).reshape(5,5)
arr3+1


# ### 2차원 형태의 슬라이싱
# 
# - : 기준

# In[222]:


arr2[:2,:]


# In[224]:


arr2[:,0]


# #### array 슬라이싱 인덱싱

# In[226]:


l2= [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
l2


# In[228]:


arr3 =np.array(l2)


# In[229]:


arr3


# In[ ]:


arr3


# ## Boolean 색인

# In[232]:


name_score = np.array(np.random.randint(50,100, size=8))
name_score


# In[233]:


name_score >= 80


# In[236]:


name_score [name_score >= 80]


# ### 연산함수

# In[239]:


arr = [1,2,3,4,5]
arr = np.array(arr)
arr


# ### sum()  합계

# In[242]:


arr.sum()
np.sum(arr)


# ### mean() 평균

# In[243]:


arr.mean()
np.mean(arr)


# ### abs : 절대값

# In[246]:


arr2 = np.array([-1,-2,-3,-4,-5])

np.abs(arr2)


# In[412]:


data = np.loadtxt("./data/ratings.dat",delimiter='::',dtype=np.int64)
data


# In[251]:


# user_id, movie_id, rating, time  4개의 column

data.shape


# In[258]:


#전체 평균
np.mean(data[:,2])


# ### 영화아이디 꺼내기

# In[424]:


data[0,1]==1193


# In[426]:


data[data[:,1]==1193]


# In[427]:


data[data[:,1]==1193][:,2]


# In[428]:


np.mean(data[data[:,1]==1193][:,2])


# ### 시간만 꺼내기

# In[442]:


data[:,3]==978300760


# In[448]:


data[data[:,3]==978300760][:,2].mean()


# ### 특정 아이디 평균

# In[450]:


data[:,0].size


# In[454]:


round(data[data[:,0]==1][:,2].mean(),2)


# In[ ]:





# In[ ]:





# In[443]:


data[data[:,2]>=4]


# In[ ]:





# ### 각 사용자별 평점 평균 구하기

# In[272]:


i=0
s=0
cnt=0
while(data[i][0]==1) :
    s+=data[i][2]
    i+=1
    cnt+=1
    if data[i][0]==2 :
        break
print(s)
print(cnt)
print(s/cnt)


# In[302]:


np.mean(data[data[:,0]==1][:,2])


# In[ ]:





# In[312]:


arr= []
arr.append([2,np.mean(data[data[:,0]==2][:,2])])
arr


# In[315]:


arr= []
for i in range(1,6041):
    arr.append([i,np.mean(data[data[:,0]==i][:,2])])
arr


# In[316]:


arr= np.array(arr)


# In[319]:


data[:,0].max()


# ### 사용자 중복제거

# In[323]:


np.unique(data[:,0])


# In[326]:


id1 = np.unique(data[:,0])


# In[327]:


id1.shape


# 중복제거한 평점 평균

# In[485]:


r =[]
for i in id1 :
    r.append([i,np.mean(data[data[:,0]==i][:,2])])
r


# In[486]:


arr3 = np.array(r)


# In[487]:


arr3[:,0][arr3[:,1]>=4].astype('int64')


# In[488]:


r


# # file 저장법

# In[489]:


np.savetxt('user_id_mean.csv',r, delimiter=',',fmt ="%.3f")


# In[ ]:





# In[ ]:





# In[ ]:





# In[403]:


np.mean(data[data[:,0]==1][:,2])>=4


# In[463]:


cnt=0
for i in range(1,6041) :
    a=data[data[:,0]==i][:,2].mean()
    if a>=4 :
        cnt+=1
        print(i,a)
cnt


# In[409]:


result =[]
for i in id1 :
    result.append([i,np.mean(data[data[:,0]==i][:,2])>=4])
#     for i in result :
#         if result[i]==True :
result


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[342]:


print('         ,r\'"7')
print("r`-_   ,'  ,/")
print(" \. \". L_r'")
print("   `~\/")
print("      |")
print("      |")


# In[ ]:


num=int(input())
i=0
cnt=0
while True :
    i = (num//10) + (num%10)
    if i==num :
        cnt+=1
        print(cnt)
        break
    elif i!= num:
        i = (i//10)+(i%10)
        cnt+=1


# In[346]:


n1 = int(input())
n2 = int(input())
print(n1+n2)


# In[ ]:


https://www.acmicpc.net/workbook/view/459


# In[362]:


def time (num1,num2,num3,num4) :
    num2+=num4//60
    num3+=num4%60
    if num2>= 60 :
        num1+=num2//60
        num2=num2%60
    if num3>= 60 :
        num2+=num3//60
        num3=num3%60 
    if num1>= 24 :
        num1=num1-24
    print(num1,num2,num3)


# In[366]:


time(23,48,59,2515)


# In[374]:


num1= int(input())
num2= int(input())
num3= int(input())
num4= int(input())
while True :
    num2+=num4//60
    num3+=num4%60
    if num2>= 60 :
        num1+=num2//60
        num2=num2%60
    if num3>= 60 :
        num2+=num3//60
        num3=num3%60 
    if num1>= 24 :
        num1=num1-24
    print(int(num1),int(num2),int(num3))
    break


# In[398]:


l4 = ['@','%','#']
n = float(input())
s= 0
while True :
    sel1= str(input())
    if sel1=='@' :
        n= n*3
    elif sel1=='%':
        n= n+5
    elif sel1=='#':
        n= n-7
    elif sel1!='@' and sel1!='%' and sel1!='#':
        break
print(round(n, 2))


# In[ ]:





# In[ ]:





# In[ ]:




