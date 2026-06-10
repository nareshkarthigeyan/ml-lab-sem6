# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs

# simulate tweet locations (3 cities)
centers = [[12.97, 77.59], [28.61, 77.20], [19.07, 72.87]]  # Bangalore, Delhi, Mumbai
X, _ = make_blobs(n_samples=300, centers=centers, cluster_std=0.5)

# add random noise (tweets from random places)
noise = np.random.uniform(low=[10, 70], high=[30, 90], size=(30, 2))
X = np.vstack([X, noise])

# %%
dbscan = DBSCAN(eps=0.8, min_samples=5)
labels = dbscan.fit_predict(X)
print("Cluster Labels:", labels)

# %%
unique_labels = set(labels)
for label in unique_labels:
    if label == -1:
        color = 'black'
        label_name = "Noise(Outlier)"
    else:
        color = None  # or use a color map
        label_name = f"Cluster {label}"

    plt.scatter(X[labels == label, 0],
                X[labels == label, 1],
                c=color,
                label=label_name)     
plt.title("DBSCAN Clustering of Tweet Locations")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.legend()
plt.show()

# count clusters (excluding noise)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)
print("Number of clusters:", n_clusters)
print("Number of noise points:", n_noise)


# %%


# %%



