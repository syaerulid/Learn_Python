#!/usr/bin/env python
# coding: utf-8

# # List
#    - Lists are ordered.
#    - Lists can contain any arbitrary objects.
#    - List elements can be accessed by index.
#    - Lists can be nested to arbitrary depth.
#    - Lists are mutable.
#    - Lists are dynamic.

# In[1]:


a = [9,1,5,7]


# In[2]:


print(a)


# ## Indexing in List Python start from 0

# In[5]:


print(a[0])


# In[7]:


print(a[3])


# In[8]:


print(a[4]) # out of range bcause index is only 0,1,2,3


# ## Finding the Size of The list using len()

# In[10]:


a = [9,1,5,7]


# In[11]:


for i in range(len(a)):
    print(i)


# In[12]:


for i in range(len(a)):
    print(a[i])


# ## For Each Loops

# In[13]:


a = [9,1,5,7,6,0]


# In[14]:


for num in a:
    print(num)


# ## Updated the elements in the list

# In[15]:


a = [9,1,5,7]

print(a)


# In[16]:


a[2] = 6


# In[17]:


print(a)


# ## Appending Element in the list

# In[18]:


a = [9,1,5,7]


# In[19]:


print(a)


# In[20]:


a.append(6)


# In[21]:


print(a)


# ## Inserting the Elements at a particular index using insert(index, "value")

# In[22]:


a = [6,4,1,9]


# In[23]:


print(a)


# In[24]:


a.insert(2,8)


# In[25]:


print(a)


# ## Remove the elements from the list using remove(element)

# In[26]:


a = [9,1,5,6]


# In[27]:


print(a)


# In[28]:


a.remove(1)


# In[29]:


print(a)


# ## Remove Latest Index with pop()

# In[30]:


a = [7,8,1,4]


# In[31]:


print(a)


# In[32]:


a.pop()


# In[33]:


print(a)


# ## Remove Specify Index using pop()

# In[60]:


a = [3,7,9,1]


# In[61]:


print(a)


# In[62]:


a.pop(2)


# In[63]:


print(a)


# ## Remove all elements from the List using clear()

# In[38]:


a = [3,7,9,1]


# In[39]:


print(a)


# In[40]:


a.clear()


# In[41]:


print(a)


# ## Reverse the List

# In[64]:


a = [3,7,9,1]


# In[65]:


print(a)


# In[66]:


a.reverse()


# In[67]:


print(a)


# ## Sorting the list by Ascending

# In[68]:


a = [3,7,9,1]


# In[69]:


print(a)


# In[70]:


a.sort()


# In[71]:


print(a)


# In[72]:


colors = ['orange','green','yellow','blue','white']


# In[73]:


print(colors)


# In[74]:


colors.sort()


# In[75]:


print(colors)


# ## Using Index() with List

# In[79]:


a = [3,7,9,1]


# In[80]:


print(a)


# In[84]:


print(a.index(9))


# ## List insert another List [Nested List]

# In[85]:


a = [9,[6,0,6,8],5,7]


# In[86]:


print(a[1])


# In[89]:


print(a[1][3])


# ## Insert Different Type of Values to List

# In[90]:


a = ['Honda','Amaze',14.5,'Petrol',True,900000]


# In[91]:


print(a[1])


# In[92]:


print(a)


# ## Forward and Backward Index

# In[93]:


a = [3,1,5,8]


# In[94]:


print(a[2])


# In[96]:


print(a[-2]) # -2 + size of the list, -2 + 4 = 2


# In[99]:


print(a[-4]) # -4 + 4 = 0


# ## Slicing The Lists

# In[100]:


a = [3,1,5,8]


# In[102]:


print(a[1:3]) # start from Index want to element position 3
# start is always index
# index : position


# In[103]:


print(a[:3])


# ## Finding the number of times the element repeated in list using count()

# In[105]:


a = [9,1,3,5,7,6,0,6,8,9,9,2]


# In[108]:


# how many time 9 repeated?
print(a.count(9))


# ## Finding maximum and minimum element from the list using max()

# In[109]:


a = [9,1,3,5,7,6,0,6,8,9,9,2]

print(max(a))


# In[110]:


print(min(a))


# ## Finding the sum of elements in the list

# In[111]:


a = [9,1,3,5,7,6,0,6,8,9,9,2]

print(sum(a))


# ## Finding data type using type()

# In[112]:


a = [9,1,3,5,7,6,0,6,8,9,9,2]

print(type(a))


# ## Deleting the list

# In[114]:


a = [9,1,5,7]
print(a)


# In[115]:


del a


# In[116]:


print(a) # error


# ## using In + Not In with List

# In[117]:


a = [9,1,5,7]

print(5 in a)


# In[118]:


print(15 in a)


# ## Concatening Two List Using Operator

# In[119]:


a = [9,1,5,7]
b = [6,0,6,8]

c = a+b


# In[120]:


print(c)


# ## Extend The Lists

# In[124]:


a = [9,1,5,7]
b = [6,0,6,8]

a.extend(b)

print(a)
print(b)


# In[ ]:




