import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.metrics import  r2_score
import numpy as np

# Отримуємо вміст файлу 
file_path = '/home/voven/501/501-TH/ml/21/data_1.txt'
data = np.loadtxt(file_path, delimiter=',')

# Розділяємо дані на змінні
# Глибина (x)
x = data[:, 0].reshape(-1, 1)  
# Температура (y)
y = data[:, 1]  

# Поділ даних 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Лінійна регресія
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

# Квадратична регресія 
# (поліном другого ступеня)
poly = PolynomialFeatures(degree=2)
x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test)
poly_reg = LinearRegression()
poly_reg.fit(x_train_poly, y_train)

# Прогнози
y_pred_lin = lin_reg.predict(x_test)
y_pred_poly = poly_reg.predict(x_test_poly)

# Метрики якості
mse_lin = mean_squared_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)

mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

plt.figure(figsize=(10, 5))

plt.scatter(x_train, y_train, color='yellow', label='Тренувальні дані')

plt.scatter(x_test, y_test, color='red', label='Тестові дані')

plt.plot(
    x, 
    lin_reg.predict(x), 
    color='green', 
    label=f'Лінійна регресія (MSE={mse_lin:.2f}, R2={r2_lin:.2f})'
)

x_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
plt.plot(
    x_range, 
    poly_reg.predict(poly.transform(x_range)), 
    color='blue', 
    label=f'Квадратична регресія (MSE={mse_poly:.2f}, R2={r2_poly:.2f})'
)

plt.xlabel('Глибина занурення датчиків, м')
plt.ylabel('Температура гірського масиву, °C')
plt.title('Лінійна та квадратична регресії залежності температури від глибини')
plt.legend()
plt.show()

print(f'Лінійна регресія: \n MSE = {mse_lin:.2f}, R2 = {r2_lin:.2f}')
print(f'Квадратична регресія: \n MSE = {mse_poly:.2f}, R2 = {r2_poly:.2f}')

