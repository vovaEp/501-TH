import numpy as np
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

input_file = 'income_data.txt'

X = []
y = []
count_class1 = 0
count_class2 = 0
max_datapoints = 30000

with open(input_file, 'r') as f:
    for line in f.readlines():
        if count_class1 >= max_datapoints and count_class2 >= max_datapoints:
            break
        if '?' in line:
            continue

        data = line[:-1].split(', ')
        if data[-1] == '<=50K' and count_class1 < max_datapoints:
            X.append(data)
            count_class1 += 1
        if data[-1] == '>50K' and count_class2 < max_datapoints:
            X.append(data)
            count_class2 += 1

X = np.array(X)

label_encoder = []
x_encoded = np.empty(X.shape)

for i, item in enumerate(X[0]):
    if item.isdigit():
        x_encoded[:, i] = X[:, i]
    else:
        label_encoder.append(preprocessing.LabelEncoder())
        x_encoded[:, i] = label_encoder[-1].fit_transform(X[:, i])

X = x_encoded[:, :-1].astype(int)
y = x_encoded[:, -1].astype(int)

# Навчання функції класифікатора
def train_classifier(test_size=0.2):
    classifier = OneVsOneClassifier(LinearSVC(random_state=0))
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=5)
    classifier.fit(x_train, y_train)

    # Оцінюємо F-measure
    y_test_pred = classifier.predict(x_test)
    f1 = f1_score(y_test, y_test_pred, average='weighted')
    return f1, classifier, x_test, y_test, y_test_pred

# 1. Розподіл (80/20)
f1_default, classifier_default, x_test_default, y_test_default, y_test_pred_default = train_classifier(test_size=0.2)
print(f'F-measure з розподілом (80/20): {f1_default:.4f}')

# 2) Налаштування розмір тестового набору до  30%
f1_test_30, classifier_test_30, x_test_30, y_test_30, y_test_pred_30 = train_classifier(test_size=0.3)
print(f'F-measure з розподілом (70/30): {f1_test_30:.4f}')

# 3) Налаштування розмір тестового набору до 40%
f1_test_40, classifier_test_40, x_test_40, y_test_40, y_test_pred_40 = train_classifier(test_size=0.4)
print(f'F-measure з розподілом (60/40): {f1_test_40:.4f}')

# 4) Збільшити розмір тренувального набору (90%)
f1_train_90, classifier_train_90, x_test_90, y_test_90, y_test_pred_90 = train_classifier(test_size=0.1)
print(f'F-measure з розподілом (90/10): {f1_train_90:.4f}')

# Порівняння
print("\nПорівння F-measures:")
print(f"F-measure (80/20): {f1_default:.4f}")
print(f"F-measure (70/30): {f1_test_30:.4f}")
print(f"F-measure (60/40): {f1_test_40:.4f}")
print(f"F-measure (90/10): {f1_train_90:.4f}")

# Прогноз за допомогою найкращої моделі
best_classifier = classifier_default  
best_label_encoder = label_encoder

data = [
    ["48","Self-emp-not-inc","265477","Assoc-acdm","12","Married-civ-spouse","Prof-specialty","Husband","White","Male","0","0","40","United-States"],
    ["31","Private","84154","Some-college","10","Married-civ-spouse","Sales","Husband","White","Male","0","0","38","?"],
    ["48","Self-emp-not-inc","265477","Assoc-acdm","12","Married-civ-spouse","Prof-specialty","Husband","White","Male","0","0","40","United-States"],
    ["31","Private","507875","9th","5","Married-civ-spouse","Machine-op-inspct","Husband","White","Male","0","0","43","United-States"],
    ["24","Private","172987","Bachelors","13","Married-civ-spouse","Tech-support","Husband","White","Male","0","0","50","United-States"],
]

for row in data:
    row[:] = ["United-States" if value == "?" else value for value in row]

for sample in data:
    print(f"Дані: {sample}")
    input_data_encoded = []
    count = 0
    for i, item in enumerate(sample):
        if item.isdigit():
            input_data_encoded.append(int(item))
        else:
            input_data_encoded.append(int(best_label_encoder[count].transform([item])[0]))
            count += 1
    input_data_encoded = np.array([input_data_encoded])
    predicted_class = best_classifier.predict(input_data_encoded)
    prediction = best_label_encoder[-1].inverse_transform(predicted_class)[0]
    print(f"Прогноз: {prediction}\n")

    