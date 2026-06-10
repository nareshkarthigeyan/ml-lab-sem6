# %% [markdown]
# #1.Load Dataset

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import warnings
from scipy.stats import mode
from sklearn.metrics import accuracy_score
import numpy as np


iris = datasets.load_iris()
X = iris.data  
y = iris.target  
print("Shape:", X.shape)

# %% [markdown]
# #2.K-Means Clustering

# %%

kmeans = KMeans(n_clusters=3, random_state=0)
kmeans_labels = kmeans.fit_predict(X)

print("K-Means Labels:\n", kmeans_labels)
#warnings.filterwarnings("ignore")

# %% [markdown]
# #3.EM Algorithm (GMM)

# %%

gmm = GaussianMixture(n_components=3, random_state=0)
gmm_labels = gmm.fit_predict(X)

print("GMM Labels:\n", gmm_labels)

# %% [markdown]
# #4.Evaluation (Clustering Quality)

# %%

# Function to match labels (since cluster labels may differ)
def match_labels(true, pred):
    from scipy.stats import mode
    labels = np.zeros_like(pred)
    for i in range(3):
        mask = (pred == i)
        labels[mask] = mode(true[mask])[0]
    return labels

kmeans_matched = match_labels(y, kmeans_labels)
gmm_matched = match_labels(y, gmm_labels)

print("K-Means Accuracy:", accuracy_score(y, kmeans_matched))
print("GMM Accuracy:", accuracy_score(y, gmm_matched))

# %% [markdown]
# #5.Visualization (2D Projection)

# %%


plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis')
plt.title("K-Means Clustering")
plt.show()

plt.scatter(X[:, 0], X[:, 1], c=gmm_labels, cmap='viridis')
plt.title("GMM (EM) Clustering")
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import accuracy_score
from scipy.stats import mode

iris = datasets.load_iris()
X = iris.data
y = iris.target

print("Shape:", X.shape)

# K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans_labels = kmeans.fit_predict(X)
print("K-Means Labels:\n", kmeans_labels)

# GMM (EM Algorithm)
gmm = GaussianMixture(n_components=3, random_state=0)
gmm_labels = gmm.fit_predict(X)
print("GMM Labels:\n", gmm_labels)

# Function to match cluster labels with true labels
def match_labels(true, pred):
    labels = np.zeros_like(pred)
    for i in range(3):
        mask = (pred == i)
        if np.any(mask):  # avoid empty cluster error
            labels[mask] = mode(true[mask], keepdims=True)[0]
    return labels

# Match labels
kmeans_matched = match_labels(y, kmeans_labels)
gmm_matched = match_labels(y, gmm_labels)

# Accuracy
print("K-Means Accuracy:", accuracy_score(y, kmeans_matched))
print("GMM Accuracy:", accuracy_score(y, gmm_matched))

plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis')
plt.title("K-Means Clustering")
plt.show()

plt.scatter(X[:, 0], X[:, 1], c=gmm_labels, cmap='viridis')
plt.title("GMM (EM) Clustering")
plt.show()

# %%



