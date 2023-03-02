#!/usr/bin/env python
# coding: utf-8

# - Operators are Symbols
# - Types of Operators in Python
#     - Arithmetic Operators
#         - Addition +
#         - Substraction -
#         - Multiplication *
#         - Division /
#         - Modulus %
#         - Exponenetial **
#         - Floor Division //
#     - Assignment Operators
#         - Assignment =
#         - +=
#         - -=
#         - *=
#         - /=
#         - %=
#         - //=
#         - **=
#     - Relational Operators
#          - Equal ==
#          - Not Equal !=
#          - Greater Than >
#          - Less Than <
#          - Greater Than or Equal To >=
#          - Less Than or Equal To <=
#          
#      - Logical Operators
#          - OR
#          - AND
#          - NOT

# # Arithmetic Operators

# In[7]:


a = 6
b = 2

print(a+b)


# In[8]:


print(a*b)


# In[9]:


print(a/b)


# In[10]:


print(a-b)


# In[11]:


print(a**b)


# In[12]:


print(a%b) # habis dibagi


# In[13]:


print(a//b)


# # Assignment Operators

# In[37]:


a = 2
b = 5


# In[21]:


a+=b # is like i said a = a+b
print(a)


# In[23]:


a-=b # is like i said a = a-b
print(a)


# In[28]:


a*=b # is like i said a = a*b
print(a)


# In[34]:


a%=b # is like i said a = a%b
print(a)


# In[38]:


a//=b # is like i said a = a//b
print(a)


# # Relational Operators

# In[39]:


a = 5
b = 4
c = 3
d = 3
e = 9


# In[40]:


print(a==b)


# In[41]:


print(a!=b)


# In[42]:


print(c>b)


# In[43]:


print(a>b)


# In[44]:


print(e>=b)


# In[45]:


print(b<=d)


# # Logical Operators

# In[47]:


## AND
"""

True + True = True
False + True = False
True + False = False
False + False = False

## OR
False + False = False
True + False = True
False + True = True
True + True = True
"""


# In[49]:


a = 5
b = 4

print(not a>b) # this provide true but with not will return false


# In[ ]:




