#!/usr/bin/env python
# coding: utf-8

# # Object
# - A Real world entity
# - We can represent real world Entities as Object in Python
# - Classes in Python, can be used for Creating these Objects
# - Creating Variables and Functons inside the class
# - Functions inside the class in Python can be called as methods
# - self keyword will be explained later
# 

# # Class
# - Template / Blueprint / Factory to create Object

# In[1]:


def sample_fun():
    print("This is a sample function")
    # normal function


# In[8]:


class Car:
    
    wheels = 4
    # the below is a method in python (function inside the class)
    def start_car(self):
        print("Car started")
        
# below is object creation statement
Car()

# object reference / not a variable
erul = Car() # first object reference
omeng = Car() # second object reference


# In[3]:


print(wheels) # error


# In[10]:


print(erul.wheels)


# In[5]:


start_car() # error because start_car is one of the property of class Car


# In[9]:


omeng.start_car() # this one is displayed, so calling class need use object reference


# In[ ]:




