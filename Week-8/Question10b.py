import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# Data loading from a file
file_path = 'data-ungradedset.csv'
data = pd.read_csv(file_path)
print(data)
# Feature selection
feature1 = 'NM' # Change to your first feature column name
feature2 = 'NG' # Change to your second feature column name
X = data[[feature1, feature2]].values
print(X)
# Determination of the optimal number of clusters using the Elbow Method
cluster_range = range(1, 12)
wcss = [] # Within-Cluster Sum of Squares
for k in cluster_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_) # Inertia is the WCSS


# The Elbow Method graph
#plt.figure(figsize=(10, 6))
plt.plot(cluster_range, wcss, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
#plt.grid()
plt.show()
# Interactive selection of k
optimal_k = int(input("Based on the elbow plot, enter the optimal number of clusters: "))

# K-means
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42)
clusters = kmeans.fit_predict(X)
# Add cluster labels to original data
data['Cluster'] = clusters
# Plotting the clusters
print(X[clusters == 0])
#plt.figure(figsize=(10, 6))
for cluster in range(optimal_k):
    plt.scatter(X[clusters == cluster, 0], X[clusters == cluster, 1], s=50, label=f'Cluster {cluster}')

# Plot the centroids
print(kmeans.cluster_centers_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', marker='X', label='Centroids')
plt.title('K-means Clustering Results')
plt.xlabel(feature1)
plt.ylabel(feature2)
plt.legend()
plt.grid()
plt.show()
# Display the clustered data
print("Data with cluster assignments:")
print(data)