import sympy as sp

A = sp.Matrix([ [3,0,0,7,1],
    [9,7,9,-1,4],
    [0,2,2,0,0],
    [5,-2,5,0,6],
    [1,9,7,8,-3]])

B = sp.Matrix([7,-9,6,15,-7])

X = A.solve(B)

print(X)