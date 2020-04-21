
import numpy as np
 

#ansNP=[]
def GaussianEliminationNoPivoting(A, b):
    n =  len(A)
    L=np.zeros(shape=(n,n))
    
    np.fill_diagonal(L,1.)
    
    if b.size != n:
        raise ValueError("Not compatible between A & b.", b.size, n)

    xrange=range
    for pivot_row in xrange(n-1):
        for row in xrange(pivot_row+1, n):
            multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
            #A[row][pivot_row] = multiplier
            A[row][pivot_row] = 0
            L[row][pivot_row] = multiplier
            
            for col in xrange(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
            #SOLUTION
            b[row] = b[row] - multiplier*b[pivot_row]
            
    print ("\nGaussian Elimination with no partial pivoting..\n")
    print ("Upper triangular Matrix\n"+str(A))
    print (b)
    print ("Lower Triangular Matrix")
    print (L)
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x
 
def GaussianEliminationPartialPivoting(A, b):
    n =  len(A)
    
    L=np.zeros(shape=(n,n))
    
    np.fill_diagonal(L,1.)
    
    if b.size != n:
        raise ValueError("Not compatible sizes between A & b.", b.size, n)    

    xrange=range
    for k in xrange(n-1):
        maxindex = abs(A[k:,k]).argmax() + k
        if A[maxindex, k] == 0:
            raise ValueError("Matrix is singular.")
        if maxindex != k:
            A[[k,maxindex]] = A[[maxindex, k]]
            b[[k,maxindex]] = b[[maxindex, k]]
        for row in xrange(k+1, n):
            multiplier = A[row][k]/A[k][k]
            #A[row][k] = multiplier
            A[row][k]=0
            #print multiplier
            L[row][k] = multiplier
            
            for col in xrange(k + 1, n):
                A[row][col] = A[row][col] - multiplier*A[k][col]
            #SOLUTION
            b[row] = b[row] - multiplier*b[k]
    
    print ("\nGaussian Elimination with partial pivoting..\n")
    print ("Upper triangular Matrix\n"+str(A))
    print (b)
    print ("Lower Triangular Matrix")
    print (L)
    
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x
 
if __name__ == "__main__":
    A = np.array([[25.,5.,1.],[64.,8.,1.],[144.,12.,1.]])
    b =  np.array([[106.8],[177.2],[279.2]]) 
    print (A)
    print (b)
    
    inn=np.copy(A)
    #print GaussianEliminationNoPivoting(np.copy(A), np.copy(b)) 
    ansNP = []
    ansNP = GaussianEliminationNoPivoting(np.copy(A), np.copy(b))
    realansNP = ansNP[0]*36 + ansNP[1]*6 +ansNP[2]
    print (ansNP)
    print ("\n"+str(realansNP))
    
    
    #print GaussianEliminationPartialPivoting(A,b)    
    ansPP=[]
    ansPP= GaussianEliminationPartialPivoting(A,b)
    realansPP=ansPP[0]*36 + ansPP[1]*6 +ansPP[2]
    print (ansPP)
    print ("\n"+str(realansPP))
    
    
    #print inn
    inverse=np.linalg.inv(inn)
    
    print ("\ninverse Matrix of A")
    print (inverse)