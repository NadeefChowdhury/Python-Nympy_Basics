#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import numpy
import numpy as np


# In[27]:


#create an array of integers from 10 to 50
np.arange(10,51)


# In[3]:


#create an array of even integers from 10 to 50
np.arange(10,51,2)


# In[5]:


#create a 3x3 matrix of integers from 0 to 8
np.arange(9).reshape(3,3)


# In[6]:


#create an 8x8 identity matrix
np.eye(8)


# In[7]:


#create an array of  6 random numbers
np.random.rand(6)


# In[9]:


np.ones(25) * np.random.rand()


# In[11]:


#create a 5x5 matrix of  25 random numbers
np.random.randn(25).reshape(5,5)


# In[14]:


#create a 10x10 matrix of numbers from 0.01 to 1.00
np.arange(0.01,1.01,0.01).reshape(10,10)


# In[18]:


#create a 5x5 matrix of numbers from 1 to 25
b = np.arange(1,26).reshape(5,5)


# In[23]:


b


# In[24]:


#find the sum of the numbers in the rows
b.sum(axis=1)


# In[ ]:





# In[ ]:




