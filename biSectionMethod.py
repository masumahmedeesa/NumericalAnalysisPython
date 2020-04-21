# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 03:01:00 2018

@author: AHMED EeSha
"""

import math
#import numpy as np
import matplotlib.pyplot as plt

#def function(x):
#    return math.sin(3*x)-math.cos(2*x)

def function(x):
    return 3*x-math.cos(x)-1

error=[]
x_lower=0
x_upper=1
tolerance=0.000000001
i=0
x_r=(x_lower+x_upper)/2.0
while(x_upper-x_lower)/2.0 > tolerance:        
    if(function(x_r))==0:
        break        
    elif function(x_r)*function(x_lower)>0:
        x_lower=x_r
    else:
        x_upper=x_r
    temp=x_r
    x_r=(x_lower+x_upper)/2.0
    error.append((abs(x_r-temp)/x_r)*100.0)
    i+=1
    #return x_r,i

print (i,x_r)

plt.plot(range(i),error,label='bisectionError')
plt.grid()
plt.legend()
plt.show()



