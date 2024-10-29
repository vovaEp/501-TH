import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Завантаження даних каротажних досліджень
file_path = '/home/voven/501/501-TH/ml/21/data_1.txt'
data = np.loadtxt(file_path, delimiter=",")
X, y = data[:, 0].reshape(-1, 1), data[:, 1]

# Розділення на навчальний та тестовий набори
num_training = int(0.8 * len(X))
num_test = len(X) - num_training

X_train, y_train = X[:num_training], y[:num_training]
X_test, y_test = X[num_training:], y[num_training:]

# Лінійна регресія
linear_regressor = linear_model.LinearRegression()
linear_regressor.fit(X_train, y_train)

# Поліноміальна регресія
poly = PolynomialFeatures(degree=3)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

poly_linear_model = linear_model.LinearRegression()
poly_linear_model.fit(X_poly_train, y_train)

# Прогнозування
y_test_pred_linear = linear_regressor.predict(X_test)
y_test_pred_poly = poly_linear_model.predict(X_poly_test)

# Візуалізація
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color="yellow", label="Тренувальні дані")
plt.scatter(X_test, y_test, color="orange", label="Тестові дані")
plt.plot(X_test, y_test_pred_linear, color="green", label="Лінійна регресія")
plt.plot(X_test, y_test_pred_poly, color="blue", label="Поліноміальна регресія")
plt.xlabel("Глибина")
plt.ylabel("Температура")
plt.title("Залежність температури від глибини (каротажні дослідження)")
plt.legend()
plt.show()

# Метрики якості для лінійної регресії
print("\n Лінійна регресія:")
print(
    "Середня абсолютна помилка =",
    round(sm.mean_absolute_error(y_test, y_test_pred_linear), 2),
)
print(
    "Середньоквадратична помилка =",
    round(sm.mean_squared_error(y_test, y_test_pred_linear), 2),
)
print(
    "Медіанна абсолютна помилка =",
    round(sm.median_absolute_error(y_test, y_test_pred_linear), 2),
)
print("R2 оцінка =", round(sm.r2_score(y_test, y_test_pred_linear), 2))

# Метрики якості для поліноміальної регресії
print("\n Поліноміальна регресія:")
print(
    "Середня абсолютна помилка =",
    round(sm.mean_absolute_error(y_test, y_test_pred_poly), 2),
)
print(
    "Середньоквадратична помилка =",
    round(sm.mean_squared_error(y_test, y_test_pred_poly), 2),
)
print(
    "Медіанна абсолютна помилка =",
    round(sm.median_absolute_error(y_test, y_test_pred_poly), 2),
)
print("R2 оцінка =", round(sm.r2_score(y_test, y_test_pred_poly), 2))



