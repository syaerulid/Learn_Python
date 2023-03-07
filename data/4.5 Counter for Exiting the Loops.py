#!/usr/bin/env python
# coding: utf-8

# In[1]:


## some programs to exits for / while loops
#Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)


# In[3]:


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


# In[4]:


"""Using a counter variable to exit a loop
Look at the snippet below:"""

counter = 10
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


# In[5]:


secret_number = 777
magic = int(input("Guess the magic number :"))
while magic != secret_number:
    print("Ha ha! You're stuck in my loop!", magic)
    magic -= 1
print("Well done, muggle! You are free now.")

(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


# In[6]:


import time

for i in range(1,6):
    print(str(i) + " Mississipi")
    i+=1
    counter = 5
print("Ready or not, here I come")

# use counter to exit the loop


# In[ ]:




