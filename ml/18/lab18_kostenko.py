import numpy
import pandas
import sys
import scipy
import matplotlib
import sklearn
import mglearn

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/banknote_authentication.csv'
columns = ['variance', 'skewness','curtosis','entropy','class']
dataset = pandas.read_csv(url, names=columns)
print(dataset.shape)
print(dataset.head(20))

#
print(dataset.describe())

#
print(dataset.groupby('class').size())

#
dataset.plot(kind='box', subplots=True, layout=(5,5), sharex=False, sharey=False)
matplotlib.pyplot.show()

dataset.hist()
matplotlib.pyplot.show()

pandas.plotting.scatter_matrix(dataset)
matplotlib.pyplot.show()
