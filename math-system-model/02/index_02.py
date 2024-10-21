import numpy as np
from numpy.linalg import solve

A = np.array([
    [3,0,0,7,1],
    [9,7,9,-1,4],
    [0,2,2,0,0],
    [5,-2,5,0,6],
    [1,9,7,8,-3],
])

B = np.array([7,-9,6,15,-7])

X = solve(A,B)

for i in range(len(X)):
    print(X[i])

