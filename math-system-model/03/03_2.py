# Таблиця значень функції

x = [ 0.8, 2, 2.8, 4.1, 5, 5.9, 7.3, 8.1, 9.2, 10 ]
f = [ 1.3, 2.6, 3.7, 4.5, 6.0, 7.2, 8.0, 9.2, 10.3, 11.8 ]
d = len (x)

# Формуємо матрицю А
A = []
for j in range(d-1, -1, -1):
  s = [1]
  p = 1
  for i in range(0, j):
    p = p * (x[j] - x[i])
    s.append(p)
  s.reverse ()
  A.append (s)

# Скалярний добуток
def scalar_product(A, f, n):
  s = 0
  r = len(A[n])
  for i in range (1, r-1):
    s = s + f[i] * A[n][r-i-1]
  return s

# Зворотний хід
for i in range(1, d):
  f[i] = (f[i] - f[0] - scalar_product(A, f, d-i-1)) / A[d-i-1][0]

# Формуємо поліном
polynom_string = "N(x) = " + str(f[0]) + "+"
p = "* (x-" + str(x[0]) + ")"
for i in range (1, d):
  polynom_string = polynom_string + str(f[i]) + p + '+'
  p = p + "* (x-" + str(x[i]) + ")"
polynom_string = polynom_string[: -1].replace("+-", "-")

# Виведення результату
print("Інтерполяційний поліном Ньютона ")
print(polynom_string)