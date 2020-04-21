# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:06:02 2018

@author: CSELAB303-16
"""

from math import factorial, cos
import numpy as np
import matplotlib.pyplot as plt

def our_cos(x,n):
    return sum([(x**(2*i))/factorial(2*i) if i%2==0 \
       else -(x**(2*i))/factorial(2*i) for i in range(n)])
#    for i in range(n):
#        if i%2==0:
#            s.append((x**(2*i))/factorial(2*i))
#        else:
#            s.append(-(x**(2*i))/factorial(2*i))
#            
#    return sum(s)

x=np.linspace(0,2*np.pi,25)
y1=our_cos(x,7)
y2=our_cos(x,8)
y3=our_cos(x,9)
y_real=np.cos(x)

plt.plot(x,y1, label='approximation, 7', color='r', linestyle=':', marker='*')
plt.plot(x,y2, label='approximation, 8')
plt.plot(x,y3, label='approximation, 9')
plt.plot(x,y_real, label='actual')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.legend()
plt.show()
