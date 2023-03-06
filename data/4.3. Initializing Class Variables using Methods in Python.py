#!/usr/bin/env python
# coding: utf-8

# - Create a Class and different Objects
# - using a method inside Car class to initialize the class variable
# 

# In[4]:


class Car:
    
    def initialization_method(self,brand,model,price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage
        
    def start_car(self):
        print(self.brand+" car having model as "+self.model+" has started")
        
    def stop_car(self):
        print(self.brand+" car having model as "+self.model+" has stopped")
        
    def print_car_details(self):
        print("Brand of the car: "+self.brand)
        print("Model of the car is:"+self.model)
        print("Price of the car is: "+str(self.price))
        print("Milage of the car is:"+str(self.milage))
        
svid = Car()
svid.initialization_method("Maruti","Swift VDI",800000,24)

hamz = Car()
hamz.initialization_method("Toyota","Agya",20000,10)

svid.start_car()
svid.stop_car()
svid.print_car_details()


# In[5]:


hamz.start_car()
hamz.stop_car()
hamz.print_car_details()


# In[ ]:




