#!/usr/bin/env python
# coding: utf-8

# # Local Variables

# In[1]:


def my_function():
    name = "Syaerul Rochman" # Local Variable / Variable inside the function
    print(name)


# In[2]:


my_function()


# In[3]:


print(name) # not possible because of Local Variable


# # Global Variables

# In[4]:


name = "Syaerul Rochman"


# In[5]:


def my_function():
    print(name)


# In[7]:


my_function()


# In[8]:


print(name)


# # Accesing Local Variable Outside the Function

# In[9]:


def my_function():
    global name # not a local variable anymore
    name = "Syaerul Rochman" 
    print(name)


# In[10]:


my_function()


# In[11]:


print(name)


# # Local and Global have same name

# In[12]:


name = "Syaerul Rochman"


# In[15]:


def my_function():
    name = "Cholifah Turizah" #local Variable
    print(name)


# In[16]:


my_function() # will display Local Variable


# In[17]:


print(name) # will display Global Variable


# In[18]:


name = "Syaerul Rochman"
def my_function():
    global name
    name = "Cholifah Turizah"
    print(name)


# In[19]:


my_function()


# In[21]:


print(name) # global variable got updated, python recognized the latest variable


# In[ ]:




