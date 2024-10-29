import pandas
from matplotlib import pyplot
import seaborn 
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/sonar.csv'
columns = [str(i) for i in range(1, 61)] + ['class']
pandas.set_option('display.max_columns', None)
dataset = pandas.read_csv(url, names=columns)

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]


X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

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
    names.append (name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
print("\n")

# Візуалізація результатів навчання 
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm comparison')
pyplot.show()



#pyplot.figure(figsize=(12, 6))
#seaborn.boxplot(data=dataset.iloc[:, :-1])
#pyplot.title("Розподіл значень ознак")
#pyplot.show()

#print(dataset.shape)
#print(dataset.head(10))
#print("\n")

#print(dataset.describe())
#print("\n")

#print(dataset.groupby('class').size())
#print("\n")

# Діаграма розмаху
#dataset.iloc[:,:-1].plot(
#    kind='box',
#    subplots=True,
#    layout=(2,2),
#    sharex=False,
#    sharey=False
#)

# Гістограма розподілу значень атрибутів
#dataset.hist()

# Матриця діаграм розподілу
#pandas.plotting.scatter_matrix(dataset)

#pyplot.show()

