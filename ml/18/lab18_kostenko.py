import numpy
import pandas
import sys
import scipy
import matplotlib
import sklearn

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Завантаження датасету
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/banknote_authentication.csv'
columns = ['variance', 'skewness','curtosis','entropy','class']
dataset = pandas.read_csv(url, names=columns)

# Статистика датасету
#print (dataset.describe())

#print(dataset.shape)
#print(dataset.head(15))

#
#print(dataset.describe())


# Розподіл значень
# print(dataset.groupby('class').size())

# Результат:
# class
# 0    762
# 1    610

# Діаграма розмаху
dataset.iloc[:, :-1].plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
matplotlib.pyplot.show()

# Гістограма
#dataset.iloc[:, :-1].hist()
#matplotlib.pyplot.show()

# Матриця
#pandas.plotting.scatter_matrix(dataset.iloc[:, :-1])
#matplotlib.pyplot.show()



# Розподіляємо датасет на навчальну та контрольну вибірки
arr = dataset.values
X = arr[:, 0:4]
y = arr[:, 4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

# Завантаження моделей алгоритмів
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma= 'auto')))

# Оцінка точності моделей
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
print("\n")

# Візуалізація результатів навчання
matplotlib.pyplot.boxplot(results)
matplotlib.pyplot.title('Algorithm comparison')
matplotlib.pyplot.show()

#---
# LR: 0.989033 (0.010692)
# LDA: 0.978090 (0.014279)
# KNN: 1.000000 (0.000000)
# CART: 0.982677 (0.013181)
# NB: 0.844037 (0.039527)
# SVM: 1.000000 (0.000000)

#------
# Ділення датасету на навчальну та контрольну вибірки з новим розміром вибірки
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.30, random_state=1)

# Налаштування логістичної регресії з доданою регуляризацією
model = LogisticRegression(solver='liblinear', multi_class='ovr', C=0.7)
model.fit(X_train, Y_train)

# Прогноз на тренувальній та контрольній вибірках
model.fit(X_train, Y_train)
predictions_validation = model.predict(X_validation)
predictions_train = model.predict (X_train)

# Оцінка прогнозу на тренувальній вибірці
training_accuracy = accuracy_score(Y_train, predictions_train)
training_confusion_matrix = confusion_matrix(Y_train, predictions_train)
training_classification_report = classification_report(Y_train, predictions_train)

# Оцінка прогнозу на контрольній вибірці
control_accuracy = accuracy_score(Y_validation, predictions_validation)
control_confusion_matrix = confusion_matrix(Y_validation, predictions_validation)
control_classification_report = classification_report(Y_validation, predictions_validation)

# Виведення результатів
print("Тренувальна вибірка: Точність", training_accuracy)
print("Тренувальна вибірка: Матриця помилок \n", training_confusion_matrix)
print("\n")
print("Тренувальна вибірка: Звіт по класифікації:\n", training_classification_report)
print("Контрольна вибірка: Точність", control_accuracy)
print("Контрольна вибірка: Матриця помилок: \n", control_confusion_matrix)
print("\n")
print("Контрольна вибірка: Звіт по класифікації: \n", control_classification_report)




