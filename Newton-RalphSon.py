
#import math
import matplotlib.pyplot as plt
#import random

#def function(x):
#    return math.sin(3*x)-math.cos(2*x)

#def function(x):
#    return 3*x-math.cos(x)-1
#def ff(x):
#    return 3 + math.sin(x)

def function(x):
    return (x*x*x)-0.165*(x*x)+(3.993*pow(10,-4))
def ff(x):
    return 3*(x*x)-0.33*x

error=[]

product=[]  
i=1

x_i = 0.05
x_r = x_i-(function(x_i)/ff(x_i))
error.append((abs(x_r-x_i)/x_r)*100.0)
product.append(x_r)
while i < 3:
    x_i=x_r
    #print (i,x_r)
    if(function(x_r))==0:
        break
    temp=x_r
    x_r=x_i-(function(x_i)/ff(x_i))
    product.append(x_r)
    error.append((abs(x_r-temp)/x_r)*100.0)
    #print (i,error[i])       
    i+=1  
#print (i,x_r)
print ("Final Roots after iteration: "+str(x_r))

print ("Roots: ")
for i in range(3):
    print (i+1, product[i])

print ("Error in percentage: ")

for i in range(3):    
    print (i+1, error[i])

plt.plot(range(i+1),error,label='Newton-Ralph',marker='*')
plt.grid()
plt.legend()
plt.show()

