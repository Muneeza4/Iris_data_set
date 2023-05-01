#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
iris_data = pd.read_csv(r"C:\Users\BT\Documents\Iris.csv")


# In[5]:


iris_data["Species"].value_counts()


# In[17]:


a = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
x, y, ve_x, ve_y, vi_x, vi_y = [], [], [], [], [], []

for e,i in enumerate(iris_data["Species"]):
    if(i == a [0]):
        x.append(iris_data["PetalLengthCm"][e])
        y.append(iris_data["PetalWidthCm"] [e])
    elif(i == a[1]):
        ve_x.append(iris_data["PetalLengthCm"][e])
        ve_y.append(iris_data["PetalWidthCm"][e])
    elif(i ==a[2]):
        vi_x.append(iris_data["PetalLengthCm"][e])
        vi_y.append(iris_data["PetalWidthCm"][e])


# In[11]:


plt.plot(x, y, 'b*', label = "Iris-setosa")
plt.plot(ve_x, ve_y, 'g.', label = "Iris-versicolor")
plt.plot(vi_x, vi_y, 'rv', label = "Iris-virginica")
plt.title("Iris Species Data Set")
plt.legend()



# In[ ]:




