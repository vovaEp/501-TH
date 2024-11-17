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

print(f"Class 1 count: {count_class1}")
print(f"Class 2 count: {count_class2}")

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
classifier = OneVsOneClassifier(LinearSVC(random_state=0))
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
classifier.fit(x_train, y_train)

 # Оцінюємо F-measure
y_test_pred = classifier.predict(x_test)
f1 = f1_score(y_test, y_test_pred, average='weighted')
print(f'F-measure для тестового набору: {f1:.4f}')

# Невикористаний зразок
unused_sample = x_test[10] 
unused_true_class = y_test[10]

print(f"Невикористаний зразок: {unused_sample}")
print(f"Реальні дані: {'<=50K' if unused_true_class == 0 else '>50K'}")

# Зробити прогноз
input_data_encoded = unused_sample
predicted_class = classifier.predict([input_data_encoded])[0]
prediction = '<=50K' if predicted_class == 0 else '>50K'
print(f"Прогноз для невикористаного зразка: {prediction}")

if predicted_class == unused_true_class:
    print("Прогноз моделі вірний!")
else:
    print("Прогноз моделі невірний")