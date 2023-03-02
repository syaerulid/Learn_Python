#!/usr/bin/env python
# coding: utf-8

# # Variable

# - Variables is to store data
# - Variables is nothing but a name given to a reserved memeory location where the data is stored
# - We Don't need to specify the data type for any variable

# ## Example

# In[1]:


a = 9 # this means value 9 is stored in a variable name a
a # when we call this, they will print a 9


# In[2]:


print(a) # or we can do something like this instead


# In[3]:


b = 2
c = 'Syaerul Rochman'
d = 'Python Programming'
e = True


# In[4]:


print(b)
print(c)
print(d)
print(e)


# In[5]:


a,b,c = 1,2,3
print(a,b,c)


# In[6]:


a=b=c = 9
print(a,b,c)


# In[7]:


my_first_name = 'Syaerul'
my_last_name = 'Rochman'


# In[8]:


my_first_name
my_last_name # python will only display the latest variable 


# In[9]:


#if we want to display two of them use print instead
print(my_first_name)
print(my_last_name)


# In[10]:


#if we want to display two of them use print instead
print(my_first_name, end = " ")
print(my_last_name)


# ## Variable will store the latest values

# In[11]:


# Example :
a = 7
a = 14
print(a) # the newest value is 14 so 14 being printed instead of 7


# In[12]:


a = 7
print("The value stored in a is :", a)


# In[ ]:




