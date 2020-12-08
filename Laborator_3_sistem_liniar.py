#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


U =np.array([[2.,-1.,-2.], [0.,4.,4.], [0.,0.,1.]])
c=np.array([[-1.],[8.],[1.]])
x=np.array([[float('nan')],[float('nan')],[float('nan')]])


# In[3]:


det_U = np.linalg.det(U)


# In[4]:


if np.abs(det_U) < 1e-14:     # daca matricea nu este inversabila
    print("Sistemul nu are soluție")
    exit(1)


# In[5]:


U


# In[6]:


# Merg de la ultima linie către prima,
# și rezolv pe rând ecuațiile prin substituție
n = 3
for i in range(n-1, -1, -1):
    coef = U[i, i+1:]
    val = x[i+1:]
    x[i] = (c[i] - coef @ val) / U[i, i]
    print("Pasul", n - i, ":",
          c[i], "-", coef, "@", val, ")",
          "/", U[i, i])

print(x)


# In[7]:


d = U[1,1:]
d


# In[ ]:





# In[ ]:




