#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Car:
    
    def sample(self,brand,model,price,milage):
        print(brand,model,price,milage)
    
    def sample_two(self):
        print(brand,model,price,milage)


# In[5]:


car1 = Car()


# In[6]:


car1.sample() #need arguments


# ## Calling needs argument

# In[8]:


car1.sample("Honda","Amaze","90000","14")


# In[10]:


car1.sample_two() # not accessible because belong to sample_1


# ## Knowing which is variable under the Class

# In[14]:


class Car:
    
    wheels = 4
    
    def sample(self,brand,model,price,milage):
        print(brand,model,price,milage)
    
    def sample_two(self):
        print(self.brand,self.model,self.price,self.milage) 
        # no brand variables, because the only variable is wheels under Car class
        
car1 = Car()
car1.sample("Honda","Amaze","90000","14")
car1.sample_two() 


# In[15]:


class Car:
    
    wheels = 4
    
    def sample(self,brand,model,price,milage):
        print(brand,model,price,milage)
    
    def sample_two(self):
        print(self.wheels) 
        
car1 = Car()
car1.sample("Honda","Amaze","90000","14")
car1.sample_two() 


# ## Creating New Variable Under the Class

# In[24]:


## update
class Car:
    
    wheels = 4
    # variable convert
    def sample(self,brand,model,price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage
        print(brand,model,price,milage)
    
    def sample_two(self):
        print(self.wheels) 
        print(self.brand)
        print(self.milage)
        
        
car1 = Car()
car1.sample("Honda","Amaze","90000","14")
car1.sample_two() 


# In[27]:


## update
class Car:
    
    wheels = 4
    
    def start_car(self):
        print("Car started")
        
    # variable convert
    def sample(self,brand,model,price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage
        print(brand,model,price,milage)
    
    def sample_two(self):
        print(self.wheels) 
        print(self.brand)
        print(self.milage)
        
    def sample_three(self):
        self.start_car()
        
        
car1 = Car()
car1.sample("Honda","Amaze","90000","14")
car1.sample_two() 
car1.sample_three()


# In[ ]:




