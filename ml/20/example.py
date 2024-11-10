import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.model_selection import train_test_split, cross_val_score

input_file = 'income_data.txt'

x = []
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
            x.append(data)
            count_class1 += 1
        if data[-1] == '>50K' and count_class1 < max_datapoints:
            x.append(data)
            count_class2 +=1

x = np.array(x)

label_encoder = []
x_encoded = np.empty(x.shape)

for i, item in enumerate(x[0]):
    if item.isdigit():
        x_encoded[:,i] = x[:,i]
    else:
        label_encoder.append(preprocessing.LabelEncoder())
        x_encoded[:,i] = label_encoder[-1].fit_transform(x[:,i])
x = x_encoded[:,:-1].astype(int)
y = x_encoded[:,-1].astype(int)

#create classifier
classifier = OneVsOneClassifier(LinearSVC(random_state=0))

classifier.fit(x,y)

#crossvalidation
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=5) 
classifier = OneVsOneClassifier(LinearSVC(random_state=0))
classifier.fit(x_train, y_train)

y_test_pred = classifier.predict(x_test)

#print(x)

#calculating
input_data = ['37', 'Private', '215646', 'HS-grad', '9', 'Never-married','Handlers-cleaners','Not-in-family','White','Male','0','0','40', 'United-States']

#prediction
input_data_encoded = [-1]*len(input_data)
count = 0

for i, item in enumerate(input_data):
    if item.isdigit():
        input_data_encoded[i] = int(input_data[i])
    else:
         #print(label_encoder[count].transform([input_data[i]])[0])
         input_data_encoded[i] = int(label_encoder[count].transform([input_data[i]])[0])
         count+=1

input_data_encoded = np.array([input_data_encoded])

predicted_class = classifier.predict(input_data_encoded)
print(label_encoder[-1].inverse_transform(predicted_class)[0])