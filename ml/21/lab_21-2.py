import numpy as np
import matplotlib.pyplot as plt

# Читаємо дані з файлу
file_path = '/home/voven/501/501-TH/ml/21/data_singlevar_regr.txt'
data = np.loadtxt(file_path, delimiter=',')

# Розділимо дані на змінні x та y
x = data[:, 0]
y = data[:, 1]

# Нормалізація даних для покращення збіжності 
# градієнтного спуску
x = (x - np.mean(x)) / np.std(x)
y = (y - np.mean(y)) / np.std(y)

# Початкові значення параметрів моделі
theta_0 = 0
theta_1 = 0

# Параметри градієнтного спуску
learn_rate = 0.01
iterations = 1000
m = len(y)  # Кількість прикладів

# Функція для обчислення квадратичної функції втрат 
# (середньоквадратична похибка)
def compute_cost(theta_0, theta_1, x, y):
    return np.sum((theta_0 + theta_1 * x - y) ** 2) / (2 * m)

# Функція для виконання градієнтного спуску
def gradient_descent(x, y, theta_0, theta_1, learning_rate, num_iterations):
    cost_history = []
    for i in range(num_iterations):
        # Обчислюємо передбачення
        predictions = theta_0 + theta_1 * x

        # Оновлення параметрів за градієнтним спуском
        theta_0 -= learning_rate * np.sum(predictions - y) / m
        theta_1 -= learning_rate * np.sum((predictions - y) * x) / m

        # Обчислюємо та зберігаємо поточну вартість 
        # (функцію втрат)
        cost = compute_cost(theta_0, theta_1, x, y)
        cost_history.append(cost)

    return theta_0, theta_1, cost_history

# Виконуємо градієнтний спуск для отримання параметрів
theta_0, theta_1, cost_history = gradient_descent(x, y, theta_0, theta_1, learn_rate, iterations)

# Функція для передбачення значень
def predict(x):
    return theta_0 + theta_1 * x

# Побудова графіку
plt.scatter(x, y, color='green', label='Тренувальні дані')
plt.plot(x, predict(x), color='red', label=f'Лінійна регресія: y = {theta_0:.2f} + {theta_1:.2f}x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Лінійна регресія (квадратична функція втрат)')
plt.show()

# Графік зміни функції втрат
plt.plot(range(iterations), cost_history)
plt.xlabel('Номер ітерації')
plt.ylabel('Вартість (функція втрат)')
plt.title('Збіжність градієнтного спуску')
plt.show()

# Виведемо значення theta0 та theta1
print(f"θ0 = {theta_0:.4f}, θ1 = {theta_1:.4f}")