#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://github.com/surPoudel/basicPythonforBeginners/blob/main/Chapter2/logo.png?raw=true" width="1000" alt="cognitiveclass.ai logo"  />
# </center>

# # Chapter 2
# ## Writing functions
# 
# ### A function is a block of code that only runs when it is called. Python functions return a value using a return statement, if one is specified. A function can be called anywhere after the function has been declared

# ## Import numpy package
# * stands for Numerical Python, is a library consisting of multidimensional array objects and a collection of routines for processing those arrays. Using NumPy, mathematical and logical operations on arrays can be performed. 

# In[1]:


import numpy as np


# ### Example of a function that computes average from a list of number

# ### We have a new term called list. So what is list?
# * Lists are used to store multiple items in a single variable.
# * Lists are one of 4 built-in data types in Python used to store collections of data
# * Lists are created using square brackets

# ## Simple list operations

# * https://www.educba.com/list-operations-in-python/
# 
# I find this website pretty useful. This gives common lists operation in python
# 1. append()
# 2. extend()
# 3. insert()
# 4. remove()
# 5. pop()
# 6. slice()
# 7. reverse()
# 8. len()
# 9. min() and max()
# 10. count()
# 11. concatenate
# 12. multiply
# 13. index()
# 14. sort()
# 15. clear()
# 
# 
# I just put 3 list examples here

# ### The append() method is used to add elements at the end of the list. This method can only add a single element at a time. To add multiple elements, the append() method can be used inside a loop.

# In[23]:


#appends
myList = [1, 2, 3]
myList.append(4) #4 is appended to myList

print(myList) #myList now becomes [1,2,3,4]


# ### The extend() method is used to add more than one element at the end of the list. Although it can add more than one element, unlike append(), it adds them at the end of the list like append()

# In[24]:


#list extends
myList.extend([4, 5, 6]) #myList  [1,2,3,4] is extended with another list [4, 5, 6]
print(myList) #myList now becomes [1, 2, 3, 4, 4, 5, 6]


# ### The insert() method can add an element at a given position in the list. Thus, unlike append(), it can add elements at any position, but like append(), it can add only one element at a time. This method takes two arguments. The first argument specifies the position, and the second argument specifies the element to be inserted.

# In[25]:


myList.insert(3, 4)


# In[26]:


print(myList)


# #### Try other list operations from https://www.educba.com/list-operations-in-python/ or any other tuturials

# ## Introduction to functions

# ### Example of functions that returns average of a list .. list are described above

# In[2]:



def average(list):
    return np.mean(list)


# ### Example of a function that multiply two numbers

# In[8]:


def multiply(x,y):
    return x*y


# ### Example of a function that computes division from 2 numvers
# 

# In[9]:


def divide(x,y):
    return x/y


# ### Since we wrote the functions,we can call the function from any part of code

# In[10]:


#example of list
testList = [1,2,3,4]
print ("The average of list is", average(testList)) 


# #### we do not need too rewrite the same function as we can call from any location

# In[12]:


#example of list
testList = [10,20,30]
print ("The average of list is", average(testList)) 



# In[11]:


print ("The multiplication of 2 x 3 = ", multiply(2,3))

