#!/usr/bin/env python
# coding: utf-8

# # Set

# - Un-Order
# - Un-Indexed
# - Un-Duplicated
# - Mutable
# - Random Order

# In[1]:


a = {9,1,5,7}


# In[2]:


print(a)


# In[3]:


print(a[2]) # error


# In[4]:


print(len(a))


# ## Adding Values to the Set

# In[5]:


a = {9,1,5,7}


# In[6]:


print(a)


# In[7]:


# using add
a.add(8)
a.add(12)


# In[8]:


print(a)


# In[9]:


a = {9,1,5,7}


# In[10]:


# using update
a.update([8,12])


# In[11]:


print(a)


# ## Remove Values from the set

# In[12]:


a = {9,1,5,7,6}


# In[13]:


# using remove
a.remove(7)


# In[14]:


print(a)


# In[15]:


# using discard
a = {9,1,5,7,6}


# In[16]:


a.discard(9)


# In[17]:


print(a)


# In[18]:


## using pop for remove random
a = {9,1,5,7,6}


# In[19]:


a.pop()


# In[20]:


print(a)


# In[21]:


# remove all values using clear
a.clear()


# In[22]:


print(a)


# In[24]:


# deleting the set
del a


# In[25]:


a


# ## For Loops with Tuple

# In[26]:


a = {9,1,5,7}


# In[27]:


for e in a:
    print(e)


# In[28]:


# for loop with range() - Not Possible


# ## In and Not in with Set

# In[29]:


a = {9,1,5,7}


# In[30]:


print(15 in a)
print(3 not in a)


# ## Nested Set, Does it Possible?

# - Set only cannot nest List and Set

# In[31]:


a = {9,6,{4,8,1,2},4,1}


# In[35]:


a = {7, (8,5,4,2),3,2} # nested tuple is possible


# In[36]:


a


# ## Converting a List to Set

# In[37]:


a = [8,5,4,2]


# In[39]:


b = set(a)


# In[41]:


print(type(a))
print(type(b))


# ## Intersect with Set

# In[42]:


a = {9,1,5,7}
b = {8,5,6,1}


# In[44]:


print(a.intersection(b))


# ## Union with set

# In[45]:


print(a.union(b))


# ## Difference with Set

# In[46]:


print(a.difference(b)) # a-b


# In[47]:


print(b.difference(a)) # b-a


# ## Symetric Difference with Set

# In[51]:


print(a.symmetric_difference(b))
print(a ^ b)


# In[ ]:




