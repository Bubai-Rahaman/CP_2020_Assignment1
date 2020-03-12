import numpy as np

A = np.array([[5,-2],[-2,8]])
'''
eigh function
'''
eign,vec = np.linalg.eigh(A)

while np.all(abs(A)>1e-2):

	Q,R = np.linalg.qr(A)
	A = R @ Q
print("The einegvalues obtained by qr decomposition are")
print(A[0,0],A[1,1])

print("Eigenvalues obtained from 'numpy.linalg.eigh'")
print(eign)

