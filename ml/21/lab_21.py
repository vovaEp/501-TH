import numpy as np
import matplotlib.pyplot as plt

# Читаємо дані з файлу
file_path = '/home/voven/501/501-TH/ml/21/data_singlevar_regr.txt'
data = np.loadtxt(file_path, delimiter=',')

# Розділимо дані на змінні x та y
x = data[:, 0]
y = data[:, 1]

# Обчислимо суми
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x_squared = np.sum(x**2)
sum_xy = np.sum(x * y)

# Система рівнянь для знаходження theta0 та theta1
theta_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
theta_0 = (sum_y - theta_1 * sum_x) / n

# Створимо функцію для передбачення
def predict(x):
    return theta_0 + theta_1 * x

# Будуємо графік
plt.scatter(x, y, color='green', label='Тренувальні дані')
plt.plot(x, predict(x), color='red', label=f'Лінійна регресія: y = {theta_0:.2f} + {theta_1:.2f}x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Лінійна регресія')
plt.show()

# Виведемо значення theta0 та theta1
print(f"θ0 = {theta_0:.4f}, θ1 = {theta_1:.4f}")