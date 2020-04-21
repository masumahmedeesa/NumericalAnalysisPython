# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 02:16:15 2018

@author: Masum AHMED EeSha
"""

import numpy as np
 
def LUDecomposeGaussianEliminationNoPivoting(A, b):
    n =  len(A)
    L=np.zeros(shape=(n,n))
    
    np.fill_diagonal(L,1.)
    #np.diag(x)
    if b.size != n:
        raise ValueError("Not compatible between A & b.", b.size, n)
    for pivot_row in xrange(n-1):
        for row in xrange(pivot_row+1, n):
            multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
            #A[row][pivot_row] = multiplier    
            
            L[row][pivot_row] = multiplier
            A[row][pivot_row] = 0.
            for col in xrange(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
#            #SOLUTION
            #b[row] = b[row] - multiplier*b[pivot_row]
            
    print "\nLU decomposition with no partial pivoting..\n"
    print "Upper triangular Matrix"
    print A
    print "Lower Triangular Matrix"
    print L   
    
    for i in range(n):
        b[i] = b[i]/L[i][i]
        for j in range(n):
            if j != i:
                b[i] -= L[i][j]*b[j]
    
    z=np.zeros(n)

    print "[L][Z]=[b]...finding [Z]"
    z=b
    print z
    print "[U][X]=[Z]....finding [X]"
    x = np.zeros(n)
    k = n-1
    x[k] = z[k]/A[k,k]
    while k >= 0:
        x[k] = (z[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x
 

 
if __name__ == "__main__":
    A = np.array([[25.,5.,1.],[64.,8.,1.],[144.,12.,1.]])
    b =  np.array([[106.8],[177.2],[279.2]]) 
    print A
    print b   
    
    print LUDecomposeGaussianEliminationNoPivoting(np.copy(A), np.copy(b))
    