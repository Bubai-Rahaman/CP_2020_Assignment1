'''
This code is valid only for the given matrix
'''

import numpy as np
import time

def SVD(A,i,j):

	AT = A.transpose()
	ATA = AT@A
	
	eval,evec = np.linalg.eigh(ATA)
	
	AAT = A@AT
	eval1,evec1=np.linalg.eigh(AAT)
		
	m = np.arange(0,j)
	n = np.flip(m)
	
	evec[:,m]=evec[:,n]
	
	VT=evec.transpose()
	U=A@evec
	U=U/np.sqrt(np.flip(eval))
	
	m_prime = np.arange(i-j+1,i)
	col_prime = evec1[:,m_prime]
	
	U=np.column_stack((U,col_prime))
	S=np.zeros(i*j).reshape(i,j)
	
	for i1 in range (0,i):
		for j1 in range (0,j):
			if (j1<j):
				S[j1][j1]=np.sqrt(eval[j-j1-1])
	return (U,S,VT)

A=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])

t_start = time.time()
for i in range(20):
	U,S,VT = SVD(A,5,3)
t_stop = time.time()

print ("singular values obtained from my code are:", S[0][0],S[1][1],S[2][2])
print()
print("U vector from my code: ", U)
print()
print("V vector from my code: ",VT)
print()
print ("and average time taken by the code is",(t_stop-t_start)/20,"sec")
print()
t_start = time.time()
for i in range(20):
	u,s,v = np.linalg.svd(A)
t_stop = time.time()
print ("singular values from the numpy function are: ",s)
print()
print("U vector from numpy function: ", u)
print()
print("V vector from numpy fumction: ",v)
print()
print ("Average time taken by the numpy function is",(t_stop-t_start)/20,"sec")
