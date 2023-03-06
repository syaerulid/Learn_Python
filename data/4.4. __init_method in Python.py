#!/usr/bin/env python
# coding: utf-8

# - We can initialize the Class variables during the object creation statement itself
# - Hence initialization process is simplified with *__init*__method
# - Using *__init*__method inside the Car class to initialize the class variables

# In[2]:


class Car:
    
    def __init__(self,brand,model,price,milage):
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
        
svid = Car("Toyota","Agya",20000,10)

hamz = Car("Toyota","Agya",20000,10)

svid.start_car()
svid.stop_car()
svid.print_car_details()


# In[5]:


hamz.start_car()
hamz.stop_car()
hamz.print_car_details()


# In[ ]:




