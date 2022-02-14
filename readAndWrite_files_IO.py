#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://github.com/surPoudel/basicPythonforBeginners/blob/main/class_logo_chapter1.png?raw=true" width="1000" alt="cognitiveclass.ai logo"  />
# </center>

# # Read a csv file in python
# * Estimated time needed: **5** minutes

# ## Objectives

# ## After completing this lab you will be able to:
# *   Read a csv file in python
# *   Write a txt file in python

# ## Test input file

# *   drug200.csv

# In[2]:


filename = "drug200.csv"


# ### Here I introduce open function in python
# *   The open() function opens a file, and returns it as a file object.

# ### Multiple ways to open a file
# *   using with statement - automatically closes the file, simplifies exception handling\n
# *   without using with statement - we need to close the file 

# ## mode defines how we wanted to treat the file
# * "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# 
# * "a" - Append - Opens a file for appending, creates the file if it does not exist
# 
# * "w" - Write - Opens a file for writing, creates the file if it does not exist
# 
# * "x" - Create - Creates the specified file, returns an error if the file exist

# ## Strategy 1

# In[4]:


#code using with statement
with open (filename,"r") as f:
    for line in f:
        print(line.strip())#here i introduce strip function that is useful to remove whitespace see the following link https://www.w3schools.com/python/ref_string_strip.asp


# ## Strategy 2

# In[5]:


file = open(filename)
data = file.read()
print (data)
file.close()


# ## Strategy 3

# In[6]:


#without the with statement but reading the file as an object f
f = open(filename, "r")
print(f.read())


# ## Write a .txt file

# In[7]:



with open("result.txt", "w") as g:
    g.write("This is an example of writing the file. Please see the output named result.txt in the folder")


# In[ ]:




