#!/usr/bin/env python
# coding: utf-8

# Precedence :
#    - () have the highest priority in Python
#    - Folloed by **(Exponential Operator)
#    - Followed by * / % // (have same precedence)
#    - Followed byu +- (have the same precedence)
#    - Same precedence Operators are evaluated from left to right

# In[3]:


# Example
print((3+4)*5) # if normal operator then result is 23 but because of () priority the result is different


# In[4]:


print(3*4**2) # exponential first, 16 x 3


# In[6]:


print((3*4)**2) # () then exponential so, 12 ** 2


# In[10]:


print(4*3/2%4//3) # left to right


# In[11]:


print(8-3+7) # left to right


# In[12]:


print(8+7-3) # same result


# In[ ]:




