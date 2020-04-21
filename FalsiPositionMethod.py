# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 03:24:13 2018

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
x_r=x_upper-((function(x_upper)*(x_lower-x_upper))/(function(x_lower)-function(x_upper)))        
while(i<2000):        
    if(function(x_r))==0:
        break
    elif function(x_r)*function(x_lower)>0:
        x_lower=x_r
    else:
        x_upper=x_r
    temp=x_r
    x_r=x_upper-((function(x_upper)*(x_lower-x_upper))/(function(x_lower)-function(x_upper)))        
    error.append((abs(x_r-temp)/x_r)*100.0)
    i+=1
  

#x=np.arange(0,math.pi,.001)
#y1=np.sin(3*x)
#y2=np.cos(2*x)

print (i,x_r)

plt.plot(range(i),error,label='falsePosition',marker='*')
plt.grid()
plt.legend()
plt.show()

