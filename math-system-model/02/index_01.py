#  Матриця А та вектор B
A = [
    [3,0,0,7,1],
    [9,7,9,-1,4],
    [0,2,2,0,0],
    [5,-2,5,0,6],
    [1,9,7,8,-3],
]

B = [7,-9,6,15,-7]

d = len(B)

for m in range(0,d-1):
    for j in range(m+1,d):
        k = A[j][m] / A[m][m]
        for i in range(m,d):
            A[j][i] = A[j][i] - k*A[m][i]
        B[j] = B[j] - k*B[m]

# Скалярний добуток
def scalar_product(A,B,n):
    s = 0
    for i in range(n+1, d):
        s = s + A[n][i]*B[i]
    return s

# Зворотній хід
for i in range(d-1, -1,-1):
    B[i] = (B[i] - scalar_product(A,B,i)) / A[i][i]

# Відображення результатів
print("Матриця А після перетворень прямого ходу")
for i in range(0,d):
    print(A[i])
print("")
print("Вектор розв'язку x")
for i in range(0,d):
    print(B[i])