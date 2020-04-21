# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 04:48:52 2018

@author: AHMED EeSha
"""

import math
import matplotlib.pyplot as plt
import random

#def function(x):
#    return math.sin(3*x)-math.cos(2*x)

def function(x):
    return 3*x-math.cos(x)-1
def ff(x):
    return 3 + math.sin(x)

error=[]
    
i=0

x_i=random.random()
print x_i
x_r=x_i-(function(x_i)/ff(x_i))
while(i<20):        
    x_i=x_r
    if(function(x_r))==0:
        break
    temp=x_r
    x_r=x_i-(function(x_i)/ff(x_i))
    error.append((abs(x_r-temp)/x_r)*100.0)
    i+=1  

print (i,x_r)


plt.plot(range(i),error,label='Newton-Ralph',marker='*')
plt.grid()
plt.legend()
plt.show()

