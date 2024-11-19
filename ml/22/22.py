import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics

X = np.loadtxt('data_clustering.txt', delimiter = ',')

num_clusters = 5

plt.figure()
plt.scatter(X[:,0], X[:,1], marker='o', facecolors='none', edgecolor='black', s=80)
x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1

plt.title('input data')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

plt.show()
print(x_min, x_max, y_min, y_max)

# Create object KMeans
kmeans = KMeans(init= 'k-means++', n_clusters=num_clusters, n_init=10)
# kmeans= KMeans(n_clusters=6)
# Learning kmeans
kmeans.fit(X)

# Visualisation borders of clusters
step_size = 0.01

# Grid

x_vals, y_vals = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))
output = kmeans.predict(np.c_[x_vals.ravel(), y_vals.ravel()])

# visualization of region
output = output.reshape(x_vals.shape)
plt.figure()
plt.clf()
plt.imshow(output, interpolation='nearest', extent=( x_vals.min(), x_vals.max(), y_vals.min(), y_vals.max()), cmap=plt.cm.Paired, aspect='auto', origin='lower' )

# 2
#plt.show()
plt.scatter(X[:,0], X[:,1], marker='o', facecolor='none', edgecolor='black', s=80)

# 3
plt.show()

# 4 +Center of 
cluster_centers = kmeans.cluster_centers_
plt.scatter(cluster_centers[:,0], cluster_centers[:,1], marker='o', s=200, linewidths=4, color='gray', zorder=12, facecolor='black')
plt.title('Borders of clusters')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks()
plt.yticks()

plt.show()