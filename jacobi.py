import numpy as np

#defining the matrix A
A = np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])

#defining the vector b
b = np.array([1,2,3,4,5])

#defining initial guess
x0 = np.zeros(5)
x = np.zeros(5)

TOL = 0.01 #defining the tolarence
k = 0
while True:
	for i in range(5):
		s = 0
		for j in range(5):
			if i==j:
				continue
			s = s+ A[i,j]*x0[j]				 
		x[i] = (b[i]-s)/A[i,i]
	k = k+1
	if (np.sqrt(np.dot(x-x0,x-x0))<TOL):
		break
	x0 = x.copy()

print("The solution is ",x)
print("and Jacobi method took ",k,"iterations")
