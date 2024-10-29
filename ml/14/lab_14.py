import pickle
import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

input_file = '/home/voven/501/501-TH/ml/14/data_singlevar_regr.txt'
data = np.loadtxt(input_file, delimiter=',')

X, y = data[:, :-1], data[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0)

regressor = linear_model.LinearRegression()

regressor.fit(X_train, y_train)

y_test_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color='red', s=10, label='Тренувальні дані')
plt.scatter(X_test, y_test, color='green', label='Тестові дані')
Y_red = regressor.predict(X)

plt.plot(X,Y_red, color='black', linewidth=2, label='Лінійна регресія')
plt.xticks(())
plt.yticks(())
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()