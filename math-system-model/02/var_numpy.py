import numpy as np
from numpy.linalg import solve

A = np.array([
    [1,2,1],
    [2,-3,-1],
    [1,1,2]
])

B = np.array([6,-5,5])

X = solve(A,B)

for i in range(len(X)):
    print(X[i])

# результат
1.0
1.9999999999999998
1.0000000000000007
