#!/usr/bin/env python
# coding: utf-8

# # Self keyword in Python
# - Represents something that belongs to the class
# - Can be used to access the variables and methods inside the same class
# - Inside the Class we have to use slef to access the properties and outside the class we have to use object reference to access the class properties
# - self parameter can be renamed
# - Assigning function parameters to class Variables

# In[1]:


class Car:
    
    wheels = 4
    
    def start_car(self):  # have to self keyword
        print("Car started")
        
    def example_one(self):
        print(self.wheels) # within the class using self
        self.start_car()
        
# Using obejct reference we can access the properties of the Class outside the class        
car1 = Car() # object reference


# In[3]:


print(car1.wheels)


# In[4]:


car1.start_car()


# In[ ]:




