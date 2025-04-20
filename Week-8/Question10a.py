import matplotlib.pyplot as plt
x = [4, 5, 10, 4, 41, 33, 11 , 14, 6, 45, 12]
y = [10, 2, 14, 4, 75, 60, 5, 4, 10, 71,2]
plt.scatter(x,y)
plt.show()

from sklearn.cluster import KMeans
data = list(zip(x, y))
inertias = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)
plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
kmeans = KMeans(n_clusters=4)
kmeans.fit(data)
plt.scatter(x, y, c=kmeans.labels_)
plt.show()