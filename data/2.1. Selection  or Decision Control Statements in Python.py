#!/usr/bin/env python
# coding: utf-8

# ## Selection / Decision Control Statements

# - If
# - If .. Else
# - Elif

# # If

# In[1]:


a = 5
b = 4


# In[2]:


if a > b:
    print("a is greater than b")


# In[3]:


a,b,c,d,e = 5,4,3,2,1


# In[5]:


"""in this program below, they will check by conditions, one by one, and if conditions = true, the loops is end."""

if a < b:
    print("a is less than b")
elif b < c:
    print("b is less than c")
elif c < d :
    print("c is less than d")
elif d < e:
    print("d is less than e")
else:
    print("e is the least")


# In[ ]:


#Update 2023/3/6
if n % 2 == 0:
    # 2 to 5 range
    if n in range(2,6): # index : position
        print("Not Weird")
    # 6 to 20 range
    elif n in range(6,21): # index : position
        print("Weird")
    # greater than 20
    elif n > 20:
        print("Not Weird")
    # odd
else:
    print("Weird")


