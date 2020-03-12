import numpy as np

#defining the matrix A
A = np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])

#defining the vector b
b = np.array([1,2,3,4,5])
n = len(b) #finding the number of elements in vector b

#initial guess
x0 = np.zeros(n)

TOL = 0.001 #tolarence

def mult( y, z):
	s = y@z
	return(s)

def op( b, n, A, x0):
	y = mult(A,x0)
	p = 1
	r = np.zeros(n)
	r = np.subtract(b,y)
	k = 0
	while (np.sqrt(np.dot(r,r))>TOL):
	
		y = np.dot(A,r)
		p = np.dot(r,r)/np.dot(r,y)	
		x0 = x0+ p*r
		r = np.subtract(r,p*y)
		k = k+1
	return(x0,k)
	
x,k=op(b,n,A,x0)

print("The solution is ",x)
print("and Conjugate Gradient method took ",k,"iterations")

