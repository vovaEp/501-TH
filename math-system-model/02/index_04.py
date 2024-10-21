import sympy as sp

a11 = sp.symbols('a11')
a12 = sp.symbols('a12')
a21 = sp.symbols('a21')
a22 = sp.symbols('a22')

b1 = sp.symbols('b1')
b2 = sp.symbols('b2')

A = sp.Matrix([[a11,a12], [a21,a22]])

B = sp.Matrix([b1,b2])

X = A.solve(B)

print(X)