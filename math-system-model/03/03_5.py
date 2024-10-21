import sympy as sp
from sympy import *

x = Symbol('x')

polynomial = (-2.089755005016802e-06 * (x-2) *(x-2.8) *(x-4.1) *(x-5) *(x-5.9) *(x-7.3)* (x-8.1) *(x-9.2) *(x-10) \
+5.9192784531021045e-05*(x-0.8)* (x-2.8)* (x-4.1)* (x-5) *(x-5.9) *(x-7.3) *(x-8.1) *(x-9.2) *(x-10) \
-0.0002373302849438983*(x-0.8) *(x-2)* (x-4.1) *(x-5) *(x-5.9) *(x-7.3) *(x-8.1) *(x-9.2) *(x-10) \
+0.0008005505402204191*(x-0.8)* (x-2)* (x-2.8) *(x-5) *(x-5.9)* (x-7.3)* (x-8.1) *(x-9.2) *(x-10) \
-0.001784695715252198*(x-0.8) *(x-2) *(x-2.8) *(x-4.1) *(x-5.9) *(x-7.3) *(x-8.1) *(x-9.2)* (x-10) \
+0.001729706796293429*(x-0.8)* (x-2)* (x-2.8) *(x-4.1) *(x-5)* (x-7.3) *(x-8.1) *(x-9.2) *(x-10) \
-0.0012203236972844899*(x-0.8) *(x-2) *(x-2.8)* (x-4.1) *(x-5)* (x-5.9) *(x-8.1)* (x-9.2) *(x-10) \
+0.000854630963812717*(x-0.8) *(x-2) *(x-2.8)* (x-4.1) *(x-5) *(x-5.9) *(x-7.3) *(x-9.2)* (x-10) \
-0.00022515198944788605*(x-0.8)* (x-2) *(x-2.8) *(x-4.1) *(x-5)* (x-5.9) *(x-7.3) *(x-8.1) *(x-10) \
+4.4859917621974715e-05*(x-0.8) *(x-2) *(x-2.8) *(x-4.1) *(x-5) *(x-5.9) *(x-7.3) *(x-8.1)* (x-9.2) )

# Розкриваємо дужки та спрощуємо вираз
simplified_polynomial = expand(polynomial)

# Спрощення полінома Лагранжа
s = sp.simplify(polynomial)

print("Інтерполяційний поліном")
print("P(x)= " + str(simplified_polynomial))