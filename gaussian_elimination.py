import numpy as np

A = np.array([[1.0,0.67,0.33],[0.45,1.0,0.55],[0.67,0.33,1.0]])
b = np.array([2.0,2.0,2.0])

x = np.linalg.solve(A,b)

print("The solution obtained using numpy is")
print(x)
print("solution obtained manually: x1 = 1.0, x2 = 1.0, x3 = 1.0")
