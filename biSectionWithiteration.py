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

i=0
x_lower=0
x_upper=1

x_r=(x_lower+x_upper)/2.0
while i<200:        
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
    
print (x_r,i)

#x=np.arange(0,math.pi,.001)
#y1=np.sin(3*x)
#y2=np.cos(2*x)

plt.plot(range(i),error,label='bisectionError')
plt.grid()
plt.legend()
plt.show()



