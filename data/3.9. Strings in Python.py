#!/usr/bin/env python
# coding: utf-8

# In[1]:


first_name = "Syaerul"


# In[2]:


last_name = 'Rochman'


# In[3]:


location = str("Indonesia")


# In[4]:


print(first_name)
print(last_name)
print(location)


# In[5]:


type(first_name)


# ## Strings work Like Collections List in Python

# In[6]:


first_name = "Syaerul"


# In[7]:


print(first_name[0])


# ## Loops in Strings

# In[9]:


for i in first_name:
    print(i)


# ## len Strings()

# In[12]:


print(len(first_name))


# In[15]:


for i in range(len(first_name)):
    print(first_name[i])


# ## In and Not In with Strings

# In[16]:


print("rul" in first_name)


# In[17]:


print("za" in first_name)


# ## Slicing with Strings

# In[18]:


print(first_name[1:2]) # Index : Position


# In[19]:


print(first_name[:3])


# # Modifiying Strings

# ## Upper and Lower

# In[21]:


first_name = "Syaerul"


# In[22]:


print(first_name.upper())


# In[23]:


print(first_name.lower())


# ## Strip

# - Remove leading and trailing spaces

# In[24]:


name = "    Syaerul Rochman    "


# In[25]:


print(name.strip())


# ## Replace

# In[26]:


name = "Syaerul Rochman"


# In[27]:


print(name.replace("o","i"))


# ## Split()

# In[29]:


name = "My name is Syaerul Rochman"


# In[32]:


words = name.split(" ")


# In[33]:


for word in words:
    print(word)


# In[34]:


print(words[3])


# ## Strings are Immutable

# In[35]:


name = "Syaerul"


# In[37]:


print(id(name))


# In[38]:


name = "Erul"


# In[39]:


print(id(name))


# ## Capitalize

# In[40]:


name = "my name is cholifah turizah"


# In[41]:


print(name.capitalize()) # capitalize the first letter


# In[42]:


print(name.title()) # capitalize first letter for each every word


# ## Count

# In[44]:


name.count("my")


# ## Find Word

# In[46]:


print(name.find("cho")) ## space is counted


# ## Compare Strings

# In[47]:


name_one = "Syaerul"
name_two = "Syaerul"
name_three = "Cho"


# In[48]:


print(name_one == name_three)


# In[50]:


print(name_one != name_two)


# In[51]:


print(name_one.__eq__(name_two))


# In[52]:


print(name_one.casefold() == name_two)


# In[ ]:




