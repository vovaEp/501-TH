import sympy as sp

A = sp.Matrix([
    [1,2,1],
    [2,-3,-1],
    [1,1,2]
])

B = sp.Matrix([6,-5,5])

X = A.solve(B)

print(X)

# результат
Matrix([[1], [2], [1]])