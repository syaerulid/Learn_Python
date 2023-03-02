#!/usr/bin/env python
# coding: utf-8

# - Using + and str
# - Using ,
# - Using {}
# - Using {index}
# - Using %s,%d,%f, or %g

# In[10]:


name = "Syaerul Rochman"
experience = str(12)
location = "Semarang"


# ## Using +

# In[12]:


print("My name is "+name+". I have around "+experience+" years of Experience and I stay in "+location)


# ## Using {}

# In[13]:


print("My name is {}. I have around {} years of experience and I stay in {}".format(name,experience,location))


# In[14]:


print("My name is {0}. I have around {1} years of experience and I stay in {2}".format(name,experience,location))


# In[15]:


print("My name is {1}. I have around {0} years of experience and I stay in {2}".format(experience,name,location))


# In[21]:


name = "Syaerul Rochman"
experience = 12
location = "Semarang"


# ## Using %

# In[22]:


print("My name is %s. I have around %d years of experience and I stay in %s"%(name,experience,location))


# In[ ]:




