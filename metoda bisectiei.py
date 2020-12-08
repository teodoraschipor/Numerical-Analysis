#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[2]:


def bisection_search(f, a, b, epsilon = 1e-5):
    
    # calculate the values in the ends of the range
    f_a = f(a)
    f_b = f(b)
    
    # must have different signs
    assert f_a * f_b < 0
    
    # prima estimare, mijlocul intervalului initial
    x_num = (a + b) / 2
    
    # required number of iterations
    N = math.floor(1 + math.log((b - a) / epsilon))
    
    # algorithm
    for i in range(N):
        value = f(x_num)
        if value == 0:
            break
        elif f_a * value < 0:
            b= x_num
        else:
            a =x_num
        x_num = (a + b) / 2
        
    return x_num


# In[3]:


# function for which we are looking for solutions
f = lambda x: (x ** 3) - 7 * (x ** 2) + 14 * x - 6

# search in the given ranges
a = bisection_search(f,0,1)
b = bisection_search(f,1,3.2)
c = bisection_search(f,3.2,4)

print(a)
print(b)
print(c)


# In[4]:


# display the result
# create a plot
fig, ax = plt.subplots(1, dpi=200)


# title
plt.title('BISECTION SEARCH')

# configure the axis
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# generate points
x = np.linspace(start=0, stop=5, num=1000)

# draw the graph
plt.plot(x, f(x), '-.')

# draw the solutions
plt.scatter([a, b, c], [0, 0, 0], c='red')

# display the legend
plt.legend(['f(x)', 'x_num'])


# tag the axis
plt.xlabel('x')
plt.ylabel('y')

plt.show()


# In[ ]:





# In[ ]:




