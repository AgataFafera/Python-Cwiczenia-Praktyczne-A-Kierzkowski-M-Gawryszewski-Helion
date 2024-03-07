#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fibonacci_rek(n):
  if n == 0: 
    return 0 
  elif n == 1: 
    return 1 
  else: 
    return fibonacci_rek(n-1) + fibonacci_rek(n-2)

print(fibonacci_rek(5))
print(fibonacci_rek(10))
print(fibonacci_rek(30))

