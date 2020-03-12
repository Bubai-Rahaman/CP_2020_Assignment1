import numpy as np

A = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])

def eigenvalue(A, x):
	Ax = A.dot(x)
	return(x.dot(Ax))


def power_iteration(A):
	
	n,d = A.shape
	
	x = np.ones(d)/np.sqrt(d)
	
	eignv = eigenvalue(A, x)
	
	while True:
		Ax = A.dot(x)
		x_new = Ax/np.linalg.norm(Ax)
		
		eignv_new = eigenvalue(A, x_new)
		if np.abs(eignv - eignv_new)<0.01:
			break
		
		x = x_new
		eignv = eignv_new
	return(eignv_new, x_new)
	
ev,v = power_iteration(A)

print (" The eigenvalue is ",ev)
print("The eigen vector is ",v) 

