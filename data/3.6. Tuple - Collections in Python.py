#!/usr/bin/env python
# coding: utf-8

# # Tuple

# - One of the four Colleciton data types in Python
#     - Create Tuple using()
#     - Print Tuple
#         - a = (5,1,3,4,8)
#         - print(a))
#         - print(type(a)
#     - Access Value in Type
#         - Forward Index
#         - Backward Index
# - Tuples are Immutable 
#      - Cannot be modified / updated
#      - We cannot update values like List
#      - a[0] = 9 will not possible and get error
#      - we cannot use append(), insert(), remove() and pop() commands
#      - sort() and reverse() are not possible

# ## Example Immutable

# In[2]:


a = (9,1,5,7)
print(a)


# In[4]:


a[2] = 6 # this is the example


# In[5]:


a = (9,1,5,7)

print(a[0])
print(a[1])
print(a[2])
print(a[3])


# ## Forward and Backwards index

# In[6]:


a = (9,1,5,7)

print(a[2]) #Forward Index
print(a[-3]) #Backward Index


# ## Using For Loop with Tuple:
# - for num in a:
#     - print(num)
# - for i in range(5):
#     - print(a[i])
# - length = len(a)
# - for i in range(length):
#     - print(a[i])

# In[9]:


a = (9,1,5,7)


# In[11]:


for num in a:
    print(num)


# In[13]:


for i in range(4):
    print(a[i])


# In[15]:


length = len(a)
length


# In[16]:


for i in range(length):
    print(a[i])


# ## Slicing Tuple (Same with Lists)

# In[17]:


a = (9,1,5,7)


# In[18]:


print(a[1:3]) # index : position


# In[20]:


print(a[:1])


# ## In and Not In with Tuple()

# In[22]:


a = (9,1,5,7)


# In[23]:


print(5 in a)


# In[24]:


print(10 in a)


# In[25]:


print(11 not in a)


# ## Count in Tuple

# In[26]:


a = (9,1,5,7,6,9,1,2,3,1,9)


# In[27]:


print(a.count(1))


# In[28]:


print(sum(a))


# In[29]:


print(max(a))


# In[30]:


print(min(a))


# In[32]:


print(a.index(6))


# In[33]:


type(a)


# ## Nested Tuple

# In[34]:


a = (9, (6,7,2,3), 4,5,6)


# In[36]:


print(a[1])


# In[39]:


print(a[1][0])


# ## Typecast

# In[40]:


a = tuple("Erul")


# In[41]:


for e in a:
    print(e)


# In[ ]:




