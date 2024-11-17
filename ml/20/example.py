import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.model_selection import train_test_split

input_file = 'income_data.txt'

X = []
y = []
count_class1 = 0
count_class2 = 0
max_datapoints = 30000

with open (input_file, 'r') as f:
    for line in f.readlines():
        if count_class1 >= max_datapoints and count_class2 >= max_datapoints:
            break
        if '?' in line:
            continue

        data = line[:-1].split(', ')
        if data[-1] == '<=50K' and count_class1 < max_datapoints:
            X.append(data)
            count_class1 += 1
        if data[-1] == '>50K' and count_class1 < max_datapoints:
            X.append(data)
            count_class2 +=1

X = np.array(X)

label_encoder = []
X_encoded = np.empty(X.shape)

for i, item in enumerate(X[0]):
    if item.isdigit():
        X_encoded[:,i] = X[:,i]
    else:
        label_encoder.append(preprocessing.LabelEncoder())
        X_encoded[:,i] = label_encoder[-1].fit_transform(X[:,i])
X = X_encoded[:,:-1].astype(int)
y = X_encoded[:,-1].astype(int)

# Create classifier
classifier = OneVsOneClassifier(LinearSVC(random_state=0))

classifier.fit(X,y)

# Crossvalidation
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=5) 
classifier = OneVsOneClassifier(LinearSVC(random_state=0))
classifier.fit(x_train, y_train)

y_test_pred = classifier.predict(x_test)

# Calculating
input_data = ['37', 'Private', '215646', 'HS-grad', '9', 'Never-married', 'Handlers-cleaners', 'Not-in-family', 'White', 'Male', '0', '0', '40', 'United-States']

# Prediction
input_data_encoded = [-1]*len(input_data)

count = 0

for i, item in enumerate(input_data):
    if item.isdigit():
        input_data_encoded[i] = int(input_data[i])
    else:
         print(label_encoder[count].transform([input_data[i]])[0])
         input_data_encoded[i] = int(label_encoder[count].transform([input_data[i]])[0])
         count+=1

input_data_encoded = np.array([input_data_encoded])

predicted_class = classifier.predict(input_data_encoded)
print(label_encoder[-1].inverse_transform(predicted_class)[0])