#!/usr/bin/env python
# coding: utf-8

# ## Задача 1

# In[1]:


import math

p = 0.01
n = 600
not_greater_than = 10


# In[2]:


def get_number_of_combinations(k, n):
    num = math.factorial(n)
    denum = math.factorial(k) * math.factorial(n - k)
    return num / denum


# In[3]:


def binomial_distribution(x, n, p):
    sum = 0
    for i in range(0, x + 1):
        comb = get_number_of_combinations(i, n)
        sum += comb * math.pow(p, i) * math.pow(1 - p, n - i)
    return sum


# In[4]:


result = binomial_distribution(not_greater_than, n, p)
print("Вероятность дефектного: ", result)


# ## Задача 2

# In[7]:


x = 50
before = 10
p = 0.1


# In[8]:


def negative_binomial_distribution(x, m, p):
    sum = 0
    for i in range(1, x + 1):
        comb = get_number_of_combinations(i, m + i - 1)
        sum += comb * math.pow(p, m) * math.pow(1 - p, i)
    return sum


# In[9]:


before_result = get_number_of_combinations(before, x + before - 1) * math.pow(p, before) * math.pow((1 - p), x)
print("50 изделий до появления 10-го деффектного: ", before_result)
before_second = negative_binomial_distribution(5, 2, p)
print("До второго деффектного не более 5 годных: ", before_second)


# ## Задача 3

# In[10]:


p = 0.95
n = 10
q = 1 - p
m = 5


# In[11]:


def geometric_distribution(x, p):
    return 1 - math.pow(1 - p, x)


# In[15]:


result_1 = q * math.pow(p, n - 1)
result_2 = geometric_distribution(m, q)

print("Для получения 1 отказа испытать 10 приборов: ", result_1)
print("Для первого отказа испытать не более 5: ", result_2)

