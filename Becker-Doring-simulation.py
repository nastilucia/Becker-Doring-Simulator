#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import random
get_ipython().magic(u'matplotlib inline')


# # UTILITY

# The following utility returns the function dP_dt given two vectors of coefficients $a$ and $b$ of equal size

# In[2]:


def get_dP_dt(a, b):
    assert isinstance(a, np.ndarray)
    assert isinstance(b, np.ndarray)
    assert len(a.shape) == len(b.shape) == 1
    assert a.shape[0] > 0
    assert a.shape[0] == b.shape[0]

    dim = a.shape[0]
    def dP_dt(P, t):
        J = a * P[0] * P
        J[:-1] -= b[1:] * P[1:]
        J[-1] = 0

        c = np.empty(dim)
        c[0] = -J[0] - J.sum()
        c[1:] = J[:-1] - J[1:]
        return c
    
    return dP_dt


# In[3]:


n = 5


# The parameters $a$ and $b$ are the vectors containing all coefficients $a_i$ and $b_i$. They must contain $n$ elements.
# In this moment all coefficients are $1$.

# In[4]:


#k_1 = random.randint(1,1001)
#k_2 = random.randint(1,1001)
k_1=1
k_2=1
dP_dt = get_dP_dt(
    #a=np.ones(n),
    #b=np.ones(n)
    a= np.full(n, k_1),
    b= np.full(n, k_2),
)


# Time and Starting point coordinates

# In[5]:


time= 1000
n_i=time-1
ts = np.linspace(0, 500, time)
#P0 = np.array([2.0, 0.0])

P0 = np.zeros(n)   # inizialize an array with n elements
P0[0] = n


# In[6]:


assert P0.shape == (n,)


# Resolution

# In[7]:


Ps = odeint(dP_dt, P0, ts)


# In[8]:


c1 = Ps[:,0]
print c1[n_i]


# # PLOT

# In[9]:


plt.figure(figsize=(15,5))
for col in xrange(n):
    plt.plot(ts, Ps[:,col], label="c{}".format(col+1))
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.show()

