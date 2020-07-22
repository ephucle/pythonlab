#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pwd()

# In[2]:


#df = pd.read_csv("sample.csv")
df = pd.read_excel('ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200713.xlsx', header=1, sheet_name='2.BS_DG_DU_Crash(2020-04-01이후)')


# In[3]:


df.head()


# In[4]:


#print(df)


# In[5]:


df.shape


# In[9]:


df.info()


# In[8]:


df.describe()


# In[10]:


import numpy as np


# In[11]:


a = np.array([1,2,3,4])
print(a)


# In[12]:


type(a)


# In[13]:


a[0]


# In[14]:


a[1]


# In[16]:


b= np.array([0.1,0.2, 3,1])


# In[17]:


print(b)


# In[23]:


A = np.array([['a','b','c'], ['d','e','f'],['g','h','i']])
A


# In[34]:


B= A[1,1]
B


# In[35]:


A.shape


# In[36]:


B=A[:,1:3]
B


# In[37]:


x = np.array([1,2,3,4])
x.mean()


# In[45]:


x.std()


# In[47]:


x.var()


# In[48]:


x.sum()


# In[49]:


x.min()


# In[50]:


x.max()


# In[61]:


C = np.array([[1, 2, 3],
       [2, 4, 6],
       [0, 1, 5]])


# In[62]:


#plus per column
C.sum(axis = 0)


# In[63]:


#plus per row
C.sum(axis = 1)


# In[66]:


x


# In[67]:


x+10


# In[68]:


x*x


# In[70]:


x*x*x


# In[71]:


a = np.arange(5)


# In[72]:


a


# In[74]:


a+20


# In[75]:


g7_pop = pd.Series([35.4, 40.5, 10.7, 111.3, 8.1, 100, 20])


# In[76]:


g7_pop


# In[77]:


g7_pop.name = "G7 Population"


# In[80]:


g7_pop


# In[85]:


g7_pop[0], g7_pop[1], g7_pop[3]


# In[88]:


#lay phan tu cuoi cung
g7_pop[len(g7_pop)-1]


# In[89]:


#do dai cua pd series
len(g7_pop)


# In[92]:


l = ['a', 'b', 'c']
l


# In[93]:


g7_pop.index


# In[94]:


g7_pop.index = ['Canada', 'France', 'Germany','Italy','Japan', 'United Kingdom', 'United State']


# In[95]:


g7_pop


# In[100]:


g7_pop['Canada'] , g7_pop['France']


# In[101]:


g7_pop.index


# In[104]:


#create pandas serial from a dict


# In[105]:


d={'a':1, 'b':2 , 'c':3}


# In[106]:


type(d)


# In[107]:


pd1 =pd.Series(d)


# In[108]:


pd1


# In[109]:


type(pd1)


# In[110]:


pd1.index


# In[111]:


pd1['a']


# In[112]:


len(pd1)


# In[115]:


certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)


# In[116]:


certificates_earned


# In[117]:


print(certificates_earned[certificates_earned>5])


# In[118]:


certificates_earned > 5


# In[120]:


g7_pop * 1_000_000


# In[121]:


g7_pop * 1000000


# In[122]:


g7_pop['Canada':'Italy']


# In[123]:


g7_pop['Canada':'United State']


# In[129]:


g7_pop[g7_pop > 10]


# In[130]:


g7_pop > 10


# In[140]:


mean_g7 = g7_pop.mean()
mean_g7


# In[141]:


g7_pop[g7_pop > g7_pop.mean()]


# In[142]:


g7_pop > g7_pop.mean()


# In[145]:


certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})

names = ['Tom', 'Kris', 'Ahmad', 'Beau']

certificates_earned.index = names
longest_streak = pd.Series([13, 11, 9, 7], index=names)
certificates_earned['Longest streak'] = longest_streak
print(certificates_earned)




