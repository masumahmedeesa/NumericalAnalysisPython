# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 04:59:15 2018

@author: AHMED EeSha
"""

import math
import matplotlib.pyplot as plt
import random

#def function(x):
#    return math.sin(3*x)-math.cos(2*x)

def function(x):
    return 3*x-math.cos(x)-1

#def function(x):
#    return math.exp(-x)-x

error=[]

x_i=random.random()
x_iminusOne=random.random()
print x_i,x_iminusOne

x_iplusOne=x_i-(((x_i-x_iminusOne)*function(x_i))/(function(x_i)-function(x_iminusOne)))

x_iminusOne=x_i
x_i=x_iplusOne

i=1
while(i<6):
    i+=1
    temp=x_iplusOne
    x_iplusOne=x_i-(((x_i-x_iminusOne)*function(x_i)*1.0)/(function(x_i)-function(x_iminusOne)))
    error.append((abs(x_iplusOne-temp)/x_iplusOne)*100.0)
    if function(x_iplusOne)==0:
        break    
    x_iminusOne=x_i
    x_i=x_iplusOne
    

print (i,x_iplusOne)

#print error


plt.plot(range(1,i),error,label='Secant',marker='*')
plt.grid()
plt.legend()
plt.show()