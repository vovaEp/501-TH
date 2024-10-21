from sklearn.datasets import load_iris
iris_dataset = load_iris()
print('Iris dataset keys: \n{}'.format(iris_dataset.keys()), '\n')
print(iris_dataset['data'][:20], '\n')
print(iris_dataset['data'][0][1], '\n')

rainbow = {'red': 620, 'green': 585}
for j in rainbow.items():
    print(j, end='\n')

for j in rainbow.values():
    print(j, end='\n')

rainbow_list = list(rainbow.items())
print(rainbow_list)

rainbow_tuple = tuple(rainbow.items())
print(rainbow_tuple)

rainbow['greeeeen'] = rainbow.pop('green')
for j in rainbow.items():
    print(j, end='\n')