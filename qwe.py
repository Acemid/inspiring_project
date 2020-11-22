import numpy as np
A=([1,2,3],[4,5,6],[7,8,9])
print(A)
b = ([29,32,28])
x = np.linalg.solve(A,b)
print(x)
