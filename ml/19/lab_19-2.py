
import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/sonar.csv'
columns = [str(i) for i in range(1, 61)] + ['class']
pandas.set_option('display.max_columns', None)
dataset = pandas.read_csv(url, names=columns)

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]


# Ділення датасету на навчальну та контрольну вибірки з новим розміром вибірки
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

# Налаштування логістичної регресії
model = KNeighborsClassifier()
model.fit(X_train, Y_train)

# Прогноз на тренувальній та контрольній вибірках
model.fit(X_train, Y_train)
predictions_validation = model.predict(X_validation)
predictions_train = model.predict (X_train)

# Оцінка прогнозу на тренувальній вибірці
accuracy_train = accuracy_score(Y_train, predictions_train)
confusion_matrix_train = confusion_matrix(Y_train, predictions_train)
classification_report_train = classification_report(Y_train, predictions_train)

# Оцінка прогнозу на контрольній вибірці
accuracy_validation = accuracy_score(Y_validation, predictions_validation)
confusion_matrix_validation = confusion_matrix(Y_validation, predictions_validation)
classification_report_validation = classification_report(Y_validation, predictions_validation)

# Виведення результатів
print("Тренувальна вибірка: Точність", accuracy_train)
print("Тренувальна вибірка: Матриця помилок\n", confusion_matrix_train)
print("Тренувальна вибірка: Звіт по класифікації\n", classification_report_train)
print("Контрольна вибірка: Точність", accuracy_validation)
print("Контрольна вибірка: Матриця помилок\n", confusion_matrix_validation)
print("Контрольна вибірка: Звіт по класифікації\n", classification_report_validation)


