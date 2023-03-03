#!/usr/bin/env python
# coding: utf-8

# - Function can intake data
# - Example: Function intaking the name

# In[1]:


def print_name(name): #name is a parameter
    print("Your name is: "+name)


# In[5]:


print_name("Syaerul Rochman") #function calling argument


# In[3]:


print_name("Cholifah Turizah")


# # Default Argument in Python

# In[8]:


print_name() # error, we need argument inside ()


# In[9]:


def print_name(name="Erul"): # = Erul is default argument
    print("Your name is: "+name)


# In[10]:


print_name() # even we don't have any argument in here, they will not error


# In[12]:


print_name("Yoga")


# In[ ]:




