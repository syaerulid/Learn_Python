#!/usr/bin/env python
# coding: utf-8

# # Break and Continue Statements in Python

# - Break Statement in Python
# - Continue Statement in Python
# - Return Statement in Python
# - Try and Except Statement in Python

# # For Statement

# In[1]:


for i in range(1,11):
    print(i)


# ## For + Break Statement

# In[2]:


for i in range(1,11):
    if i==5:
        break
    print(i) # loops will stop if i == 5


# ## For + Continue Statement

# In[3]:


for i in range(1,11):
    if i == 5:
        continue
    print(i) # only 5 is not printed, because continue = skipped


# # While Statement

# In[4]:


i = 1


# In[5]:


while i <=10:
    i+=1
    print(i)


# ## While + Break

# In[6]:


i = 1

while i <=10:
    if i==5:
        break
    print(i)
    i+=1


# ## While + Continue

# In[7]:


i = 1

while i <=10:
    if i==5:
        i+=1
        continue
    print(i)
    i+=1


# In[ ]:





# In[ ]:




