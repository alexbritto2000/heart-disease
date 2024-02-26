#!/usr/bin/env python
# coding: utf-8

# In[1]:


#header file declaraction
import pickle#make a dummy file
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import sklearn
import numpy as np


# In[2]:


#reading the two datasets for heart and diabetes
dh=pd.read_csv("heart.csv")
dd=pd.read_csv("diabetes.csv")


# In[ ]:


print(dh.head())


# In[ ]:


print(dd.head())


# In[7]:


#feature selection for heart
di=dh[["male","age","currentSmoker","cigsPerDay","prevalentStroke","prevalentHyp","diabetes","totChol","sysBP","diaBP","heartRate","glucose"]]
do=dh.iloc[:,-1]
#featuire selection for diabetes
ddi=dd.iloc[:,1:-1]
ddo=dd.iloc[:,-1]


# In[10]:


import matplotlib.pyplot as plt
import pandas as pd
num=pd.value_counts(dh['TenYearCHD'],sort=True).sort_index()
num.plot(kind='bar')
plt.title("HEART DISEASES")
plt.xlabel('HEART DETAILS')
plt.ylabel('number')


# In[11]:


import matplotlib.pyplot as  plt
#num=pd.value_counts
num=pd.value_counts(dd['Outcome'],sort=True).sort_index()
num.plot(kind='bar')
plt.title("DIABETES")
plt.xlabel('DIABETES')
plt.ylabel('number')


# In[12]:


print(dh.info())


# In[13]:


print(dd.info())


# In[14]:


#thus heart module contains null values
from sklearn.preprocessing import LabelEncoder
import warnings 
warnings.filterwarnings('ignore')
#da=di.fillna(1,inplace=True)

da=LabelEncoder()

di["cigsPerDay"]=da.fit_transform(di[["cigsPerDay"]])
di["totChol"]=da.fit_transform(di[["totChol"]])
di["heartRate"]=da.fit_transform(di[["heartRate"]])
di["glucose"]=da.fit_transform(di[["glucose"]])


# In[15]:


print(di.isnull().sum())
print(do.isnull().sum())
print(ddi.isnull().sum())
print(ddo.isnull().sum())


# In[16]:


#for heart dieases training set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(di,do,test_size=0.2)

#for diabetes
x1_train,x1_test,y1_train,y1_test=train_test_split(ddi,ddo,test_size=0.2)


# In[17]:


import warnings 
warnings.filterwarnings('ignore')
#for heart diseases
from sklearn.linear_model import LogisticRegression
lg=LogisticRegression()
lg.fit(x_train,y_train)
lg.predict(x_test)
print(lg.score(x_test,y_test))


#for diabets

from sklearn.linear_model import LogisticRegression
lg1=LogisticRegression()
lg1.fit(x1_train,y1_train)
lg1.predict(x1_test)
print(lg1.score(x1_test,y1_test))



# In[18]:


#for heart diseases
from sklearn.ensemble import AdaBoostClassifier
a=AdaBoostClassifier()
a.fit(x_train,y_train)
a.predict(x_test)
f=a.score(x_test,y_test)
print("heart AB Score:",f)

#for diabets

from sklearn.ensemble import AdaBoostClassifier
a1=AdaBoostClassifier()
a1.fit(x1_train,y1_train)
a1.predict(x1_test)
s=a1.score(x1_test,y1_test)
print("Diabetes AB Score:",s)


# In[19]:


#for heart diseases
from sklearn.ensemble import RandomForestClassifier
lg=RandomForestClassifier()
lg.fit(x_train,y_train)
lg.predict(x_test)
t=lg.score(x_test,y_test)
print("heart RF Score:",t)

#for diabets

from sklearn.ensemble import RandomForestClassifier
lg1=RandomForestClassifier()
lg1.fit(x1_train,y1_train)
lg1.predict(x1_test)
r=lg1.score(x1_test,y1_test)
print("Diabetes  Score:",r)


# In[20]:


import matplotlib.pyplot as plt
plt.title("RANDOM FOREST")
plt.xlabel('ACCURACY VALUES')
plt.ylabel('RATINGS')
plt.hist(r)


# In[21]:


#for heart diseases
from sklearn.svm import SVC
a=SVC()
a.fit(x_train,y_train)
a.predict(x_test)
f=a.score(x_test,y_test)
print("heart SVC Score:",f)

#for diabets
from sklearn.svm import SVC
a1=SVC()
a1.fit(x1_train,y1_train)
a1.predict(x1_test)
s=a1.score(x1_test,y1_test)
print("Diabetes SVC Score:",s)

import matplotlib.pyplot as plt
plt.title("SVM")
plt.xlabel('ACCURACY VALUES')
plt.ylabel('RATINGS')

plt.hist(s)


# In[22]:


with open("heartnew.pickle","wb") as f:
    pickle.dump(lg,f)
with open("diabetesnew.pickle","wb") as g:
    pickle.dump(lg1,g)


# In[23]:


#print(ddi.head())


# In[ ]:


#print(di.head())


# In[ ]:





# In[ ]:




