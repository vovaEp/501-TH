# Таблиця значень функції
x = [ 0.8, 2, 2.8, 4.1, 5, 5.9, 7.3, 8.1, 9.2, 10 ]
f = [ 1.3, 2.6, 3.7, 4.5, 6.0, 7.2, 8.0, 9.2, 10.3, 11.8 ]
d = len (x)

a = []
L = []

# Формуємо коефіцієнти та складові частини полінома
for j in range(d):
  p = 1
  s = ''
  for i in range(d):
    if i == j:
      continue 
    else:
      p = p * (x[j] - x[i])
      s = s + "(x-" + str(x[i]) + ") "
  k = f[j] / p
  a.append(k)
  L.append(s)

# Формуємо поліном
polynom_string = "L(x) = "
for i in range(d):
  polynom_string = polynom_string + str(a[i]) + "*" + L[i] + "+"
polynom_string = polynom_string[: -1].replace("+-", "-")

# Результат
print("Інтерполяційний поліном Лагранжа ")
print(polynom_string)