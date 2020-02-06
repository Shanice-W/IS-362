#!/usr/bin/env python
# coding: utf-8

# Using the zip() function:
# The zip() function returns an iterator of tuples based on the iterable objects.
# 
# If we do not pass any parameter, zip() returns an empty iterator
# If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
# If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.
# 
# Suppose, two iterables are passed to zip(); one iterable containing three and other containing five elements. Then, the returned iterator will contain three tuples. It's because iterator stops when the shortest iterable is exhausted.

# In[2]:


Listofnumbers = [2,4,6]
Listofstrings = ['apple','banana','pear']

#No iterables were passed
results = zip()

#Converting to interior list
result_list = list(results)
print(result_list)

#Two iterables are passed
results = zip(Listofnumbers, Listofstrings)

# Converting itertor to set
result_set = set(results)
print(result_set)

