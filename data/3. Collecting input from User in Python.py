#!/usr/bin/env python
# coding: utf-8

# - Collecting input from User and Type Casting if required
# - input() in-built function
# - Practical Demonstration

# In[1]:


print("Enter your name here:")

name = input() # default is string


# In[2]:


print("Welcome "+name)


# # Multiple Input

# In[ ]:


num1 = input() #"5" in string format
print("Enter second number:")

num2 = input() # "4"
print("Multiplication of two given number is "+(num1*num2)) # not possible to multiple the string format


# In[2]:


num1 = input() #"5" in string format
print("Enter second number:")

num2 = input() # "4"
print("Multiplication of two given number is "+str(int(num1)*int(num2))) # not possible to multiple the string format


# In[ ]:




