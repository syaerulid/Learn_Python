#!/usr/bin/env python
# coding: utf-8

# # Dictionary

# - Store multiple values in Key Value pairs

# In[4]:


car = {"Brand":"Honda",
       "Model":"Amaze",
       "Price":90000,
       "Milage":32}


# In[5]:


print(car)


# In[6]:


print(type(car))


# ## Get the Values of Key

# In[7]:


print(car.get("Price"))


# In[8]:


print(car['Model'])


# ## Printing All the Keys

# In[9]:


print(car.keys())


# ## Printing All Values

# In[10]:


print(car.values())


# ## Updating Values

# In[11]:


car['Price'] = 100000


# In[12]:


print(car)


# ## Adding new Values

# In[14]:


car['Color'] = 'Black'


# In[15]:


print(car)


# ## For Loops with Dictionary

# In[16]:


for i in car:
    print(i)


# In[17]:


for i in car.keys():
    print(i)


# In[18]:


for i in car.values():
    print(i)


# ## Keys and Values Loops

# In[21]:


for i in car.keys():
    print(i, car.get(i))


# In[23]:


for i in car.keys():
    print(i, car[i])


# In[24]:


for k,v in car.items():
    print(k,v)


# ## Removing Item with Dict

# In[25]:


car = {"Brand":"Honda",
       "Model":"Amaze",
       "Price":90000,
       "Milage":32}


# In[26]:


car.pop("Model")


# In[27]:


print(car)


# In[28]:


del car['Price']


# In[29]:


print(car)


# ## Removing Last Item with Dict

# In[30]:


car = {"Brand":"Honda",
       "Model":"Amaze",
       "Price":90000,
       "Milage":32}


# In[31]:


car.popitem()


# In[32]:


print(car)


# ## Remove All Key, Values from Dict

# In[33]:


car.clear()


# In[34]:


print(car)


# ## Finding the Size of Dictionary

# In[35]:


car = {"Brand":"Honda",
       "Model":"Amaze",
       "Price":90000,
       "Milage":32}


# In[37]:


len(car)


# In[38]:


# delete dictionary
del car


# In[39]:


print(car)


# ## Compare Dictionary

# In[40]:


car1 = {"Brand":"Honda",
       "Model":"Amaze",
       "Price":90000,
       "Milage":32}


# In[41]:


car2 = {"Brand":"Honda",
       "Model":"Amaze",
       "Price":90000,
       "Milage":32}


# In[42]:


print(car1==car2)


# In[43]:


car2 = {"Brand":"Honda",
       "Model":"Amaze",
       "Milage":32}


# In[44]:


print(car1==car2)


# In[ ]:




