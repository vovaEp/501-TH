# Таблиця значень функції

# x = [ 0, 0.5, 1, 2, 3.5, 4, 6 ]
# f = [ 82.914, 102.491, 172.301, 281.908, 202.791, 159.072, 187.951 ]

x = [ 0.8, 2, 2.8, 4.1, 5, 5.9, 7.3, 8.1, 9.2, 10 ]
f = [ 1.3, 2.6, 3.7, 4.5, 6.0, 7.2, 8.0, 9.2, 10.3, 11.8 ]
d = len (x)

# Формуємо матрицю А
A = []
for j in range(d):
  s = []
  for i in range(d-1, -1, -1):
    s.append(x[j]**i)
  A.append(s)

# Метод Гауса
def Gauss (A, b):
  n = len(A)
  for i in range(n):
    A[i].append(b[i])
  for i in range(n):
    max_row = i
    for j in range(i + 1, n):
      if abs(A[j][i]) > abs(A[max_row][i]):
        max_row = j
    A[i], A[max_row] = A[max_row], A[i]
    for j in range(i + 1, n):
      factor = A[j][i] / A[i][i]
      for k in range(i, n + 1):
        A[j][k] -= factor * A[i][k]
  x = [0] * n
  for i in range(n - 1, -1, -1):
    x[i] = A[i][n] / A[i][i]
    for j in range(i - 1, -1, -1):
      A[j][n] -= A[j][i] * x[i]
  return x

# Обчислюємо коефіцієнти полінома
c = Gauss(A, f)

# Формуємо поліном
polynom_string = "P(x) = "
for i in range(d):
  polynom_string += str(c[i]) + "x^" + str(d-i-1) + "+"
polynom_string = polynom_string[:-5].replace("+-", "-").replace("x^1", "x")

# Відображаємо поліном
print("Інтерполяційний поліном")
print(polynom_string)